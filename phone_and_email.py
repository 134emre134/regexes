#! python
# phone_and_email.py - Finds phone numbers and email adresses on the clipboard.

import pyperclip
import re

phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?          # area code
    (\s|-|\.)?                  # sperator 
    (\d{3})                     # first 3 digits
    (\s|-|\.)                  # sperator
    (\d{4})                     # first 4 digits
)""", re.VERBOSE)
