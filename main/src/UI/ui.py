from time import sleep

import os

import sys

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()
OGG = 0.6

print(f" OGG registrar: {OGG}")
