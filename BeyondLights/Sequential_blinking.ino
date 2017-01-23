
/* A simple program to sequentially turn on and turn off 2 set of LEDs */ 

int LED1 = 12;
int LED2 = 13;
int LED3 = 2;
int LED4 = 3;

void setup() {
   pinMode(LED1, OUTPUT);
   pinMode(LED2, OUTPUT);
   pinMode(LED3, OUTPUT);
   pinMode(LED4, OUTPUT);
}


void loop() {
  //digitalWrite(LED1, HIGH);    // turn on LED1 
  //digitalWrite(LED2, HIGH);    // turn on LED2
  //delay(1000);                  // wait for x ms 
  //digitalWrite(LED1, LOW);     // turn off LED1      
  //digitalWrite(LED2, LOW);     // turn off LED2
  
  digitalWrite(LED3, HIGH);    // turn on LED3 
  digitalWrite(LED4, HIGH);    // turn on LED4 
  //delay(1000);                  // wait for x ms
  //digitalWrite(LED3, LOW);     // turn off LED3
  //digitalWrite(LED4, LOW);     // turn off LED4
}
