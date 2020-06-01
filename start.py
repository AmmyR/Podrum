#!/usr/bin/env python3

import sys
from os import getcwd
from threading import Thread
from src.Podrum.Server import Server

if __name__ == "__main__":
    if(sys.argv[1] == "--no_wizard"):
        serverThread = Thread(target=Server, args=(getcwd(), False))
    else:
        serverThread = Thread(target=Server, args=(getcwd(), True))
    serverThread.start()
