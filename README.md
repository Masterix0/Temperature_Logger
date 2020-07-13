# Temperature_Logger
A simple temperature logger written in Python.
Reads temperature from a connected thermometer (in my case, I'll be using 
a Raspberry Pi 3B connected to the thermomether using GPIO, but feel free
to change your input by changing the parser.py file).
This project is made to have independent modules, meaning you can use whichever
temperature input you wish and still be able to use the rest of the modules.
In the future, I wish to implement email notifications in case the temperature
goes above over a certain threshold and send a graph containing all the temperature
readings made over the course of a day every night.
