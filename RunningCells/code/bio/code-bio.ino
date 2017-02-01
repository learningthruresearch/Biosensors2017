//Initialisation
const int ledPin1 = 3;
const int ledPin2 = 5;
const int ledPin3 = 9;
int valPWM = 64; //64 = 25%, 127 = 50%, 191 = 75%, 255 = 100% - règle l'intensité des LEDs

void setup() {     
  // Initialise le Pin comme une sortie
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() {
  analogWrite(ledPin1, valPWM);
  analogWrite(ledPin2, valPWM);
  analogWrite(ledPin3, valPWM);
}
