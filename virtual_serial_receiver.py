import serial

# Replace 'COM2' with your actual virtual COM port
host_port = '/tmp/ttyV1'
baudrate = 9600

# Open the serial port
ser = serial.Serial(host_port, baudrate, timeout=1)

try:
    while True:
        # Read data from the serial port
        if ser.in_waiting > 0:
            received_data = ser.readline().decode('utf-8').strip()
            print(f"Received: {received_data}")
except KeyboardInterrupt:
    pass
finally:
    ser.close()  # Close the serial port
