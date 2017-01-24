//Biosensors week 1
//Bi lumni team

// 18/01/17
// Arduino code for LDR sensors


int sensorPin = A0; // select the input pin for ldr
int sensorValue = 0; // variable to store the value coming from the sensor
int Lux = 0; // variable to store the Lux
void setup() {
  Serial.begin(9600); //sets serial port for communication
}
void loop() { 
  sensorValue = analogRead(sensorPin); // read the value from the sensor
  Serial.println(sensorValue); //prints the values coming from the sensor on the screen
  Lux=(2500/((sensorValue*0.0048828125)-500))/10;
  Serial.println(Lux);
  Serial.println(Lux);
  delay(100);
}

// Code largely inspired by : https://diyhacking.com/arduino-ldr-sensor/
