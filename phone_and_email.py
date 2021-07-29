#! python
# phone_and_email.py - Finds phone numbers and email adresses on the clipboard.

import pyperclip
import re

# Create phone regex
phone_regex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # sperator 
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # sperator
    (\d{4})                         # first 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)""", re.VERBOSE)

# Create email regex
email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something                                
)""", re.VERBOSE)

# TODO: Find matches in clipboard text.

# TODO: Copy results to the clipboard.
