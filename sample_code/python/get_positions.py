import argparse
from manuel1 import RobotConfig, originPositions
import json
from pathlib import Path
from time import sleep

arg_parser = argparse.ArgumentParser("Get robot positions")
arg_parser.add_argument("-du", "--delay_to_unfreeze", type=float, default=0)
arg_parser.add_argument("-dr", "--delay_to_record", type=float, default=0)
arg_parser.add_argument("-f", "--freeze", nargs="?", type=bool, default=False, const=True)
arg_parser.add_argument("-s", "--save", nargs="?", type=bool, default=False, const=True)
args = arg_parser.parse_args()

def arr_diff(arr1, arr2):
    return [i-j for (i,j) in zip(arr1, arr2)]

robot_config = RobotConfig(motor_ids=[2, 3, 4, 5, 6, 7, 8])

if args.delay_to_unfreeze > 0:
    print(f"Waiting {args.delay_to_unfreeze} seconds before unfreezing...")
    sleep(args.delay_to_unfreeze)
    robot_config.enable_torque(False)

if args.delay_to_record > 0:
    print(f"Waiting {args.delay_to_record} seconds before recording...")
    sleep(args.delay_to_record)

if args.freeze:
    robot_config.enable_torque(True)
    print("The robot has been frozen.")

absolute_pos = robot_config.get_positions()
relative_pos = arr_diff(absolute_pos, originPositions)

print("Relative position:", relative_pos)
print("Absolute position:", absolute_pos)

if args.save:
    scriptDirectory = Path(__file__).resolve().parent
    configFileName = scriptDirectory/"config.json"
    with open(configFileName, "r") as configReadFile:
        config = json.load(configReadFile)
    config['origin_positions'] = absolute_pos
    with open(configFileName, "w") as configWriteFile:
        json.dump(config, configWriteFile, indent=4)