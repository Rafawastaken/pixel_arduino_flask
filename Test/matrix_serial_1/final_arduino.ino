#define ROW_1 2
#define ROW_2 3
#define ROW_3 4
#define ROW_4 5
#define ROW_5 6
#define ROW_6 7
#define ROW_7 8
#define ROW_8 9

#define COL_1 10
#define COL_2 11
#define COL_3 12
#define COL_4 13
#define COL_5 A0
#define COL_6 A1
#define COL_7 A2
#define COL_8 A3

const byte rows[] = {
  ROW_1, ROW_2, ROW_3, ROW_4, ROW_5, ROW_6, ROW_7, ROW_8
};
const byte col[] = {
  COL_1, COL_2, COL_3, COL_4, COL_5, COL_6, COL_7, COL_8
};

String Status;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);

  for (byte i = 2; i <= 13; i++) {
    pinMode(i, OUTPUT);
    pinMode(A0, OUTPUT);
    pinMode(A1, OUTPUT);
    pinMode(A2, OUTPUT);
    pinMode(A3, OUTPUT);
  }
}

void loop() {
  while (!Serial.available());
  Status =  Serial.readString();
  // byte STATUS[] = Status.toCharArray();
  
}

void  drawScreen(byte buffer2[])
{
  for (byte i = 0; i < 8; i++)
  {
    digitalWrite(rows[i], HIGH);
    for (byte a = 0; a < 8; a++)
    {
      digitalWrite(col[a], (buffer2[i] >> a) & 0x01);
      delayMicroseconds(100);
      digitalWrite(col[a], 1);
    }
    digitalWrite(rows[i], LOW);
  }
}
