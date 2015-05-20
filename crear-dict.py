#! /usr/bin/python
import os, sys

if len(sys.argv)<2:
    print "crear-dict.py <LANG>"
    sys.exit(0)	

LANG= sys.argv[1]
first=True
for LANG in sys.argv:
    if first:
        first=False
        continue
    print "Generando diccionario "+LANG
    os.system(" aspell --lang="+LANG+" dump master | aspell --lang="+LANG+" expand | tr ' ' '\n' >> dict.txt")
