# Pixel Arduino Flask Webapp

> Rafawastaken | October 2022

## About

Web interface to control local LED Matrix connected to arduino.

## How does it work

tldr; Graphical interface to select LED in the Matrix to turn off, turn on. Python script is sending get request to defined endpoint to read the current status of any given LED. The LED status are sent to the arduino using SERIAL comunication.

## Hardware Required:

1. Any controller of you **needs to support SERIAL COMUNICATION**

- I've used arduino nano

2. 8x8 LED Matrix **without I2C (IIC) communication**:

- [Aliexpress Product](https://pt.aliexpress.com/item/32717752819.html "Aliexpress link")

3. Breadboard
4. Jumper Cables

## Project Structure

The project has 2 main folder:

### Hardware:

- Contains all the arduino codes and connections;

### Web:

- Contains the webapp to drive the LED matrix;

## Install Dependencies

> python3 -m pip install -r requirements.txt

## Run it

> python3 run.py
