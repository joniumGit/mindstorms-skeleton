from typing import Literal, Tuple, Optional, Union

_GESTURE = Literal['shaken', 'tapped', 'doubletapped', 'falling']
_COLOR = Optional[Literal['black', 'blue', 'cyan', 'green', 'red', 'violet', 'white', 'yellow']]
_PORT = Literal['A', 'B', 'C', 'D', 'E', 'F']
_DISTANCE = Literal['cm', 'in', '%']
_PERCENT = Literal[
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

_STATUS_COLOR = Literal['azure', 'black', 'blue', 'cyan', 'green', 'orange', 'red', 'violet', 'white', 'yellow']
_MIDI_NOTE = Literal[
    44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123
]
_ORIENTATION = Literal['back', 'down', 'up', 'front', 'leftside', 'rightside']
_PIXEL_POS = Literal[0, 1, 2, 3, 4]

_POWER = Union[
    Literal[
        -0, -1, 2, - 3, -4, -5, -6, -7, -8, -9, -10,
        -11, - 12, -13, -14, -15, -16, -17, -18, -19, -20,
        -21, - 22, -23, -24, -25, -26, -27, -28, -29, -30,
        -31, - 32, -33, -34, -35, -36, -37, -38, -39, -40,
        -41, - 42, -43, -44, -45, -46, -47, -48, -49, -50,
        -51, - 52, -53, -54, -55, -56, -57, -58, -59, -60,
        -61, - 62, -63, -64, -65, -66, -67, -68, -69, -70,
        -71, - 72, -73, -74, -75, -76, -77, -78, -79, -80,
        -81, - 82, -83, -84, -85, -86, -87, -88, -89, -90,
        -91, - 92, -93, -94, -95, -96, -97, -98, -99, -100
    ],
    _PERCENT
]
_MOTOR_ACTION = Literal['coast', 'brake', 'stop']
_MOTOR_UNIT = Literal['cm', 'in', 'rotations', 'degrees', 'seconds']


class _HubComponent:
    pass


class _Connectable:

    def __init__(self, port: _PORT, /):
        pass


class _Button:

    def is_pressed(self) -> bool:
        pass

    def wait_until_pressed(self):
        pass

    def wait_until_released(self):
        pass


class App:

    def play_sound(self, name: str, volume: _PERCENT = 100, /):
        """
        See documentation
        """
        pass

    def start_sound(self, name: str, volume: _PERCENT = 100, /):
        """
        See documentation
        """
        pass


class ForceSensor(_Connectable, _Button):

    def get_force_newton(self) -> int:
        pass

    def get_force_percentage(self) -> _PERCENT:
        pass


class DistanceSensor(_Connectable):

    def light_up_all(self, brightness: _PERCENT = 100, /):
        pass

    def light_up(
            self,
            right_top: _PERCENT = 100,
            left_top: _PERCENT = 100,
            right_bottom: _PERCENT = 100,
            left_bottom: _PERCENT = 100,
            /
    ):
        pass

    def wait_for_distance_closer_than(
            self,
            distance: float,
            unit: _DISTANCE = 'cm',
            short_range: bool = False,
            /
    ):
        pass

    def wait_for_distance_farther_than(
            self,
            distance: float,
            unit: _DISTANCE = 'cm',
            short_range: bool = False,
            /
    ):
        pass

    def get_distance_percentage(self, short_range: bool = False, /) -> _PERCENT:
        pass

    def get_distance_inches(self, short_range: bool = False, /) -> int:
        pass

    def get_distance_dm(self, short_range: bool = False, /) -> int:
        pass


class ColorSensor(_Connectable):

    def light_up_all(self, brightness: _PERCENT = 100, /):
        pass

    def light_up(self, light_1: _PERCENT = 100, light_2: _PERCENT = 100, light_3: _PERCENT = 100, /):
        pass

    def wait_until_color(self, color: _COLOR):
        pass

    def wait_for_new_color(self) -> _COLOR:
        pass

    def get_blue(self) -> _PERCENT:
        pass

    def get_red(self) -> _PERCENT:
        pass

    def get_green(self) -> _PERCENT:
        pass

    def get_color(self) -> _COLOR:
        pass

    def get_rgb_intensity(self) -> Tuple[_PERCENT, _PERCENT, _PERCENT, _PERCENT]:
        """
        :return: Red, Green, Blue, Overall intensity
        """
        pass

    def get_reflected_light(self) -> _PERCENT:
        pass

    def get_ambient_light(self) -> _PERCENT:
        pass


class Motor(_Connectable):
    # TODO: funcs
    pass


class MotorPair:

    def __init__(self, motor_1_port: _PORT, motor_2_port: _PORT, /):
        pass

    def start_tank_at_power(self, left_power: _POWER, right_power: _POWER, /):
        pass

    def start_at_power(self, power: _POWER, steering: _POWER = 0, /):
        pass

    def start_tank(self, left_speed: _POWER, right_speed: _POWER, /):
        pass

    def move_tank(
            self,
            amount: float,
            unit: _MOTOR_UNIT = 'cm',
            left_speed: Optional[_POWER] = None,
            right_speed: Optional[_POWER] = None,
            /
    ):
        pass

    def stop(self):
        pass

    def start(self, steering: _POWER = 0, speed: Optional[_POWER] = None, /):
        pass

    def move(
            self,
            amount: float,
            unit: _MOTOR_UNIT = 'cm',
            speed: Optional[_POWER] = None,
            /
    ):
        pass

    def get_default_speed(self) -> _POWER:
        pass

    def set_default_speed(self, default_speed: _POWER, /):
        pass

    def set_stop_action(self, action: _MOTOR_ACTION = 'coast', /):
        pass

    def set_motor_rotation(self, amount: float = 17.6, unit: Literal['cm', 'in'] = 'cm', /):
        pass


class Button(_HubComponent, _Button):

    def was_pressed(self) -> bool:
        """
        :return: Return True if this was pressed since last call
        """
        pass


class Speaker(_HubComponent):

    def set_volume(self, volume: _PERCENT = 100, /):
        pass

    def get_volume(self) -> _PERCENT:
        pass

    def beep(self, note: _MIDI_NOTE = 60, seconds: float = 0.2, /):
        pass


class LightMatrix(_HubComponent):

    def set_pixel(self, x: _PIXEL_POS, y: _PIXEL_POS, brightness: _PERCENT = 100, /):
        pass

    def show_image(self, image: str, brightness: _PERCENT = 100, /):
        """
        See documentation
        """
        pass

    def write(self, text: str):
        pass

    def off(self):
        pass


class StatusLight(_HubComponent):

    def on(self, color: _STATUS_COLOR = 'white', /):
        pass

    def off(self):
        pass


class MotionSensor(_HubComponent):

    def was_gesture(self, name: _GESTURE, /) -> bool:
        pass

    def wait_for_new_gesture(self) -> _GESTURE:
        pass

    def wait_for_new_orientation(self) -> _ORIENTATION:
        pass

    def get_orientation(self) -> _ORIENTATION:
        """
        :return: Returns which side of the hub is facing up. Font is charging cable side.
        """
        pass

    def get_gesture(self) -> _GESTURE:
        pass

    def get_pitch_angle(self) -> int:
        """
        :return: Degrees
        """
        pass

    def get_roll_angle(self) -> int:
        """
        :return: Degrees
        """
        pass

    def get_yaw_angle(self) -> int:
        """
        :return: Degrees
        """
        pass

    def reset_yaw_angle(self):
        pass


class MSHub:
    right_button: Button
    speaker: Speaker
    light_matrix: LightMatrix
    status_light: StatusLight
    motion_sensor: MotionSensor

    PORT_A: Literal['A']
    PORT_B: Literal['B']
    PORT_C: Literal['C']
    PORT_D: Literal['D']
    PORT_E: Literal['E']
    PORT_F: Literal['F']
