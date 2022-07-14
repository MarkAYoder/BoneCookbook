#!/usr/bin/env python
# From: 
import smtplib, ssl

port = 587  # For starttls
smtp_server    = "smtp.gmail.com"
sender_email   = "mark.a.yoder@gmail.com"
receiver_email = "mark.a.yoder@rose-hulman.edu"
# Go to: https://myaccount.google.com/security
# Select App password
# Generate your own 16 char password, copy here
# Delete password when done
password = "cftqhcejjdjfdwjh"
message = """\
Subject: Hi there 4

This message is sent from Python.

"""
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
