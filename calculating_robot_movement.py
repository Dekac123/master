import math


def horizontal_rotation(motor_rotation:int) -> int:

    motor_gear = 16
    plate_gear = 50

    return round(motor_rotation * (motor_gear/plate_gear))

def vertical_rotation(motor_rotation:int) -> int:

    m4_pitch = 0.7

    return round(motor_rotation * (m4_pitch))
