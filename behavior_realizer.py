import math
import xml.etree.ElementTree as ET
import time
import threading
import os
from playsound import playsound
from gtts import gTTS
from abc import ABC

from qibullet import SimulationManager

class BML(ABC):
    @classmethod
    def pointing(self):
        print("not implemented")


class Pepper:
    def __init__(self):
        simulation_manager = SimulationManager()
        client = simulation_manager.launchSimulation(gui=True)
        self.robot = simulation_manager.spawnPepper(client, spawn_ground_plane=True)
        self.rest()

    def rest(self, **kwargs):
        self.robot.setAngles("RShoulderPitch", 1.5708, 0.6)
        self.robot.setAngles("LShoulderPitch", 1.5708, 0.6)
        
    def NOD(self):
        self.robot.setAngles("HeadPitch", -0.3, 0.6) 
        time.sleep(1.0)
        self.robot.setAngles("HeadPitch", 0.3, 0.6)
        time.sleep(1.0)
        self.robot.setAngles("HeadPitch", 0.0, 0.6)

    def wave(self, **kwargs):
        # Right shoulder and elbow angles are changed using setAngles function to make the Pepper robot wave with the right hand
        self.robot.setAngles("RShoulderPitch", -1.5708, 0.7)  # -90 degrees
        time.sleep(0.5)
        self.robot.setAngles("RElbowRoll", 0.349066, 0.4)  # 20 degrees
        time.sleep(0.5)
        self.robot.setAngles("RElbowRoll", -0.349066, 0.4)  # -20 degrees
        self.robot.setAngles("RShoulderRoll", -0.436332, 0.6)  # -30 degrees (adjust as needed)
        time.sleep(0.5)
        self.robot.setAngles("RShoulderRoll", 0.436332, 0.6)  # 30 degrees (adjust as needed)
        # 2nd wave
        self.robot.setAngles("RElbowRoll", 0.349066, 0.4)  # 20 degrees
        time.sleep(0.5)
        self.robot.setAngles("RElbowRoll", -0.349066, 0.4)  # -20 degrees
        self.robot.setAngles("RShoulderRoll", -0.436332, 0.6)  # -30 degrees (adjust as needed)
        time.sleep(0.5)
        self.robot.setAngles("RShoulderRoll", 0.436332, 0.6)  # 30 degrees (adjust as needed)
        time.sleep(0.5)
        # To bring the arm down
        self.robot.setAngles("RShoulderPitch", 1.5708, 0.6)  # 90 degrees


    def raise_both_hands(self, **kwargs):
        # Set angles to raise both hands (adjust as needed)
        self.robot.setAngles("LShoulderPitch", math.radians(0), 0.6)
        self.robot.setAngles("RShoulderPitch", math.radians(0), 0.6)
        self.robot.setAngles("LElbowYaw", math.radians(-180), 0.6)
        self.robot.setAngles("RElbowYaw", math.radians(180), 0.6)
        self.robot.setAngles("LElbowRoll", math.radians(-45), 0.6)
        self.robot.setAngles("RElbowRoll", math.radians(45), 0.6)

    def raise_one_hand(self, **kwargs):
        # Raise one hand in a confused manner (adjust as needed)
        self.robot.setAngles("LShoulderPitch", math.radians(0), 0.6)  # Adjust angles as needed
        self.robot.setAngles("LElbowYaw", math.radians(-180), 0.6)  # Adjust angles as needed
        self.robot.setAngles("LElbowRoll", math.radians(-35), 0.6)  # Adjust angles as needed

    def nod(self, **kwargs):
        self.robot.setAngles("HeadPitch", -0.3, 0.6)
        time.sleep(0.3)
        self.robot.setAngles("HeadPitch", 0.3, 0.6)
        time.sleep(0.3)
        self.robot.setAngles("HeadPitch", 0.0, 0.6)

    def speech(self, text):
        tts = gTTS(text=text, lang='en')
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(current_dir, 'Soundpepper', 'audio.mp3')
        tts.save(filename)
        playsound(filename)


    def wait(self, **kwargs):
        print("running wait")
        for k, v in kwargs.items():
            if k == "duration":
                time.sleep(v)
            print(f"I got  {k} with value {v}")

    # def speech(self, **kwargs):
    #      print("running speech")
    #       for k,v in kwargs.items():
    #           print(f"I got  {k} with value {v}")

if __name__ == "__main__":
    pepper = Pepper()
    tree = ET.parse("behavior.bml")

    root = tree.getroot()

    # for child in root:
    #     func = getattr(pepper, child.tag)
    #     func(**child.attrib)

    #pepper.wait()
    pepper.nod(id="this-is-id")
    pepper.speech(text="Glad to meet you!")
    pepper.wave()
    pepper.rest()

    while True:
        user_input = input("INPUT : ")
        if user_input == "done":
            break
        if user_input == "rest":
            pepper.rest()



    """
    <bml characterId="Alice" 
        id="bml1">
    <speech id="behavior1" start="0">            
        <text>
        Good morning.
        </text>
    </speech>
    <wait id="behavior2" start="behavior1:end" duration="1"/>
    <speech id="behavior3" start="behavior2:end" end="">            
        <text>
        Goodbye.
        </text>
    </speech>

</bml>
    """
