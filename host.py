import argparse
import re
import serial
import time

parser = argparse.ArgumentParser()
parser.add_argument("port", type=str, help="Serial port of the board", nargs=1)
args = parser.parse_args()
port = args.port

channel = serial.Serial(args.port[0])
channel.timeout = 0.05

def check_for_bracets(s):
    print(s)

    pattern = r'^\((.*)\)$'
    return bool(re.match(pattern, s))


username = ""
password = ""
while True:
    
    line = None
    try:
        line = channel.readline()
    except KeyboardInterrupt:
        print("KeyboardInterrupt - quitting")
        exit()
    

    if line:
        try:
            decoded_line = line.decode("utf8").strip()

            if check_for_bracets(decoded_line):
                if(len(username) == 0):
                    username = decoded_line[1:-1]
                else:
                    password = decoded_line[1:-1]
            else:
                if decoded_line == "Logout":
                    from selenium_test import logout
                    logout()
                    break

            if len(username) > 0 and len(password) > 0:
                from selenium_test import login
                login(username, password)
                username = ""
                password = ""
        except ValueError:
            print("error decode")
            pass
    
    time.sleep(0.1)