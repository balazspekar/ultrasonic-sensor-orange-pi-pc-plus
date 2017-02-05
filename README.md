# Ultrasonic Sensor HC-SR04 Sample Python Code for Orange Pi PC Plus v1.1

The code in this repository is similar to the one at [ModMyPi](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi) however this code works on the Orange Pi PC Plus v1.1 (using a Raspbian Image).

I apologize for the unprofessional breadboard work, I just wanted to put this sample together as quick as possible.

I used the following library to make GPIO pins work on my board:
[Orange Pi PC GPIO PyH3](https://github.com/duxingkei33/orangepi_PC_gpio_pyH3) 

Pay attention how much voltage you send to your input pin! The ultrasonic sensor sends 5V. Use resistors to make it around 3V.

Some images about the setup:

![alt tag](https://raw.githubusercontent.com/balazspekar/ultrasonic-sensor-orange-pi-pc-plus/master/1.jpg)
![alt tag](https://raw.githubusercontent.com/balazspekar/ultrasonic-sensor-orange-pi-pc-plus/master/2.jpg)
![alt tag](https://raw.githubusercontent.com/balazspekar/ultrasonic-sensor-orange-pi-pc-plus/master/3.jpg)

Orange Pi Pc Plus v1.1 PIN Layout:

![alt tag](https://raw.githubusercontent.com/balazspekar/ultrasonic-sensor-orange-pi-pc-plus/master/4.jpg)
