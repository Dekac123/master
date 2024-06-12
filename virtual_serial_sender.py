import serial
import random
import time

def send_random_data(port='/tmp/ttyV0', baudrate=9600, interval=0.01):
    """
    Sends random data between 50 and 55 to the specified serial port every 0.1 seconds.

    Parameters:
    - port: The serial port to use (default is '/tmp/ttyV0').
    - baudrate: The baud rate for the serial communication (default is 9600).
    - interval: The interval in seconds between data sends (default is 0.1 seconds).
    """
    try:
        # Open the serial port
        with serial.Serial(port, baudrate, timeout=1) as ser:
            print(f"Sending data to {port} every {interval} seconds.")
            while True:
                # Generate a random value between 50 and 55
                random_value = random.randint(20, 25)
                # Send the value as a string
                ser.write(f"{random_value}\n".encode('utf-8'))
                print(f"Sent: {random_value}")
                # Wait for the specified interval
                time.sleep(interval)
    except serial.SerialException as e:
        print(f"Error opening or using serial port {port}: {e}")

# Example usage:
# Call the function to start sending random data
send_random_data()
