from curses import baudrate
from time import sleep
import serial
import requests

def generate_matrix(sample, coluna, linha, estado):
    sample[coluna][linha] = estado
    return sample

def get_status():
    endpoint = "http://127.0.0.1:5000/matrix-status"
    r = requests.get(endpoint)
    content = r.json()

    return content

def send_arduino(sample):
    arduino = serial.Serial(port = "COM3", baudrate='9600', timeout=0.1)
    arduino.write(bytes(str(sample), 'utf-8'))

    print(str(sample))
    sleep(0.5)
    data = arduino.readline()
    return data

def main():
    sample = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    count = 0
    while True:
        content = get_status()

        for enum, entry in enumerate(content):
            coluna = int(entry.get("coluna")) - 1
            linha = int(entry.get('linha')) - 1
            estado = int(entry.get('estado'))
            sample = generate_matrix(sample, linha, coluna, estado)

        # Send it to arduino
        data = send_arduino(sample)
        sleep(1)

        print(f"{data} - sending: {count}", end = '\r')
        count = count + 1



if __name__ == '__main__':
    main()