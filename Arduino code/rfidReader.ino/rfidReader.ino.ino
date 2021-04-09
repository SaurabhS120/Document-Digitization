#define LED 2
#define SCAN true
#define STOP false
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance

String a;
bool state=STOP;
void changeState(bool s){
  if(s){
    digitalWrite(LED,HIGH);
     Serial.println("SCAN");
  }else{
    digitalWrite(LED,LOW);
    Serial.println("STOP");
  }
  state=s;
}
bool getUid(){
  // Reset the loop if no new card present on the sensor/reader. This saves the entire process when idle.
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return false;
  }

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return false;
  }

  // Dump debug info about the card; PICC_HaltA() is automatically called
  for(int i=0;i<4;i++){
    Serial.print(mfrc522.uid.uidByte[i],HEX);
  }
  Serial.println();
  return true;
}
void setup() {
  Serial.begin(9600);   // Initialize serial communications with the PC
  while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
  SPI.begin();      // Init SPI bus
  mfrc522.PCD_Init();   // Init 
  pinMode(LED,OUTPUT);
  digitalWrite(LED,LOW);
}

void loop() {
  while(Serial.available()) {
  
    a= Serial.readString();// read the incoming data as string
    
    a.trim();
    if(a.equals("start")){
      changeState(SCAN);
    }
    if(a.equals("stop")){
      changeState(STOP);
    }
  
  }

    if(state==SCAN){
      if(getUid()){
        changeState(STOP);
      }
    }

}
