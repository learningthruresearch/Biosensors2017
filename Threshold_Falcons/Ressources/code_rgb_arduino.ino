    /*     Arduino Color Sensing Tutorial
     *      
     *  by Dejan Nedelkovski, www.HowToMechatronics.com
     *  
     */
     
    #define S0 4
    #define S1 5
    #define S2 6
    #define S3 7
    /*#define LED 13*/
    #define sensorOut 8
    int frequency = 0;
    void setup() {
      pinMode(S0, OUTPUT);
      pinMode(S1, OUTPUT);
      pinMode(S2, OUTPUT);
      pinMode(S3, OUTPUT);
      //pinMode(LED, OUTPUT);
      pinMode(sensorOut, INPUT);
      
      // Setting frequency-scaling to 20%
      digitalWrite(S0,HIGH);
      digitalWrite(S1,LOW);
      //digitalWrite(LED, LOW);
      
      Serial.begin(9600);
    }
    void loop() {
      // Setting red filtered photodiodes to be read
      digitalWrite(S2,LOW);
      digitalWrite(S3,LOW);
      // Reading the output frequency
      frequency = pulseIn(sensorOut, LOW);
      //Remaping the value of the frequency to the RGB Model of 0 to 255
      Serial.print("nomapR= ");//printing name
      Serial.print(frequency);
      Serial.print("  ");
      frequency = map(frequency, 0,1500,0, 255);
      // Printing the value on the serial monitor
      Serial.print("R= ");//printing name
      Serial.print(frequency);//printing RED color frequency
      Serial.print("  ");
      delay(100);
      // Setting Green filtered photodiodes to be read
      digitalWrite(S2,HIGH);
      digitalWrite(S3,HIGH);
      // Reading the output frequency
      frequency = pulseIn(sensorOut, LOW);
      //Remaping the value of the frequency to the RGB Model of 0 to 255
      Serial.print("nomapG= ");//printing name
      Serial.print(frequency);
      Serial.print("  ");
      frequency = map(frequency, 0,1500,0,255);
      // Printing the value on the serial monitor
      Serial.print("G= ");//printing name
      Serial.print(frequency);//printing RED color frequency
      Serial.print("  ");
      delay(100);
      // Setting Blue filtered photodiodes to be read
      digitalWrite(S2,LOW);
      digitalWrite(S3,HIGH);
      // Reading the output frequency
      frequency = pulseIn(sensorOut, LOW);
      //Remaping the value of the frequency to the RGB Model of 0 to 255
      Serial.print("nomapB= ");//printing name
      Serial.print(frequency);
      Serial.print("  ");
      frequency = map(frequency, 0,1500,0,255);
      // Printing the value on the serial monitor
      Serial.print("B= ");//printing name
      Serial.print(frequency);//printing RED color frequency
      Serial.println("  ");
      delay(100);
    }
