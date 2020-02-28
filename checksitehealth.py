#!/usr/bin/env python
import requests
from collections import namedtuple
import smtplib, ssl

WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
#names = ['www.aseanip', 'bar']
names = ['http://ipsearch.aseanip.org/', 'https://realpython.com/python-send-email/','https://www3.wipo.int/caseportal']
custvar=""


def sendemail(port = 587, smtp_server = "smtp.gmail.com", sender_email = "my@gmail.com", receiver_email = "your@gmail.com"):
    #port = 587  # For starttls
    #smtp_server = "smtp.gmail.com"
    #sender_email = "my@gmail.com"
    #receiver_email = "your@gmail.com"
    print("port:{}, smtp_server:{}, sender_email:{}, receiver_email:{}".format(port, smtp_server, sender_email, receiver_email))
    password = input("Type your password and press enter:")
    message = """\
       Subject: Hi there
       
       This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message) 

def get_status(site):
    try:
        response = requests.head(site, timeout=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = WebsiteStatus(status_code, reason)
    return website_status

for name in names:
    #site = 'https://{}.org'.format(name)
    #website_status = get_status(site)
    website_status = get_status(name)
    #print("{0:30} {1:10} {2:10}".format(site, website_status.status_code, website_status.reason))
    print("{0:30} {1:10} {2:10}".format(name, website_status.status_code, website_status.reason))
    if website_status.status_code == 200:
        #sendemail()
        print("good")
        #test()
    else:
        print("bad")




