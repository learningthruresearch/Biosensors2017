#include "Arduino.h"

int ledPin = 9;
int brightness = 10; // Change this value for different brightness. Put 0|1|10|100|255

void setup()
{
  // initialize serial comms
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); 
}

void loop()
{
  // read A0
  analogWrite(ledPin, brightness);
  int val1 = analogRead(A0);
  Serial.print(val1);
  Serial.print(" ");
  Serial.print(millis());
  Serial.print("\n");
  // wait 
  delay(1000);
}
