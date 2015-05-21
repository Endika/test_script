#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import smtplib
from email.mime.text import MIMEText

_CONF = {'SMTP': 'smtp.yourserver.com',
         'SMTP_PORT': 587,
         'USERNAME': 'your_username',
         'PASSWORD': 'your_password',
         'EMAIL_FROM': 'alert@example.com',
         'EMAIL_TO': 'mi@email.com',
         'SUBJECT': 'Aviso IP cambiada',
         'FILE_TMP': 'oldIP.tmp',
         }


def mail(mensaje):
        global _CONF
        mail_server = smtplib.SMTP(_CONF['SMTP'], _CONF['SMTP_PORT'])
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(_CONF['USERNAME'], _CONF['PASSWORD'])
        mensaje = MIMEText(str(mensaje))
        mensaje['From'] = _CONF['EMAIL_FROM']
        mensaje['To'] = _CONF['EMAIL_TO']
        mensaje['Subject'] = _CONF['SUBJECT']
        mail_server.sendmail(
            _CONF['EMAIL_FROM'], _CONF['EMAIL_TO'], mensaje.as_string())
        mail_server.close()


def leer():
    global _CONF
    contenido = ''
    try:
        f = open(_CONF['FILE_TMP'], 'r')
    except Exception:
        os.system('echo "000.000.000.000" > %s' % (_CONF['FILE_TMP']))
        f = open(_CONF['FILE_TMP'], 'r')
    while True:
        linea = f.readline()
        contenido = contenido + ' ' + linea
        if not linea:
            break
    f.close()
    return contenido


def main():
    global _CONF
    coint = 10
    newip = ''
    oldip = leer()
    while len(oldip) < 7 and coint > 0:
        oldip = leer()
        coint -= 1
    if coint == 0:
        oldip = "Error: corrupt file"

    coint = 10
    while len(newip) < 7 and coint > 0:
        os.system('dig +short myip.opendns.com @resolver1.opendns.com > %s'
                  % (_CONF['FILE_TMP']))
        # os.system("curl ifconfig.me > %s" % (_CONF['FILE_TMP']))
        newip = leer()
        coint -= 1
    if coint == 0:
        oldip = "Error: connect to opendns.com"
    print "Old IP: " + oldip
    if oldip != newip:
        print "New IP: " + newip
        print "send email..."
        mail("""
La IP a cambiado a %s.
La antigua IP era %s.
             """ % (newip, oldip))
    else:
        print "Is the same IP, no changes."
main()
