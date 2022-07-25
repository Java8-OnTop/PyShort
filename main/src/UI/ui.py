from time import sleep

import os

import sys
import colorama
import socket
SysMon = True

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()
OGG = 0.6

print(f" OGG registrar: {OGG}")

from colorama import init, Fore, Back, Style init(convert=SysMon)

print(Fore.RED + 'FATAL ERROR')
print(Back.GREEN + 'retrying')
print(Style.DIM + 'connecting...')
print(Style.RESET_ALL)
print('SOCKET OPENED.)
