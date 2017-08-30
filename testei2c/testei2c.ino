#include <Wire.h>

int SLAVE_ADDRESS = 3;
int ID = 125;
int tipo = 3;
int number = 0;
int state = 0;

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600); // start serial for output
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);
    
    // define callbacks for i2c communication
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);
    
    Serial.println("Ready!");
}

void loop() {
  delay(100);
}

// callback for received data
void receiveData(int byteCount){

  while(Wire.available()) {
    number = Wire.read();
    Serial.print("data received: ");
    Serial.println(number);
    
    if(SLAVE_ADDRESS == 3){
      SLAVE_ADDRESS = number;
      Wire.begin(SLAVE_ADDRESS);
    }
  }
}

// callback for sending data
void sendData(){
  Serial.println(number);
  if (SLAVE_ADDRESS == 3){
    Wire.write(tipo);
    return;
  }
  if (number == 0){
     Wire.write(ID);
  }
  else if (number == 1) {
     Wire.write(tipo);
  }
  else Wire.write(millis());
}
