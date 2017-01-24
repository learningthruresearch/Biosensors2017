int led = 9;           // the PWM pin the LED is attached to
int brightness = 255;     // how many points to fade the LED by

// the setup routine runs once when you press reset:
void setup() {
  // declare pin 9 to be an output:
  pinMode(led, OUTPUT);
  analogWrite(led, brightness);
}

void loop() {
  // put your main code here, to run repeatedly:

}""
