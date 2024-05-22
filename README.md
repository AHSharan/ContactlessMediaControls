# ContactlessMediaControls
This script controls media playback and volume using infrared (IR) sensors connected to an Arduino board. It uses the PyFirmata library to interact with the Arduino and PyAutoGUI to simulate key presses on the computer

# IR Sensor Media Control

This project uses infrared (IR) sensors connected to an Arduino to control media playback and volume on a computer. It interacts with the Arduino using the PyFirmata library and simulates key presses with PyAutoGUI.

## Setup

1. **Hardware:**
   - Connect three IR sensors to the Arduino's digital pins 9, 10, and 11.
   - Ensure the Arduino is connected to the correct COM port (adjust `COM5` in the script if necessary).

2. **Dependencies:**
   - `pyfirmata`: To communicate with the Arduino board.
   - `pyautogui`: To simulate keyboard actions.
   - `time`: To handle sleep functions (built-in).

   Install the necessary packages using pip:

   pip install pyfirmata pyautogui
