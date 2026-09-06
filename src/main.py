#!/usr/bin/env python3

import re
import json


# Read input
with open("input/raw-text.txt", "r") as file:
    text = file.read()


# 1. EMAILS
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
emails = re.findall(email_pattern, text)


# Check ALU email domains
alu_emails = []

for email in emails:
    if re.match(
        r"^[A-Za-z0-9._%+-]+@"
        r"(alueducation\.com|alumni\.alueducation\.com|"
        r"si\.alueducation\.com)$",
        email
    ):
        alu_emails.append(email)


# 2. CREDIT CARDS
card_pattern = r"\b(?:\d{4}[- ]?){3}\d{4}\b"
cards = re.findall(card_pattern, text)

# Mask credit card numbers
masked_cards = []

for card in cards:
    numbers = re.sub(r"[- ]", "", card)
    masked_cards.append(
        numbers[:4] + " **** **** " + numbers[-4:]
    )


# 3. PHONE NUMBERS
phone_pattern = r"(?:\+250[\s-]?|0)7\d{2}[\s-]?\d{3}[\s-]?\d{3}"
phones = re.findall(phone_pattern, text)


# 4. URLs
url_pattern = r"https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?"
urls = re.findall(url_pattern, text)


# Save results
results = {
    "emails": emails,
    "alu_emails": alu_emails,
    "credit_cards": masked_cards,
    "phone_numbers": phones,
    "urls": urls
}


with open("output/sample-output.json", "w") as file:
    json.dump(results, file, indent=4)


print("Data extraction completed successfully.")
print("Results saved to output/sample-output.json")
