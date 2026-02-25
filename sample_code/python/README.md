# Sample Python code

This directory contains sample code you can use to control the Manuel 1.0 robot
arm.

Files:
* manuel1.py: Common functions and classes for use in the samples
* get_positions.py: Script that retrieves all joint positions from the robot,
including the ability to freeze or unfreeze the arm on a timer
* wave.py: Robot arm waves its gripper like in a greeting
* config.json: Contains saveable values, including the USB port, baud rate, and
origin joint position

## Setup

1. Make sure you have dynamixel_sdk installed: `pip install dynamixel-sdk`
2. Connect the U2D2 USB converter module to the robot, to a power outlet, and
to your computer. Flip the switch on.
3. In `config.json`, set `usb_port` to the name of the USB port that the U2D2
module is connected to.
4. Make sure no other applications on your computer are connected to the robot.
If the Dynamixel Wizard is connected, either click the disconnect button or
close the program.
5. Move the robot into resting position, where the wrist lies flat on the
shoulder. This will be your "origin position", which all other positions
will be relative to.
6. Save the origin position in `config.json` with
`python3 sample_code/python/get_positions.py -s`