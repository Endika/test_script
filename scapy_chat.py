#! /usr/bin/env python
import sys
import os
import textwrap
from pprint import pprint
from optparse import OptionParser
from datetime import datetime

try:
    from scapy.all import *
except ImportError:
    print 'run: sudo aptitude install python-scapy befor execute this script'

def doopts():
    program = os.path.basename(sys.argv[0])
    usg = """\
                usage: %s -h | [-p PORT] [-d IP]

          """
    usg = textwrap.dedent(usg) % program
    parser = OptionParser(usage=usg)

    parser.add_option('-p', '--port', dest='port',
                                        metavar='PORT', default=12345,
                                        help='Port to send your msg')

    parser.add_option('-d', '--dst', dest='dst',
                                        metavar='DST', default=None,
                                        help='IP to recive your msg')
    return parser

def prepareLen(options):
	ip=options.dst+":"+options.port
	while len(ip)<=15:
		ip+=" "
	text=str(datetime.now())+"\n\t"+ip
	return text

def waitToResponse(options):
	while True:
		try:
			p = sniff(count=1,filter="tcp and port "+str(options.port))
			if len(p)<=0:
				continue
			if not hasattr(p[0].getlayer(Raw), 'load'):
				continue
			if not hasattr(p[0].getlayer(IP), 'src'):
				continue
			rawLoad = p[0].getlayer(Raw).load
			ip=p[0].getlayer(IP).src
			print prepareLen(options)+" (NaN) => "+rawLoad
			break
		except Exception, e:
			raise

def sendPacket(options):
	while True:
		ipr=RandIP()
		mensaje = raw_input("%s (You) => " % prepareLen(options))
		pack=IP(src=ipr,dst=str(options.dst))/TCP(sport=RandShort(),dport=int(options.port),flags="S",seq=12345)/str(mensaje)
		send(pack, verbose=0)
		print "..."
		waitToResponse(options)

def validate(options):
	if not options.dst:
		print "--dst argument is not defined"
		exit(0)

def main():
	parser = doopts()
	(options, args) = parser.parse_args()
	validate(options)
	os.system("clear")
	print options
	sendPacket(options)

main()