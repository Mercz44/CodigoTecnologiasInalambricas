int num;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  num=0;
}

void loop() {
  // put your main code here, to run repeatedly:
  num=num+1;
  Serial.println(num);
  delay(1000);
}
