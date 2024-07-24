# LOID: Log Out/In Device - Smart School Project

LOID is a project developed during the "Hack Tues X" event under the theme "Back to the Roots," focusing on the subtopic of "Smart School." The project aims to streamline student authentication and interaction with online platforms through a personalized device. Each student possesses a unique device that securely stores their credentials, facilitating seamless access to educational resources.

## Project Overview

The core components of the LOID project include a Raspberry Pi Pico microcontroller, a 128x64 display, and two switches. Upon pressing the first switch, the device transmits the student's credentials (email and password) to a host computer running the necessary code. This information is encoded using the UTF-8 protocol for secure transmission. The host program receives and processes the data, utilizing Selenium to automate the login process on the Google Classroom platform.

Pressing the second switch triggers the device to send a "Logout" signal to the host program. Upon verification, the host initiates a logout sequence using Selenium, ensuring secure session management.

## Features

- Seamless authentication process for students
- Automated login and logout functionality for Google Classroom
- Intuitive interaction through physical switches and a display
- Customizable animations and user interface elements

## Installation

### On Your PC:

Ensure the following libraries are installed:

- Selenium: `pip install selenium`
- Serial : `pip install serial`

### On the Raspberry Pi Pico:

Install the necessary libraries in the lib folder on the board:

- adafruit_blinka (it may work without it)
- adafruit_circuitpython_ssd1306
- adafruit_circuitpython_displayio
- adafruit_imageload
- digitalio
- displayio

(If you get any error, open PuTTY or look at the shell(if you are using the Thonny IDE) and there you will see witch library is missing)


## Usage

1. Connect the Raspberry Pi Pico and ensure it is recognized by the host computer.
2. Upload the `pico.py` script to the Raspberry Pi Pico using a compatible IDE or text editor.
3. Execute the `host.py` script on the host computer, specifying the serial port of the Raspberry Pi Pico as an argument.
4. Interact with the device by pressing the designated switches to log in or log out of Google Classroom.

## Additional Notes

- Adjust the sleep intervals in the Selenium file (`selenium.py`) to optimize performance based on your system specifications.
- Customize the display animations and user interface elements to suit your preferences.

**Note:** The code is written in CircuitPython.

## Images
![PSLLD_image](https://github.com/user-attachments/assets/831c75c3-4529-45e7-9c22-13c570cc26de)

