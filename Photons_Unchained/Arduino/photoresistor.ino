int val;
int brightness = 0;
int sensorpin=A0; // the pin used is A0


void setup()

{
pinMode(sensorpin, INPUT); // activates the pin (INPUT)
Serial.begin(9600); // sets the serial port to 9600

}

void loop()

{

val = analogRead(sensorpin); // read analog input pin 0
brightness = map(val, 0, 1023, 0, 255); // converts the output of the sensor from [0,1023] to [0,255]
Serial.println(brightness); // prints the value in the serial (top right)

delay(400); 

} 
