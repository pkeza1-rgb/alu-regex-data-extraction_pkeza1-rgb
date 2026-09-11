#!/usr/bin/env python3
#Import regex and json libraries

import re
import json

# Read the input file

with open("input/raw-text.txt", "r") as file:
    text = file.read()

# Extract Email addresses

    pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails=re.findall(pattern,text)
    print("Emails are:", emails)

# Extract and validate ALU Emails

    alu_emails=[]
    for email in emails:
       if re.match( r"^[a-zA-Z0-9._%+-]+@(alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)$",email):
           alu_emails.append(email)
    print("ALU emails are:", alu_emails)

# Extract and mask credit card numbers

    card_pattern=r"\b(?:\d{4}[- ]?){3}\d{4}\b"
    card=re.findall(card_pattern,text)
    m_card=[]
    for c in card:
        good_card=re.sub(r"[- ]","",c)
        mask=good_card[:4] + " **** **** " + good_card[-4:]
        m_card.append(mask)
    print("The credit card numbers are:", m_card)

# Extract phone numbers

    t_pattern=r"(?:\+250[\s-]?|0)7\d{2}[\s-]?\d{3}[\s-]?\d{3}"
    tel=re.findall(t_pattern, text)
    print("The phone numbers are:", tel)

# Extract URLs

    u_pattern=r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"
    url=re.findall(u_pattern, text)
    print("The URLs are:", url)

# Store and save results as JSON

    results={
        "Emails": emails,
        "ALU_Emails": alu_emails,
        "Credit_Cards_Numbers": m_card,
        "Phone_Numbers": tel,
        "URLs": url
    }
    with open("output/sample-output.json", "w") as file:
        json.dump(results, file, indent=4)
