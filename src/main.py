#!/usr/bin/env python3

import re
with open("input/raw-text.txt", "r") as file:
    text= file.read()
    pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails=re.findall(pattern,text)
    alu_emails=[]
    print("Emails are:", emails)
     for email in emails:
       if re.match( r"^[a-zA-Z0-9._%+-]+@(alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)$",email):
           alu_emails.append(email)
    print("ALU emails are:", alu_emails)
