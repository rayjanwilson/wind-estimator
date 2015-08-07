#include <Wire.h>
#include "RTClib.h"
#include "Adafruit_TMP007.h"
#include "Adafruit_HTU21DF.h"
#include <SPI.h>
#include "SD.h"

// Set the pins used
#define chipSelect 10

// the logging file
File logfile;
char filename[8];

RTC_DS1307 rtc;
Adafruit_TMP007 tmp007;
Adafruit_HTU21DF htu = Adafruit_HTU21DF();

void setup() {
  Serial.begin(57600);

  Serial.println("Initializing SD card...");
  // make sure that the default chip select pin is set to
  // output, even if you don't use it:
  pinMode(10, OUTPUT);
  
  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    return;
  }
  Serial.println("Card initialized");
  
  Wire.begin();
  if(!rtc.begin()){
    Serial.println("RTC failed");
  }
  DateTime now = rtc.now();
  //char buf[50];
  sprintf(filename, "%02d%02d%02d%02d", now.month(), now.day(), now.hour(), now.minute());
  Serial.print("logging to "); Serial.println(filename);
  
  if (! tmp007.begin((uint8_t)TMP007_CFG_4SAMPLE)) {
    Serial.println("No temperature sensor found");
    while (1);
  }
  
  if (!htu.begin()) {
    Serial.println("Couldnt find humidity sensor!");
    while (1);
  }
}

uint32_t timer = millis();

void loop() {

  // if millis() or timer wraps around, we'll just reset it
  if (timer > millis())  timer = millis();

  // approximately every 1 seconds or so, print out the current stats
  if (millis() - timer > 1000) { 
    timer = millis(); // reset the timer


      float objt = tmp007.readObjTempC();
      float diet = tmp007.readDieTempC();
      float hum = htu.readHumidity();
      float hum_temp = htu.readTemperature();
      
      DateTime now = rtc.now();
      //long seconds = now.secondstime();
      
      File logfile = SD.open(filename, FILE_WRITE);
      if (logfile) {
        logfile.print(now.unixtime());
        logfile.print(", ");
        logfile.print(objt);
        logfile.print(", ");
        logfile.print(diet);
        logfile.print(", ");
        logfile.print(hum);
        logfile.print(", ");
        logfile.print(hum_temp);
        logfile.println();
        logfile.close();
        
      }else{
        Serial.println("error writing data to data.txt");
      }
      Serial.print(now.unixtime());
      Serial.print(", ");
      Serial.print(objt);
      Serial.print(", ");
      Serial.print(diet);
      Serial.print(", ");
      Serial.print(hum);
      Serial.print(", ");
      Serial.print(hum_temp);
      Serial.println(" ");

  }

  
}
