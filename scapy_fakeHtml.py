#! /usr/bin/env python
import sys
import os
import textwrap
from pprint import pprint
from optparse import OptionParser
from datetime import datetime

try:
    import logging
    l=logging.getLogger("scapy.runtime")
    l.setLevel(49)
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
                                        metavar='PORT', default=80,
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

def sendPacket(p,options):
	#p.show()

	if p[IP].dst==options.dst:
		#print p[IP].dst
		if p.haslayer('Raw'):
			print p.getlayer(Raw).load
			#print p['Raw'].load.find("<html")
			#print p['Raw'].load
			if p['Raw'].load.find("<html")>0:
				if p['Raw'].load.find("<img src='http://imagenes.es.sftcdn.net/es/scrn/69000/69838/python-20.jpg'></body>")<0:
					print p['Raw'].load
					print p['Raw'].load.replace("</body>", "<img src='http://imagenes.es.sftcdn.net/es/scrn/69000/69838/python-20.jpg'></body>");
			#p['Raw'].load="HOlaaa"
					sendp(p)
	"""
	if p.getlayer(IP).dst != options.dst:
		return False
	print p.getlayer(IP).src
	print p.getlayer(IP).dst
	print p.getlayer(Raw).load
	"""
	#pack=IP(src=p.getlayer(IP).src,dst=p.getlayer(IP).dst)/TCP(sport=RandShort(),dport=int(options.port),flags="S",seq=12345)/str("HOLAAAA")
	#send(pack, verbose=0)
	#send(pack, verbose=0)
	#return True

def waitToResponse(options):
	#while True:
	try:
		sniff(filter="tcp and port "+str(options.port),prn=lambda x:sendPacket(x,options))
		"""
			if len(p)<=0:
				continue
			if not hasattr(p[0].getlayer(Raw), 'load'):
				continue
			if not hasattr(p[0].getlayer(IP), 'src'):
				continue
			#rawLoad = p[0].getlayer(Raw).load
			#ip=p[0].getlayer(IP).src
			#print prepareLen(options)+" (NaN) => "+rawLoad
			return p[0]
		"""
	except Exception, e:
		raise

def validate(options):
	if not options.dst:
		print "--dst argument is not defined"
		exit(0)

def main():
	parser = doopts()
	(options, args) = parser.parse_args()
	validate(options)
	os.system("clear")
	#while True:
	print "..."
	p=waitToResponse(options)
	"""
		if p.getlayer(IP).dst == options.dst:
			print "Capturado"
			if sendPacket(p,options):
				print "Enviado"
	"""
main()
