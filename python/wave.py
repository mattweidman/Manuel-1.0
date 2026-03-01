from manuel1 import RobotConfig, originPositions

regular_velocities = [100, 150, 50, 100, 100, 100, 100]
waving_velocities = [150] * 7
regular_accelerations = [10] * 7
waving_accelerations = [20] * 7

robot_config = RobotConfig(motor_ids=[2, 3, 4, 5, 6, 7, 8])
robot_config.set_all_operating_modes_to_extended_position()
robot_config.set_velocities(regular_velocities)
robot_config.set_accelerations(regular_accelerations)
robot_config.enable_torque(True)

def arr_sum(arr1, arr2):
    return [x + y for x, y in zip(arr1, arr2)]

def move_to_relative_position(arr):
    pos = arr_sum(originPositions, arr)
    robot_config.write_positions_and_wait(pos)

wave_start = [-2115, 1742, 732, 800, -896, -1162]
wave_end = [-2115, 1742, 732, 1800, -896, -1162]

move_to_relative_position(wave_start)

robot_config.set_velocities(waving_velocities)
robot_config.set_accelerations(waving_accelerations)

move_to_relative_position(wave_end)
move_to_relative_position(wave_start)
move_to_relative_position(wave_end)
move_to_relative_position(wave_start)

robot_config.set_velocities(regular_velocities)
robot_config.set_accelerations(regular_accelerations)

move_to_relative_position([0, 0, 0, 0, 0, 0, 0])

robot_config.enable_torque(False)