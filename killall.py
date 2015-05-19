#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import subprocess
import signal
import os
import sys
import getopt


def usage():
    print """
%s -p <process name>
version 0.1 by Endika Iglesias <me@endikaiglesias.com>
          """ % (sys.argv[0])
    sys.exit(2)

try:
    options, remainder = getopt.getopt(sys.argv[1:], 'n:p:h:tdx:d',
                                       ['name=', 'process='])
except getopt.GetoptError:
    usage()

process_name = None
test_mode = False
debug_mode = False

for opt, arg in options:
    if opt in ('-n', '--name', '-p', '--process'):
        process_name = arg
    elif opt in ('-t', '--test'):
        test_mode = True
    elif opt in ('-d', '--debug'):
        debug_mode = True
    else:
        usage()

if process_name is None:
    usage()

p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
out, err = p.communicate()
mypid = os.getpid()
find = False
count = 0
process_list = []

for line in out.splitlines():
        if process_name in line:
            pid = int(line.split(None, 1)[0])
            if mypid != pid:
                find = True
                count += 1
                process_list.append(line)
                if not test_mode:
                    os.kill(pid, signal.SIGKILL)

find = 'not' if not find else ''
test_mode = 'Test mode\n' if test_mode else ''
if debug_mode:
    for line in process_list:
        print line
print """
%s'%s' process %s found
%s process found and killed
          """ % (test_mode, process_name, find, count)
