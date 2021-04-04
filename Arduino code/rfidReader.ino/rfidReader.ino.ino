#define LED 13
#define SCAN true
#define IDLE false
String a;
bool state=IDLE;
void changeState(bool s){
  state=s;
  if(s==SCAN){
    digitalWrite(LED,HIGH);
  }else{
    digitalWrite(LED,LOW);
  }
}
void setup() {

Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
pinMode(LED,OUTPUT);
changeState(IDLE);
}

void loop() {

while(Serial.available()) {

a= Serial.readString();// read the incoming data as string

Serial.println(a);
a.trim();
if(a.equals("start")){
  changeState(SCAN);
}
if(a.equals("stop")){
  changeState(IDLE);
  
}

}

}
