"""
This script controls media playback and volume using infrared (IR) sensors connected to an Arduino board.
It uses the PyFirmata library to interact with the Arduino and PyAutoGUI to simulate key presses on the computer.

Setup:
- Connect three IR sensors to the digital pins 9, 10, and 11 on the Arduino.
- Ensure the Arduino is connected to the correct COM port.

Functionality:
- IR sensor 1 (connected to pin 9) controls play/pause (space key).
- IR sensor 2 (connected to pin 10) controls volume up.
- IR sensor 3 (connected to pin 11) controls volume down.

Dependencies:
- pyfirmata: To communicate with the Arduino board.
- pyautogui: To simulate keyboard actions.
- time: To handle sleep functions.
"""

from pyfirmata import Arduino, util       
from time import sleep, time
import pyautogui

try:
    board = Arduino('COM5')
    print("Connected to Arduino successfully!")
except Exception:
    print("Error: Could not connect to Arduino. Check port or connection.")
    exit()
                                                                        
         
# Start an iterator thread to prevent buffer overflow
it = util.Iterator(board)
it.start()

ir1 = board.get_pin('d:9:i')
ir2 = board.get_pin('d:10:i')
ir3 = board.get_pin('d:11:i')
VOLUME_REPEAT=4
IR1_FUNCTION = "space"
IR2_FUNCTION = "volumeup"
IR3_FUNCTION = "volumedown"

while True:
    
    print(f"IR 1:{ir1.read()} IR 2:{ir2.read()} IR 3:{ir3.read()}")
    sleep(0.4)

    if ir1.read() == False:
        pyautogui.press(IR1_FUNCTION)     
        sleep(.6)

    elif ir2.read() == False:
        while ir2.read() == False:
            for _ in range(VOLUME_REPEAT):
                pyautogui.press(IR2_FUNCTION) 
    
    elif ir3.read() == False:
        while ir3.read() == False:
            for _ in range(VOLUME_REPEAT):
                pyautogui.press(IR3_FUNCTION) 
