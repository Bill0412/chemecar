## Chem E Car Project by ZJU School of ChemE

# Introduciton
This repository provides control solution for the Chem E Car 
Project for a competition of our team at School of Chemical 
Engineering, ZJU.

# What is Chem E Car Competition
This is a competition that require all teams to control
a car with controled chemical reactions. We are supposed
to stop the car around the finishing line by observing
our chemical reactions.

# Our Solution
We use a reaction fades the color of the solution as it
goes along and by analyzing the video taken of the 
solution, we stop the car promptly when the reaction ends.

A Raspberry Pi 3B is used to control the whole system, and 
that's where this repository is deployed at.

# How to deploy to raspberry Pi
Firstly, clone this project
```
$ git clone https://www.github.com/bill0412/chemecar /home/pi/Desktop/chemecar
```

Then, set up starting the program on start
```
$ sudo crontab -e
```

select the best editor for you and write
```
@reboot nohup python3 /home/pi/Desktop/chemecar/solution-cv/car.py &
```

Next time on Raspberry Pi startup, wait about 1 minute and you will see that the program is automatically initialized.


# Liscence
MIT
