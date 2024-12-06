// GSR sensör pinini tanımlıyoruz
const int GSR_PIN = A0;

// LED pinini tanımlıyoruz
const int LED_PIN = 51;

// GSR için referans değerini belirliyoruz
int baseline = 0;
const int numReadings = 10;
int readings[numReadings];
int readIndex = 0;
int total = 0;
int average = 0;

void setup() {
  // LED pini çıkış olarak ayarlıyoruz
  pinMode(LED_PIN, OUTPUT);
  
  // Seri haberleşmeyi başlatıyoruz
  Serial.begin(9600);
  
  // Baseline değerini hesaplamak için okumaları sıfırlıyoruz
  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
  }
  
  // GSR sensöründen temel (baseline) değeri alıyoruz
  baseline = getBaseline();
  Serial.print("Baseline: ");
  Serial.println(baseline);
}

void loop() {
  // GSR sensöründen veri okuyoruz
  int gsrValue = analogRead(GSR_PIN);
  
  // Ortalama değeri güncelliyoruz
  total = total - readings[readIndex];
  readings[readIndex] = gsrValue;
  total = total + readings[readIndex];
  readIndex = (readIndex + 1) % numReadings;
  average = total / numReadings;
  
  // Seri monitöre değerleri yazdırıyoruz
  Serial.print("GSR Value: ");
  Serial.println(gsrValue);
  
  // Seri Plotter için veri yazdırıyoruz
  Serial.print("GSR: ");
  Serial.print(gsrValue);
  Serial.print(" Average: ");
  Serial.print(average);
  Serial.print(" Baseline: ");
  Serial.println(baseline);
  
  // Yalan tespiti ve LED kontrolü
  if (average > baseline + 10) { // Eşik değeri 10 olarak belirlendi
    digitalWrite(LED_PIN, HIGH); // LED'i yak
  } else {
    digitalWrite(LED_PIN, LOW);  // LED'i söndür
  }
  
  delay(500);
}

int getBaseline() {
  int total = 0;
  for (int i = 0; i < 50; i++) {
    total += analogRead(GSR_PIN);
    delay(20);
  }
  return total / 50;
}

