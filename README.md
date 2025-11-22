# Manuel 1.0: Open-source robotic arm

This is an open-source robotic arm I made as a hobby project. It's flexible,
easy to connect to a computer, and relatively inexpensive. Besides a 3D
printer, no expensive tools (>$50) are required to build it. Feel free to build
and use this robot however you like, as long as it's safe.

* This arm is made entirely with 3D-printed components and mass-produced
parts you can find online. If you have a 3D printer, some cheap hobby tools,
and enough budget for parts, you can build it.
* As of 2025, the parts cost about $2300, substantially cheaper than all
commercial robotic arms (that I know of) with similar size and torque
capabilities.
* It has 7 motors: 6 degrees of freedom + a gripper.
* 4 out of 6 joints (waist + 3 wrist joints) can turn more than 360 degrees.
* Wrist joints allow the gripper to rotate completely in all 3 axes when
unobstructed. The gripper can point forward, backward, up, down, left, or right
only by moving the wrist.
* The arm as I designed it reaches 860 mm from shoulder to gripper tip. That's
similar in length to a human arm. You can change the length by using shorter or
longer T-slot extrusions (mine are 300 mm each). A shorter arm will vibrate
less or be able to lift more.
* This arm was designed to lift 1 kg with the length I used.
* All motors are from the [Dynamixel X](https://www.robotis.us/x-series/)
series from Robotis. Robotis has excellent documentation and code resources,
so it is fairly straightforward to control the joints with any of their
[SDKs](https://github.com/ROBOTIS-GIT/DynamixelSDK) written in various
languages. Linux, Windows, and Mac are all supported, and you can connect the
robot to a computer with USB.
* All 3D-printed components can be printed with standard PLA filament. On my
Bambu Lab A1, I don't need supports for any of the components.
* All components can be removed and replaced. No glue is used anywhere. Most
plastic components are connected with M3 screws and heat set inserts.
* Wires are well organized. If you follow the recommended wire lengths, you
shouldn't have any annoying dangling wires. Of course you will have to adjust
the wire lengths if you choose differently-lengthed extrusions.

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

## Bill of materials

TODO

## Tools needed

* 3D printer that can print PLA
* Soldering iron
* Crimping tool
* Wire strippers
* Lighter or some kind of heat source for heating heat shrinks
* Pliers
* Phillips screwdriver (what size?)
* (Optional) Hex drivers (what size?)

## Wire lengths

TODO