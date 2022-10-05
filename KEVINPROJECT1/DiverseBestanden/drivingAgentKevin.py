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

import time as tm               # Voor 'time out', niet elke milliseconde rekenen
#import traceback as tb
#import math as mt
import sys as ss                #Systeem
import os                       #Operating System
import socket as sc             #Communicatie tussen 'world' en 'drivingagent'
import tensorflow as tf         #library TF voor het importeren en gebruik van mijn model
import numpy as np              #library NP voor numerieke berekeningen in matrices
keras = tf.keras                #keras (als onderdeel van TF) voor met name de layers


ss.path +=  [os.path.abspath (relPath) for relPath in  ('..',)] 

import socket_wrapper as sw     #zie socket
import parameters as pm         #noodzakelijke module

model_sonar_path = 'C:/Users/kcvan/MakeAIWork/KEVINPROJECT1/norm_sonar_model_01'
#model_lidar_path = 'C:/Users/kcvan/MakeAIWork/KEVINPROJECT1/norm_lidar_model_01'


class DrivingAgent:                     #als klasse omdat onderstaande functies in 1 x worden aangeroepen bij aanroepen klasse
    def __init__ (self):                #class constructor
        self.model = None                         
        self.steeringAngle = 0
        with open (pm.sampleFileName, 'w') as self.sampleFile:
            with sc.socket (*sw.socketType) as self.clientSocket:
                self.clientSocket.connect (sw.address)
                self.socketWrapper = sw.SocketWrapper (self.clientSocket)   # van World naar Car en vice versa, ontvangen en sturen van data
                self.halfApertureAngle = False

                while True:
                    self.input ()
                    self.sweep ()
                    self.output ()
                    # self.logTraining ()
                    tm.sleep (0.02)         #timeout voor processor, tevens punt waarin nieuwe stuurhoek wordt doorgegeven

    def input (self):
        sensors = self.socketWrapper.recv ()

        if not self.halfApertureAngle:
            self.halfApertureAngle = sensors ['halfApertureAngle']
            self.sectorAngle = 2 * self.halfApertureAngle / pm.lidarInputDim 
            self.halfMiddleApertureAngle = sensors ['halfMiddleApertureAngle']
            
        if 'lidarDistances' in sensors:
            self.lidarDistances = sensors ['lidarDistances']
            if self.model==None:
                self.model = tf.keras.models.load_model(model_lidar_path) #lidar uit model path inladen           
        else:
            self.sonarDistances = sensors ['sonarDistances']
            if self.model==None:
                self.model = tf.keras.models.load_model(model_sonar_path) #sonar uit model path inladen


    def lidarSweep (self):                                                          #Must have in MoSCoW notatie
        sample = self.model.predict(np.array([self.lidarDistances]))        
        steeringangle = self.model.predict(np.array([sample[0:16]])) 
        self.steeringAngle = float(steeringangle[0]) 
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle) 

    def sonarSweep (self):                                                          #Must have in MoSCoW notatie
        sample = self.model.predict(np.array([self.sonarDistances]))
        self.steeringAngle = float(sample[0][0])
        self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)

    def sweep (self):                                                               #keuze uit lidarsweep/sonarsweep. In de sweep gebeurt het meeste.
        if hasattr (self, 'lidarDistances'):
            self.lidarSweep ()
        else:
            self.sonarSweep ()

    def output (self):                                                              #Must have in MoSCoW notatie: nieuwe output naar SW essentieel
        actuators = {
            'steeringAngle': self.steeringAngle,
            'targetVelocity': self.targetVelocity
        }

        self.socketWrapper.send (actuators)             # Hier worden de nieuwe stuurhoek en snelheid doorgegeven aan Car

    # def logLidarTraining (self):                                                                  #loggen data niet noodzakelijk in getrainde versie
    #     sample = [pm.finity for entryIndex in range (pm.lidarInputDim + 1)]                       #Won't have - in MoSCoW notatie

    #     for lidarAngle in range (-self.halfApertureAngle, self.halfApertureAngle):
    #         sectorIndex = round (lidarAngle / self.sectorAngle)
    #         sample [sectorIndex] = min (sample [sectorIndex], self.lidarDistances [lidarAngle])
    #     steeringangle = self.model.predict(np.array([sample]))

    #     self.steeringAngle = float(steeringangle[0][0])

    #     self.targetVelocity = pm.getTargetVelocity (self.steeringAngle)
    #     sample [-1] = self.steeringAngle
    #     print (*sample, file = self.sampleFile)

    # def logSonarTraining (self):
    #     sample = [pm.finity for entryIndex in range (pm.sonarInputDim + 1)]

    #     for entryIndex, sectorIndex in ((2, -1), (0, 0), (1, 1)):
    #         sample [entryIndex] = self.sonarDistances [sectorIndex]

    #     sample [-1] = self.steeringAngle
    #     print (*sample, file = self.sampleFile)

    # def logTraining (self):
    #     if hasattr (self, 'lidarDistances'):
    #         self.logLidarTraining ()
    #     else:
    #         self.logSonarTraining ()
    
    #def main():  
    #     agent = DrivingAgent(name="NissanJuke")
    #     print("The agent is driving")
            
    # if __name__ == "__main__":
    #     main()
        
DrivingAgent ()    #.main() #helaas zonder main functie, dit kreeg ik niet werkend. Could have - in MoSCoW notatie (Jeroen zou zeggen Should have)
