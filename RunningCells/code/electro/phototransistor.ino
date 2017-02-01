int val;
const int ledPin1 = 3;
int valPWM = 64; //64 = 25%, 127 = 50%, 191 = 75%, 255 = 100%



void setup()

{

Serial.begin(9600); // sets the serial port to 9600
pinMode(ledPin1, OUTPUT);
}

void loop()

{

analogWrite(ledPin1, valPWM);

val = analogRead(A0); // read analog input pin 0


Serial.println(val); // prints the value read

//Serial.print(" "); // prints a space between the numbers

delay(10); // wait 10ms for next reading

}
