#include <AccelStepper.h> // Include the AccelStepper library
#include <VL53L0X.h>

#define DIR_PIN_1 4  // Define the direction pin
#define STEP_PIN_1 3 // Define the step pin
#define EN_PIN_1 2   // Define the enable pin

#define DIR_PIN_2 7  // Define the direction pin
#define STEP_PIN_2 6 // Define the step pin
#define EN_PIN_2 5   // Define the enable pin

// Create instances of the AccelStepper class
AccelStepper stepper1(AccelStepper::DRIVER, STEP_PIN_1, DIR_PIN_1);
AccelStepper stepper2(AccelStepper::DRIVER, STEP_PIN_2, DIR_PIN_2);

void setup() {
  Serial.begin(9600);

  // Set the maximum speed and acceleration
  stepper1.setMaxSpeed(1000);      // Set max speed to 1000 steps per second for stepper1
  stepper1.setAcceleration(500);   // Set acceleration to 500 steps per second^2 for stepper1

  stepper2.setMaxSpeed(1000);      // Set max speed to 1000 steps per second for stepper2
  stepper2.setAcceleration(500);   // Set acceleration to 500 steps per second^2 for stepper2

  pinMode(EN_PIN_1, OUTPUT);  // Set enable pin as an output for stepper1
  digitalWrite(EN_PIN_1, LOW); // Enable the motor driver for stepper1

  pinMode(EN_PIN_2, OUTPUT);  // Set enable pin as an output for stepper2
  digitalWrite(EN_PIN_2, LOW); // Enable the motor driver for stepper2

  // Set the initial speed for continuous rotation
  stepper1.setSpeed(2000); // Set speed to 500 steps per second for stepper1
  stepper2.setSpeed(300); // Set speed to 500 steps per second for stepper2
}

void loop() {
  // Run the stepper motors at constant speed
  stepper1.runSpeed();  // Run stepper1 at the set speed
  stepper2.runSpeed();  // Run stepper2 at the set speed
}
