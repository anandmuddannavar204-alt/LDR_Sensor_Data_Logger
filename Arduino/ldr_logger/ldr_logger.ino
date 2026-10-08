// LDR Sensor Data Logger
// Hardware: Arduino Uno, LDR, 10k ohm resistor
// Wiring: 5V -> LDR -> A0 -> 10k resistor -> GND

const int ldrPin = A0;

void setup() {
  Serial.begin(9600);
  Serial.println("Time_ms,LDR_Value");
}

void loop() {
  unsigned long timeMs = millis();
  int ldrValue = analogRead(ldrPin);

  Serial.print(timeMs);
  Serial.print(",");
  Serial.println(ldrValue);

  delay(1000); // approximately one reading per second
}
