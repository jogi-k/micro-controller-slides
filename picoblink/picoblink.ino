

#define MILLIWAIT 500
#define TOGGLE_PIN 18 

void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(TOGGLE_PIN, OUTPUT);
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);
    digitalWrite(TOGGLE_PIN, HIGH);
    delayMicroseconds(MILLIWAIT * 1000);
    digitalWrite(TOGGLE_PIN, LOW);
    digitalWrite(LED_BUILTIN, LOW);
    delayMicroseconds(MILLIWAIT * 1000);
}
