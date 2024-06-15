#include <AccelStepper.h> // Include the AccelStepper library

#define DIR_PIN_1 2  // Define the direction pin
#define STEP_PIN_1 3 // Define the step pin
#define EN_PIN_1 4   // Define the enable pin


#define DIR_PIN_2 5  // Define the direction pin
#define STEP_PIN_2 6 // Define the step pin
#define EN_PIN_2 7   // Define the enable pin

// Create an instance of the AccelStepper class
AccelStepper stepper1(AccelStepper::DRIVER, STEP_PIN_1, DIR_PIN_1);
AccelStepper stepper2(AccelStepper::DRIVER, STEP_PIN_2, DIR_PIN_2);

void setup() {
  // Set the maximum speed and acceleration
  stepper1.setMaxSpeed(7000);      // Set max speed to 1000 steps per second
  stepper1.setAcceleration(1000);  // Set acceleration to 1000 steps per second^2

   stepper2.setMaxSpeed(1000);      // Set max speed to 1000 steps per second
  stepper2.setAcceleration(1000);  // Set acceleration to 1000 steps per second^2

  pinMode(EN_PIN_1, OUTPUT);  // Set enable pin as an output
  digitalWrite(EN_PIN_1, LOW); // Enable the motor driver

   pinMode(EN_PIN_2, OUTPUT);  // Set enable pin as an output
  digitalWrite(EN_PIN_2, LOW); // Enable the motor driver


  // Set the initial direction of the motor
  stepper1.setSpeed(5000); // Set speed to 500 steps per second
  stepper1.move(10000);    // Move 2000 steps in one direction

  stepper2.setSpeed(1000); // Set speed to 500 steps per second
  stepper2.move(10000);    // Move 2000 steps in one direction
}

void loop() {
  // Run the stepper motor
  if (stepper1.distanceToGo() == 0) {
    // If the stepper has reached the target position, change direction
    stepper1.moveTo(-stepper1.currentPosition());
    stepper2.moveTo(-stepper2.currentPosition());
    
  }
  stepper1.run();
  stepper2.run();
}
