const int led = 3; //pin 3 on the LED, a PMW pin that allows variation
byte brightness = 0; //choose the intensity between [0,255]. No unity.

void setup() {
pinMode(led, OUTPUT); 
}

void loop() {

analogWrite(led, brightness); // Changes the intensity of the LED.

delay(30);
}

//7
