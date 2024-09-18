# Using regular Expression

import re

text = "12/09/2023 2023-09-12 Sep 12,2023 2022-08-15 August 15,2021 Sep 12,2023"

extract_dates = r"\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|[A-Za-z]{3,} \d{1,2},\d{4})\b"

x = re.findall(extract_dates, text)

for date in x:
    print(date)
