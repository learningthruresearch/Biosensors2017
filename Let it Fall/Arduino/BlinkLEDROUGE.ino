//Constants, here each Pin which will be used
const int ledPin1 = 5;
const int ledPin2 = 10;
const int ledPin3 = 3;
const int ledPin4 = 6;
const int ledPin5 = 9;

//Give the intensities for each LED : 64 = 25%, 127 = 50%, 191 = 75%, 255 = 100%
int val1 = 255; //100%
int val2 = 51; //20%
int val3 = 102; //40%
int val4 = 153; //60%
int val5 = 204; //80%

void setup() {     
  // Initialise each Pin as an output with pinMode()
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() { // Give to each Pin a value, here an intensity
  analogWrite(ledPin1, val1);
  analogWrite(ledPin2, val2);
  analogWrite(ledPin3, val3);
  analogWrite(ledPin4, val4);
  analogWrite(ledPin5, val5);
}



