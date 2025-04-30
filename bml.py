from collections import Counter
from qibullet import SimulationManager
from gtts import gTTS
from playsound import playsound
import threading
import time
import json
import xmltodict

class BehaviorRealizer():

    def __init__(self):
        # Loading Robot and  Ground
        simulation_manager = SimulationManager()
        client = simulation_manager.launchSimulation(gui=True)
        self.pepper = simulation_manager.spawnPepper(client, spawn_ground_plane=True)

    def speak_peper(self,text):
        #Using google text to speech the text is coverted to speech
        tts = gTTS(text=text, lang='en')
        filename = 'audio.mp3'
        tts.save(filename)
        playsound(filename)
        

    def pointing(self):
        # Right shoulder and elbow angles are changed using setAngles function to make the Pepper robot wave with the right hand
        behavior_realizer_class.pepper.setAngles("RShoulderPitch", -1.5708, 0.7)  # -90 degrees
        time.sleep(1.5)
        behavior_realizer_class.pepper.setAngles("RElbowRoll", 0.349066, 0.4)  # 20 degrees
        time.sleep(1.5)
        behavior_realizer_class.pepper.setAngles("RElbowRoll", -0.349066, 0.4)  # -20 degrees
        behavior_realizer_class.pepper.setAngles("RShoulderRoll", -0.436332, 0.6)  # -30 degrees (adjust as needed)
        time.sleep(1.0)
        behavior_realizer_class.pepper.setAngles("RShoulderRoll", 0.436332, 0.6)  # 30 degrees (adjust as needed)
        # 2nd wave
        behavior_realizer_class.pepper.setAngles("RElbowRoll", 0.349066, 0.4)  # 20 degrees
        time.sleep(1.5)
        behavior_realizer_class.pepper.setAngles("RElbowRoll", -0.349066, 0.4)  # -20 degrees
        behavior_realizer_class.pepper.setAngles("RShoulderRoll", -0.436332, 0.6)  # -30 degrees (adjust as needed)
        time.sleep(1.0)
        behavior_realizer_class.pepper.setAngles("RShoulderRoll", 0.436332, 0.6)  # 30 degrees (adjust as needed)
        time.sleep(1.0)
        # To bring the arm down
        behavior_realizer_class.pepper.setAngles("RShoulderPitch", 1.5708, 0.6)  # 90 degrees

    def NOD(self):
        behavior_realizer_class.pepper.setAngles("HeadPitch", -0.3, 0.6) 
        time.sleep(1.0)
        behavior_realizer_class.pepper.setAngles("HeadPitch", 0.3, 0.6)
        time.sleep(1.0)
        behavior_realizer_class.pepper.setAngles("HeadPitch", 0.0, 0.6)

    def speech(self, text):
        
            tts = gTTS(text='HELLO', lang='en')
            filename = 'audio.mp3'
            tts.save(filename)
            playsound(filename)

    def gaze(self):
        behavior_realizer_class.pepper.setAngles("HeadPitch", 0.0, 0.6)

    def posture(self):
       behavior_realizer_class.pepper.setAngles("LShoulderPitch",-1.5708,0.7) #-90 degree
       behavior_realizer_class.pepper.setAngles("RShoulderPitch",-1.5708,0.7) #-90 degree
       behavior_realizer_class.pepper.moveTo(0,0,6,1,0.9)
       behavior_realizer_class.pepper.setAngles("LShoulderPitch",1.5708,0.7) #90 degree
       behavior_realizer_class.pepper.setAngles("RShoulderPitch",1.5708,0.7) #90 degree

    def raiseBothHands(self):
        # Set angles to raise both hands (adjust as needed)
        self.pepper.setAngles("LShoulderPitch", 1.0, 0.6)
        self.pepper.setAngles("RShoulderPitch", 1.0, 0.6)
        self.pepper.setAngles("LElbowYaw", 1.0, 0.6)
        self.pepper.setAngles("RElbowYaw", -1.0, 0.6)

    def raiseOneHand(self):
        # Raise one hand in a confused manner (adjust as needed)
        self.pepper.setAngles("LShoulderPitch", 0.5, 0.5)  # Adjust angles as needed
        self.pepper.setAngles("LElbowYaw", -0.5, 0.5)  # Adjust angles as needed
        self.pepper.setAngles("LElbowRoll", 0.5, 0.5)  # Adjust angles as needed

    def WhatHand(self):
        # Adjust joint angles to raise the right hand in a confused manner
        self.pepper.setAngles("RShoulderPitch", 0.5, 0.6)  # Adjust the angle as needed
        self.pepper.setAngles("RElbowYaw", -0.5, 0.6)  # Adjust the angle as needed
        self.pepper.setAngles("RElbowRoll", -0.5, 0.6) 

    # def custom_thread_function(duration):
         
    #      start_time = time.time()
    # end_time = start_time + duration

    # while time.time() < end_time:
        
    #     print("Thread is running...")

    # def BML(self):


        # if self.value == data['bml']:
        #     behavior_realizer_class.wave_pepper()
        #     print(self.value)
        # if "gaze" == bml_data["bml"]["gaze"]:
        #     behavior_realizer_class.wave_pepper()

        # if "gaze" in bml_data:
        #     behavior_realizer_class.NOD()

        # if "pointing" in bml_data:
        #     pointing_data = bml_data["pointing"]

        # if "speech" in bml_data:
        #     speech_data = bml_data["speech"]
        #     for speech_item in speech_data:
        #         text = speech_item["text"]

        # if "head" in bml_data:
        #     head_data = bml_data["head"]

        # if "posture" in bml_data:
        #     posture_data = bml_data["posture"]





        


if __name__ == "__main__":

    

    behavior_realizer_class = BehaviorRealizer()  
    #TODO: Implement necessary code for robot behaviours 

    with open("bml.xml") as xml_file:
     
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            
            with open("data.json", "w") as json_file:
                json_file.write(json_data)

            with open("data.json", "r") as json_file:
                bml_data = json.load(json_file)
                print(json.dumps(bml_data, indent=4))


                gaze_data = bml_data["bml"]["gaze"]
                pointing_data = bml_data["bml"]["pointing"]
                speech_data = bml_data["bml"]["speech"]
                head_data = bml_data["bml"]["head"]
                posture_data = bml_data["bml"]["posture"]

                # Create and start threads for each BML action
                gaze_thread = threading.Thread(target=behavior_realizer_class.gaze)
                pointing_thread = threading.Thread(target=behavior_realizer_class.pointing)
                speech_thread = threading.Thread(target=behavior_realizer_class.speech, args=('Hello!'))
                speech_thread2 = threading.Thread(target=behavior_realizer_class.speech, args=('Glad to meet you!'))
                
                head_thread = threading.Thread(target=behavior_realizer_class.NOD)
                posture_thread = threading.Thread(target=behavior_realizer_class.posture)

                gaze_thread.start()
                time.sleep(2)
                pointing_thread.start()
                speech_thread.start()
                
                

                # Wait for all threads to finish
                gaze_thread.join()
                head_thread.start()
                pointing_thread.join()
                speech_thread2.start()
                speech_thread2.join()
      
                head_thread.join()
                posture_thread.start()
                posture_thread.join()          



    #The code bellow is used to change the angles of pepers hand so that it could bring both its hand parralel to it body
    behavior_realizer_class.pepper.setAngles("LShoulderPitch",1.5708,0.6) #the joint used if the left shoulder, the angle is given in radians and the speed is 0.6
    behavior_realizer_class.pepper.setAngles("RShoulderPitch",1.5708,0.6)

        
    INPUT_OPTIONS=["done","speak","wave","BML"]
     
    repeat_ = True
    while repeat_:

        #based on the user's input the speak or wave or close application is executed
        print("Type BML/speak/wave/done")

        user_input = input("INPUT : ")

        if str(user_input)==INPUT_OPTIONS[1]:
            text_val=input("Enter the text here: ")
            behavior_realizer_class.speak_peper(text_val)
        
        if str(user_input)==INPUT_OPTIONS[3]:
            # text = "Hello!"
            # text1 = "Glad to meet you!"
            behavior_realizer_class.BML()
        
        if str(user_input)==INPUT_OPTIONS[2]:
            behavior_realizer_class.wave_pepper()

        if str(user_input)==INPUT_OPTIONS[0]:
            repeat_=False

        if not user_input in INPUT_OPTIONS:
            print("Please enter 'done' to exit.")