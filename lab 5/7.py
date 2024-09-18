# Using regular Expression

import re

text = "abc@gmail.com kiakehne@gmail.com zabardast@gmail.com ajeeb@gmail.com naakaro@gmail.com"

email_pattern = r"[a-zA-Z0-9.]+@[a-zA-Z0-9]+.[a-zA-Z]{1,}"

x = re.findall(email_pattern, text)

for email in x:
    print(email)
