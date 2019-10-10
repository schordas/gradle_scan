#!/usr/bin/python
import sys
import re

def scan_line(line):
    matches = []
    matches.append(re.match(r'.*Exec.*$', line, re.M|re.I))
    matches.append(re.match(r'.*exec.*$', line, re.M|re.I))
    matches.append(re.match(r'.*commandLine.*$', line, re.M|re.I))
    matches.append(re.match(r'.*\.\/sh.*$', line, re.M|re.I))
    matches.append(re.match(r'.*\.py.*$', line, re.M|re.I))
    matches.append(re.match(r'.*python.*$', line, re.M|re.I))
    matches.append(re.match(r'.*\.go', line, re.M|re.I))
    matches.append(re.match(r'.*args.*$', line, re.M|re.I))

    for match in matches:
        if match:
            return True

def sanitize(arg):
    return re.match(r'.*\.gradle$', arg, re.M|re.I)

def open_file(arg):
    input_file = open(arg)

    i = 0

    for line in input_file:
        if scan_line(line) == True:
            i += 1
            print ('##############')
            print ('WARNING: suspicious line found in ' + arg + '\n')
            print ('line in question:\n')
            print ('line ' + str(i) + ' ' + line)
            print ('##############\n')


def parse_input():
    sys.argv.pop(0)
    for arg in sys.argv:
        if sanitize(arg):
            print (arg + " is a valid file\n")
            print ('Scanning for suspicious content...\n')
        else:
            print (arg + ': is an INVALID file name\n')
            continue
        open_file(arg)

parse_input()