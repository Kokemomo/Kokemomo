#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

__author__ = 'hiroki'

def send_mail(source, destination, message, subject):
    '''
    Send mail.
    :param source: Address of the source..
    :param destination: Address of the destination
    :param message: Message.
    :param subject: Subject
    :return:
    '''
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = source
    msg['To'] = destination
    server = smtplib.SMTP('localhost')
    server.sendmail(source, [destination], msg.as_string())
    server.quit()