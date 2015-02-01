#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

# Config AREA =======================================================
# WebSite AREA ======================================================
websites = {'TITLE WEBSITE 01': 'http://website01.com',
            'TITLE WEBSITE 02': 'http://website02.com',
            }
# Server AREA =======================================================
conf = {"SMTP": "smtp.server.com",
        "SMTP_PORT": "587",
        "SMTP_USER": "user@server.com",
        "SMTP_PASS": "password",
        "EMAIL_DESTINO": "user@server.com",
        "EMAIL_ORIGEN": "user@server.com",
        "ASUNTO": "Alert Website",
        "LOG_FILE": "/var/log/websites_status.log"
        }
# ===================================================================
# ===================================================================


def _registrar(texto):
    if 'LOG_FILE' in conf.keys():
        fm = open(conf["LOG_FILE"], "a")
        fm.write(texto)
        fm.close()
        return True
    return False


def _send_mail(mensaje, email=conf['EMAIL_DESTINO']):
    if 'SMTP' in conf.keys() and \
       'SMTP_PORT' in conf.keys() and \
       'SMTP_USER' in conf.keys() and \
       'SMTP_PASS' in conf.keys() and \
       'EMAIL_ORIGEN' in conf.keys() and \
       'ASUNTO' in conf.keys():

        mailServer = smtplib.SMTP(conf['SMTP'], conf['SMTP_PORT'])
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(conf['SMTP_USER'], conf['SMTP_PASS'])
        mensaje = MIMEText(str(mensaje), 'html')
        mensaje['From'] = conf['EMAIL_ORIGEN']
        mensaje['To'] = email
        mensaje['Subject'] = conf['ASUNTO']
        mailServer.sendmail(conf['EMAIL_ORIGEN'],
                            email,
                            mensaje.as_string())
        mailServer.close()
        return True
    return False

display = Display(visible=0, size=(800, 600))
display.start()
msg = "<html><head></head><body>"
send = False
for web in websites:
    img = ""
    try:
        browser = webdriver.Firefox()
        browser.get(websites[web])
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "ON"
        if web not in browser.title:
            status = "OFF"
            send = True
            base64 = browser.get_screenshot_as_base64()
            img = '<br/><img src="data:image/png;base64,' + base64 + '" />'
        text = date + " " + status + " " + web + " " + websites[web]
        msg += "<p>" + text + img + "</p>"
        print text
        _registrar(msg)
        browser.close()
    except Exception, e:
        browser.close()

if send:
    msg += "</body></html>"
    _send_mail(msg)
