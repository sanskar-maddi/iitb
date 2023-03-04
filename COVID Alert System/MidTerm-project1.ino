#define BLYNK_PRINT Serial
#include<SimpleTimer.h>
#include <SoftwareSerial.h>
#include<DHT.h>
#include<Servo.h>
#include<BlynkSimpleStream.h>

#define DHTPIN 2
#define DHTTYPE DHT11

SoftwareSerial s(2, 3);
DHT dht ( DHTPIN , DHTTYPE);
Servo motor;
SimpleTimer timer;
float humid;
int LED=7; 

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "YourAuthToken";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Aniket";
char pass[] = "123456712";

void read_values()
{
   humid = dht.readHumidity();
   Blynk.virtualWrite(V3, humid);
}

void setup()
{
  // Debug console
  motor.attach(8);
  Serial.begin(9600);
  Blynk.begin(Serial, auth);
  timer.setInterval(1000, read_values);
  pinMode(LED, OUTPUT);
}

void loop()
{
  Blynk.run();
  if ( humid <= 50)
  {
      for(int pos = 0; pos <= 180; pos++)
      {
        motor.write(pos);
      }
      for( int pos = 180; pos >= 0; pos--)
      {
        motor.write(pos);
      }
      digitalWrite(LED, HIGH);
      delay(500);
  }
  else
  {
      digitalWrite(LED, LOW);
      delay(500);
  }
  timer.run();
}
