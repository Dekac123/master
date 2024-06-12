import serial
import time
from serial_plotting_live_data import x_list, y_list, z_list

waiting_for_ready_state = 30

ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
time.sleep(waiting_for_ready_state)  #at least waiting this much for robot


def serial_read(ser_param: serial):
    return ser_param.readline()


def serial_write_tick(ser_param: serial): #move motors
    ser_param.write('tick')
    ser_param.write('\n')


def waiting_for_ready_robot(ser_param: serial):
    while (not ser_param.inWaiting()):  #waiting for robot to be ready
        print('Waiting for robot to be ready: \n')
    ser_param.flushInput()


def serial_plan(ser_param: serial):

    pass
