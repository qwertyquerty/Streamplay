import json
import socket
import time
import re
try:
    import threading
except:
    import pip
    pip.main(["install","threading"])
    import threading
try:
    import keyboard
except:
    import pip
    pip.main(["install","keyboard"])
    import keyboard


dat = json.loads(open("config.json").read())
HOST = "irc.chat.twitch.tv" #don't change this
PORT = 6667 #don't change this
NICK = dat["channel"] #twitch username
PASS = dat["oauth"]   # your Twitch OAuth token, make sure to include the oauth: part
CHAN = "#"+dat["channel"] #twitch username with # at the start
keys =  dat["keys"] #list of allowed keys and times

def keypress(key):
    global keys
    keyboard.press(key)
    time.sleep(keys[key])
    keyboard.release(key)

def press(key):
    t = threading.Thread(target=keypress, args=(key,))
    t.start()

s = socket.socket()
s.settimeout(10000)

def pongloop():
    global s
    while 1:
        time.sleep(40)
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))

s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))
CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

t = threading.Thread(target=pongloop)
t.start()

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        message = CHAT_MSG.sub("", response)
        message = message.strip("\r\n")
        args = message.split()
        for arg in args:
            try:
                if arg in keys.keys():
                    press(arg)
                    print(username+": "+arg)

            except Exception as E:
                pass
