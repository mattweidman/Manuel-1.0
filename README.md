# Manuel 1.0: Open-source robotic arm

This is an open-source robotic arm I made as a hobby project. It's flexible,
similar in size to a human arm, and relatively inexpensive. Besides a 3D
printer, no expensive tools (>$50) are required to build it. Feel free to build
and use this robot however you like, as long as it's safe. I sincerely hope
that someone besides me can find some use or enjoyment out of this project.

Features:
* This arm is made entirely with 3D-printed components and mass-produced
parts you can find online. If you have a 3D printer, some cheap hobby tools,
and money for parts, you can build it.
* As of 2025, the parts cost about $2300, substantially cheaper than all
commercial robotic arms (that I know of) with similar size and torque
capabilities.
* There are 7 motors: 6 degrees of freedom + a gripper.
* 4 out of 6 joints (waist + 3 wrist joints) can turn more than 360 degrees.
* Wrist joints allow the gripper to rotate completely in all 3 axes when
unobstructed. The gripper can point forward, backward, up, down, left, right,
and anywhere inbetween only by moving the wrist.
* The arm as I designed it reaches 860 mm from shoulder to gripper tip. That's
similar in length to a human arm. You can change the length by using shorter or
longer T-slot extrusions (mine are 300 mm each). A shorter arm will vibrate
less or be able to lift more.
* This arm was designed to lift a payload of 1 kg with the length I used.
* All motors are from the [Dynamixel X](https://www.robotis.us/x-series/)
series from Robotis. Robotis has excellent documentation and code resources,
so it is fairly straightforward to control the joints with any of their
[SDKs](https://github.com/ROBOTIS-GIT/DynamixelSDK) written in Python, C++,
Java, C#, and more. Linux, Windows, and Mac are all supported, and you can
connect the robot to a computer with USB.
* All 3D-printed components can be printed with standard PLA filament. For many
3D printers such as my Bambu Lab A1, no supports are needed.
* All components can be removed and replaced. No glue is used anywhere. Most
plastic components are connected with M3 screws and heat set inserts.
* Wires are well organized. If you follow the recommended wire lengths, you
shouldn't have any annoying dangling wires. Of course you will have to adjust
the wire lengths if you choose extrusions that are not 300 mm.

## Tips

* I recommend putting a maximum acceleration of "10" on all motors using the
[profile acceleration](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/#profile-acceleration)
setting. Acceleration that is too high will cause joints to vibrate, and you
won't get good accuracy. You can later adjust this as you see fit.
* I use 0.2mm Standard 3D printer settings for all parts except for the gears.
For the gears, I increase the wall loops to 4 to try to fill all of the teeth
completely.
* Some of the printed components have a small overhang inside the screw hole
where the screw meets the plastic. My printer can do some overhangs, but often
it leaves plastic threads sticking around, and the hole is often too small. You
can fix this by taking a small allen wrench and forcing it through the hole.
Then take a bigger one and do it again. Eventually you'll be able to fit the
screw in there.

## Tools needed

* Any computer with a USB port
* 3D printer that can print PLA; bed size should be at least 17 cm x 17 cm
* Soldering iron
* Crimping tool that can crimp
[JST SEH-001T-P0.6](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/#connector-information)
* Wire stripper
* Lighter or some kind of heat source for heating heat shrinks
* 2mm Phillips screwdriver
* Hex drivers / allen wrenches, sizes 1.5mm, 2.0mm, 2.5mm, and 4mm
* Pliers
* Flathead screwdriver
* Table clamps

## Bill of materials

TODO

## Wire lengths

Here is a list of all electronics and the lengths of wires between them, from
base to tip. Every wire is written of the form "{F/M}-{#}-{F/M}", where "{F/M}"
indicates whether the connector on one end is female (F) or male (M), and "{#}"
indicates the wire length in cm. Note that many Dynamixel motors come with an
18 cm female-female wire included, so if you see "F-18-F" in the list, you
don't need to make it yourself.

All F/M connectors are
[3-pin JST EH connectors](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/#connector-information).

1. [U2D2](https://emanual.robotis.com/docs/en/parts/interface/u2d2/) USB
connector
1. F-18-F
1. M-13-F
1. [XM430-W350-T](https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/)
(waist)
1. F-22-F
1. [XM540-W270-T](https://emanual.robotis.com/docs/en/dxl/x/xm540-w270/)
(shoulder)
1. F-40-F (change length if you used a different extrusion length)
1. M-17-F
1. [XM540-W270-T](https://emanual.robotis.com/docs/en/dxl/x/xm540-w270/)
(elbow)
1. F-32-M
1. F-18-F (change length if you used a different extrusion length)
1. [XM430-W350-T](https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/)
(wrist 1)
1. F-18-F
1. [XM430-W350-T](https://emanual.robotis.com/docs/en/dxl/x/xm430-w350/)
(wrist 2)
1. F-21-F
1. [XL430-W350-T](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/)
(wrist 3)
1. F-15-F
1. [XL430-W350-T](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/)
(gripper)