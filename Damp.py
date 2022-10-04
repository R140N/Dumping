import os, sys
try:
    __import__("c").Menu()
except Exception as e:
    exit(str(e))
