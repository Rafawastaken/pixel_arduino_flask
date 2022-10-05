# Pixel Arduino Flask Webapp

> Rafawastaken | October 2022

## About

Web interface to control local LED Matrix connected to arduino.

## How does it work

tldr; Graphical interface to select LED in the Matrix to turn off, turn on. Python script is sending get request to defined endpoint to read the current status of any given LED. The LED status are sent to the arduino using SERIAL comunication.

## Install Dependencies

> python3 -m pip install -r requirements.txt

## Run it

> python run.py
