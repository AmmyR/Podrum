#!/usr/bin/env python3

import sys
from os import getcwd
from threading import Thread
from src.Podrum.Server import Server

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        if sys.argv[1] == "--no_wizard" and sys.argv[2] == "--travis":
                serverThread = Thread(target=Server, args=(getcwd(), False, True))
        else:
            print("[!] None valid args selected.")
            serverThread = Thread(target=Server, args=(getcwd(), True))
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--no_wizard":
                serverThread = Thread(target=Server, args=(getcwd(), False))
        else:
            print("[!] None valid args selected.")
            serverThread = Thread(target=Server, args=(getcwd(), True))
    else:
        serverThread = Thread(target=Server, args=(getcwd(), True))
    serverThread.start()
