'''
====== Legal notices

Copyright (C) 2013 - 2021 GEATEC engineering

This program is free software.
You can use, redistribute and/or modify it, but only under the terms stated in the QQuickLicense.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY, without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the QQuickLicense for details.

The QQuickLicense can be accessed at: http://www.qquick.org/license.html

__________________________________________________________________________


 THIS PROGRAM IS FUNDAMENTALLY UNSUITABLE FOR CONTROLLING REAL SYSTEMS !!

__________________________________________________________________________

It is meant for training purposes only.

Removing this header ends your license.
'''
#!/usr/bin/env python

import time as tm
import traceback as tb
import math as mt
import sys as ss
import os
import socket as sc
import tensorflow as tf
import numpy as np
keras = tf.keras


ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw
import parameters as pm

model_sonar_path = r'../P1_KevinVanDerMeer/norm_sonar_model_01'
#model_lidar_path = r'../P1_KevinVanDerMeer/norm_lidar_model_01'


class DrivingAgent:
    def __init__ (self):
        self.model = None
        self.steeringAngle = 0
        with open (pm.sampleFileName, 'w') as self.sampleFile:
            with sc.socket (*sw.socketType) as self.clientSocket:
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)
                self.halfApertureAngle = False

                while True:
                    self.input ()
                    self.sweep ()
                    self.output ()
                    tm.sleep (0.02)

    def input (self):
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim 
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
            if self.model==None:
                self.model = tf.keras.models.load_model(model_lidar_path)           
        else:
            self.sonarDistances = sensors ['sonarDistances']
            if self.model==None:
                self.model = tf.keras.models.load_model(model_sonar_path) 


    def lidarSweep (self):
        sample = self.model.predict(np.array([self.lidarDistances]))        
        steeringangle = self.model.predict(np.array([sample[0:16]])) 
        self.steeringAngle = float(steeringangle[0]) 
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle) 

    def sonarSweep (self):
        sample = self.model.predict(np.array([self.sonarDistances]))
        self.steeringAngle = float(sample[0][0])
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sweep (self):
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)


DrivingAgent ()
