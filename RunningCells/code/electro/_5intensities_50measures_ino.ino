/*
 * Code d'exemple pour une photorÃ©sistance.
 */
//Constantes
const int ledPin1 = 3;
int valPWM = 255; //64 = 25%, 127 = 50%, 191 = 75%, 255 = 100%
int count = 0; //variable 

// Fonction setup(), appelÃ©e au dÃ©marrage de la carte Arduino
void setup() {
   // Initialise le Pin comme une sortie | Initialize the digital pin as an output with pinMode()
  pinMode(ledPin1, OUTPUT);
  // Initialise la communication avec le PC
  Serial.begin(9600);
}

// Fonction loop(), appelÃ©e continuellement en boucle tant que la carte Arduino est alimentÃ©e
void loop() {
  if (count == 0) {
    delay(5000);
  }
  analogWrite(ledPin1, valPWM);
  if (count <= 50) {
    int valeur = analogRead(A0);   // Mesure la tension sur la broche A0
  //  int valeurnew = map(valeur, 0, 1024, 0, 10);
    // Envoi la mesure au PC pour affichage et attends 250ms
    Serial.print(valPWM);
    Serial.print(',');
    Serial.println(valeur);
    count ++ ;1;
    delay(100);
  }
  }
