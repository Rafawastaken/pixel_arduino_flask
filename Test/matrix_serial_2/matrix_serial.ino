/*
  PINS A SEREM UTILIZADOS:
  D2, D3, D4, D5, D6, D7, D8, D9, D10
  D11, D12, D13, A0, A1, A2, A3
*/

// LINHAS
#define ROW_1 2
#define ROW_2 3
#define ROW_3 4
#define ROW_4 5
#define ROW_5 6
#define ROW_6 7
#define ROW_7 8
#define ROW_8 9

// COLUNAS
#define COL_1 10
#define COL_2 11
#define COL_3 12
#define COL_4 13
#define COL_5 A0
#define COL_6 A1
#define COL_7 A2
#define COL_8 A3

int linha;
int coluna;
int estado;

void setup() {
  // INICIAR SERIAL COM TIMEOUT 1
  Serial.begin(9600);
  Serial.setTimeout(1);
  // DEFINIR PINOS COMO OUTPUT
  for (byte i = 2; i <= 13; i++)
    pinMode(i, OUTPUT);
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
}

void loop() {
  while (!Serial.available())
    ;

  linha = Serial.readString().toInt();
  coluna = Serial.readString().toInt();
  estado = Serial.readString().toInt();

  selecionar_linha(linha, estado);
  selecionar_coluna(coluna, estado);

  delay(500);
}


void selecionar_linha(int linha, int estado) {
  if (linha == 1) {
    if (estado == 1) {
      digitalWrite(ROW_1, HIGH);
    } else {
      digitalWrite(ROW_1, LOW);
    }
  } else if (linha == 2) {
    if (estado == 1) {
      digitalWrite(ROW_2, HIGH);
    } else {
      digitalWrite(ROW_2, LOW);
    }
  } else if (linha == 3) {
    if (estado == 1) {
      digitalWrite(ROW_3, HIGH);
    } else {
      digitalWrite(ROW_3, LOW);
    }
  } else if (linha == 4) {
    if (estado == 1) {
      digitalWrite(ROW_4, HIGH);
    } else {
      digitalWrite(ROW_4, LOW);
    }
  } else if (linha == 5) {
    if (estado == 1) {
      digitalWrite(ROW_5, HIGH);
    } else {
      digitalWrite(ROW_5, LOW);
    }
  } else if (linha == 6) {
    if (estado == 1) {
      digitalWrite(ROW_6, HIGH);
    } else {
      digitalWrite(ROW_6, LOW);
    }
  } else if (linha == 7) {
    if (estado == 1) {
      digitalWrite(ROW_7, HIGH);
    } else {
      digitalWrite(ROW_7, LOW);
    }
  } else if (linha == 8) {
    if (estado == 1) {
      digitalWrite(ROW_8, HIGH);
    } else {
      digitalWrite(ROW_8, LOW);
    }
  }
}

void selecionar_coluna(int coluna, int estado) {
  if (coluna == 1) {
    if (estado == 1) {
      digitalWrite(COL_1, HIGH);

    } else {
      digitalWrite(COL_1, LOW);
    }
  }

  else if (coluna == 2) {
    if (estado == 1) {
      digitalWrite(COL_2, HIGH);

    } else {
      digitalWrite(COL_2, LOW);
    }

  } else if (coluna == 3) {
    if (estado == 1) {
      digitalWrite(COL_3, HIGH);

    } else {
      digitalWrite(COL_3, LOW);
    }

  } else if (coluna == 4) {
    if (estado == 1) {
      digitalWrite(COL_4, HIGH);

    } else {
      digitalWrite(COL_4, LOW);
    }

  } else if (coluna == 5) {
    if (estado == 1) {
      digitalWrite(COL_5, HIGH);

    } else {
      digitalWrite(COL_5, LOW);
    }

  } else if (coluna == 6) {
    if (estado == 1) {
      digitalWrite(COL_6, HIGH);

    } else {
      digitalWrite(COL_6, LOW);
    }

  } else if (coluna == 7) {
    if (estado == 1) {
      digitalWrite(COL_7, HIGH);

    } else {
      digitalWrite(COL_7, LOW);
    }

  } else if (coluna == 8) {
    if (estado == 1) {
      digitalWrite(COL_8, HIGH);

    } else {
      digitalWrite(COL_8, LOW);
    }
  }
}