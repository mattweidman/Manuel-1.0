# Common APIs to use in different control scripts for Manuel 1.0

import dynamixel_sdk
from time import sleep

# portHandler = dynamixel_sdk.PortHandler('COM6') # Windows
portHandler = dynamixel_sdk.PortHandler('/dev/tty.usbserial-FT9MIQU2') # Mac
packetHandler = dynamixel_sdk.PacketHandler(2.0)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

# Set port baudrate
if portHandler.setBaudRate(57600):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Throw an exception if a message failed in some way.
def handle_results(motor_id: int, address: int, comm_result: int, error):
    if comm_result == dynamixel_sdk.COMM_SUCCESS and error == 0:
        return

    details = f'''
Motor ID: {motor_id}
Address: {address}
Result = {comm_result}
Error = {error}
'''
    
    raise Exception("Message to motor failed. Details:" + details)

# Enable torque for a motor.
def enable_torque(motor_id: int, enable: bool = True):
    address = 64

    comm_result, error = packetHandler.write1ByteTxRx(
        portHandler,
        motor_id,
        address,
        data=1 if enable else 0)

    handle_results(motor_id, address, comm_result, error)
    print(f"Successfully {'enabled' if enable else 'disabled'} torque for motor {motor_id}.")

def is_torque_enabled(motor_id: int):
    '''Get whether torque is enabled for a motor.'''
    address = 64

    enabled, comm_result, error = packetHandler.read1ByteTxRx(
        portHandler,
        motor_id,
        address)
    
    handle_results(motor_id, address, comm_result, error)
    return False if enabled == 0 else True

def set_operating_mode(motor_id: int, mode: int):
    '''Set the operating mode for a motor.

    Modes:
    * 1: velocity control mode
    * 3: position control mode (default)
    * 4: extended position control mode
    * 16: PWM control mode
    '''
    address = 11

    comm_result, error = packetHandler.write1ByteTxRx(
        portHandler,
        motor_id,
        address,
        data=mode)

    handle_results(motor_id, address, comm_result, error)
    print(f"Set operating mode of motor {motor_id} to {mode}.")

def get_operating_mode(motor_id: int):
    '''Get the operating mode for a motor.

    Modes:
    * 1: velocity control mode
    * 3: position control mode (default)
    * 4: extended position control mode
    * 16: PWM control mode
    '''
    address = 11

    mode, comm_result, error = packetHandler.read1ByteTxRx(
        portHandler,
        motor_id,
        address)
    
    handle_results(motor_id, address, comm_result, error)
    return mode

# Read position of a motor.
def read_position(motor_id: int) -> int:
    address = 132

    position, comm_result, error = packetHandler.read4ByteTxRx(
        portHandler,
        motor_id,
        address)
    
    # Ensure that the upper half of integers are represented as negative
    if (position >= 2**31):
        position = position - 2**32
    
    handle_results(motor_id, address, comm_result, error)
    print(f"Position of motor {motor_id}: {position}")
    return position

# Write position of a motor.
def write_position(motor_id: int, target_position: int):
    address = 116

    comm_result, error = packetHandler.write4ByteTxRx(
        portHandler,
        motor_id,
        address,
        data=target_position)
    
    handle_results(motor_id, address, comm_result, error)
    print(f"Set goal position of motor {motor_id} to {target_position}.")

def read_pwm(motor_id: int):
    address = 124

    pwm, comm_result, error = packetHandler.read2ByteTxRx(
        portHandler,
        motor_id,
        address)
    
    # Ensure that the upper half of integers are represented as negative
    if (pwm >= 2**15):
        pwm = pwm - 2**16
    
    handle_results(motor_id, address, comm_result, error)
    print(f"PWM of motor {motor_id}: {pwm}")
    return pwm

def write_pwm(motor_id: int, target_pwm: int):
    '''Write PWM (torque) for a motor.'''
    address = 100

    comm_result, error = packetHandler.write2ByteTxRx(
        portHandler,
        motor_id,
        address,
        data=target_pwm)
    
    handle_results(motor_id, address, comm_result, error)
    print(f"Set goal PWM of motor {motor_id} to {target_pwm}.")

def set_velocity(motor_id: int, velocity: int):
    '''
    Setting this to 0 will choose the maximum velocity. The max value
    is 32,767, in units of 0.229 rev/min.
    '''
    address = 112

    comm_result, error = packetHandler.write4ByteTxRx(
        portHandler,
        motor_id,
        address,
        data=velocity)
    
    handle_results(motor_id, address, comm_result, error)
    print(f"Set the velocity of {motor_id} to {velocity}.")

def set_acceleration(motor_id: int, acceleration: int):
    '''
    Setting this to 0 will choose the maximum acceleration. The max value
    is 32,737, in units of 214.577 rev/min^2.
    '''
    address = 108

    comm_result, error = packetHandler.write4ByteTxRx(
        portHandler,
        motor_id,
        address,
        data=acceleration)
    
    handle_results(motor_id, address, comm_result, error)
    print(f"Set the acceleration of {motor_id} to {acceleration}.")

POSITION_CLOSENESS_THRESHOLD = 5
TICK_SECONDS = 0.01

class RobotConfig:
    '''Defines a set of motors and operations that work on all of them at once.'''

    def __init__(self, motor_ids: list[int]):
        '''
        motor_ids: IDs of each motor
        '''
        self.motor_ids = motor_ids
    
    def get_positions(self):
        '''Return the positions of all motors in the order they were provided
        in the constructor.'''
        return [read_position(motor_id) for motor_id in self.motor_ids]
    
    def set_velocities(self, velocities):
        '''Set the maximum velocity of all motors to values in a list.'''
        for motor_id, velocity in zip(self.motor_ids, velocities):
            set_velocity(motor_id, velocity)
    
    def set_accelerations(self, accelerations):
        '''Set the maximum acceleration of all motors to values in a list.'''
        for motor_id, acceleration in zip(self.motor_ids, accelerations):
            set_acceleration(motor_id, acceleration)
    
    def enable_torque(self, enable: bool):
        '''Enable or disable torque for all motors.'''
        for motor_id in self.motor_ids:
            enable_torque(motor_id, enable)
    
    def set_operating_mode(self, motor_index: int, mode: int):
        '''Set a motor operating mode.

        Modes:
        * 1: velocity control mode
        * 3: position control mode (default)
        * 4: extended position control mode
        * 16: PWM control mode
        '''
        motor_id = self.motor_ids[motor_index]

        # No need to do anything if already in the desired mode
        previous_operating_mode = get_operating_mode(motor_id)
        if previous_operating_mode == mode:
            return

        # Torque must be disabled to set the operating mode
        torque_enabled_previously = is_torque_enabled(motor_id)
        if torque_enabled_previously:
            enable_torque(motor_id, enable=False)
        
        set_operating_mode(motor_id, mode)

        # Re-enable torque if it was enabled previously
        if torque_enabled_previously:
            enable_torque(motor_id, enable=True)
    
    def set_operating_mode_to_pwm(self, motor_index: int):
        self.set_operating_mode(motor_index, mode=16)
    
    def set_operating_mode_to_extended_position(self, motor_index: int):
        self.set_operating_mode(motor_index, mode=4)
    
    def set_all_operating_modes(self, mode: int):
        '''Set the operating mode to all motors.

        Modes:
        * 1: velocity control mode
        * 3: position control mode (default)
        * 4: extended position control mode
        * 16: PWM control mode
        '''
        for motor_index in range(len(self.motor_ids)):
            self.set_operating_mode(motor_index, mode)
    
    def set_all_operating_modes_to_extended_position(self):
        self.set_all_operating_modes(mode=4)
    
    def write_positions(self, target_positions: list[int]):
        '''Write positions of all motors in the order that they came in the constructor.'''
        for motor_id, position in zip(self.motor_ids, target_positions):
            write_position(motor_id, position)
    
    def reached_target_positions(self, target_positions: list[int]):
        '''Returns true if all motors have reached their target positions within
        the threshold.'''
        for motor_id, target_position in zip(self.motor_ids, target_positions):
            current_position = read_position(motor_id)
            # Return false if any motor has moved significantly since the last tick
            if abs(current_position - target_position) > POSITION_CLOSENESS_THRESHOLD:
                return False
        return True

    def write_one_position_and_wait(self, motor_index: int, target_position: int):
        '''Write the position of one motor and wait for it to settle.'''
        motor_id = self.motor_ids[motor_index]
        write_position(motor_id, target_position)
        last_position = read_position(motor_id)
        while True:
            sleep(TICK_SECONDS)
            position = read_position(motor_id)
            if (last_position is not None and
                abs(position - last_position) < POSITION_CLOSENESS_THRESHOLD):
                return
            last_position = position

    def write_positions_and_wait(self, target_positions: list[int]):
        '''Write positions to all motors and wait for them to settle.'''
        self.write_positions(target_positions)

        last_positions = self.get_positions()
        while True:
            sleep(TICK_SECONDS)
            current_positions = self.get_positions()

            # Stop iterating when all motors have stopped moving significantly
            all_stable = True
            for current_pos, last_pos in zip(current_positions, last_positions):
                if abs(current_pos - last_pos) > POSITION_CLOSENESS_THRESHOLD:
                    all_stable = False
                    break
            if all_stable:
                return

            last_positions = current_positions
    
    def write_pwm(self, motor_index: int, target_pwm: int):
        '''Write PWM for one motor.'''
        write_pwm(self.motor_ids[motor_index], target_pwm)

def arr_sum(arr1, arr2):
    return [i+j for (i,j) in zip(arr1, arr2)]