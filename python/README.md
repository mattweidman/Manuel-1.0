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
`python3 "python/get_positions.py -s`
7. You're ready to start developing. For an example, try out the code in
`wave.py` with `python3 "python/wave.py`. Make sure the robot has a clear space
around it before running.

## get_positions.py

`get_positions.py` is a useful script you can use to get the joint positions.
You can set a timer to give you time to manually move it into a certain
position before the joint positions are recorded. You can also use it to
freeze or unfreeze all joints on a timer.

### Parameters

#### --delay_to_unfreeze

If the robot is currently frozen (torque enabled in all joints), the robot will
unfreeze (disable all of its joints) after the specified number of seconds.
This is useful if you want to disable the robot, and you want to give yourself
time to grab it to keep it from falling.

Syntax:

`python3 "python/get_positions.py -delay_to_unfreeze <float>`

`python3 "python/get_positions.py -du <float>`

Example:

`"python/get_positions.py -du 4.5`

#### --delay_to_record

Positions will not be recorded until the specified number of seconds have
lapsed. This time begins after the time in `--delay_to_unfreeze` completes.
This is useful if you want to record the position of a robot in a particular
position, but you need time to get move from your computer to the robot before
you manually manipulate it. Sort of like setting a timer on your camera.

Syntax:

`python3 "python/get_positions.py --delay_to_record <float>`

`python3 "python/get_positions.py -dr <float>`

Example:

`"python/get_positions.py -dr 4.5`

#### --freeze

Whether the robot should freeze when it records. You might want to do this if
you want to let go of the robot after recording its position, but you don't
want it to fall yet.

Syntax:

`python3 "python/get_positions.py --freeze`

`python3 "python/get_positions.py -f`

#### --save

When this flag is used, the robot will save its position in the
`origin_positions` JSON property of `config.json`.

Syntax:

`python3 "python/get_positions.py --save`

`python3 "python/get_positions.py -s`