from curses import baudrate
from time import sleep
import serial

arduino = serial.Serial("COM3", baudrate=9600, timeout=1)

def enviar(linha):
    # arduino_data = f"{linha} {coluna} {valor}"
    arduino.write(bytes(linha, 'utf-8'))
    sleep(1)
    data = arduino.readline()
    return data

def send_com_matrix(linha, coluna, estado):
    arduino.write(bytes(linha, 'utf-8'))
    arduino.write(bytes(coluna, 'utf-8'))
    arduino.write(bytes(estado, 'utf-8'))
    sleep(1)
    data = arduino.readline()
    return data


while True:
    linha = str(input("Linha acender: "))
    coluna = str(input("Coluna acender: "))
    estado = str(input("Estado do pixel: "))
    send_com_matrix(linha, coluna, estado)
    