#!/usr/bin/env python3

import re
with open("input/raw-text.txt", "r") as file:
    text= file.read()
    pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails=re.findall(pattern,text)
    print(emails)
    
