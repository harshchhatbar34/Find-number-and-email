#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re,pyperclip

phonrragex = re.compile(r'''(
(\d{3}|\(\d{3}\))?       #area code
(\s|-|\.)?               #separator
(\d{3})                  #first 3 digit
(\s|-|\.)                #separator
(\d{4})                  #last 4 digits                    
(\s*(ext|x|ext.)\s*(\d{2,5}))?)''',re.VERBOSE)


# Creat email regex.
emailRagex = re.compile(r'''(
    [a-zA-Z0-9._+-]+       # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''',re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
#print(text)
matches = []
for groups in phonrragex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' +groups[8]
    matches.append(phoneNum)
for groups in emailRagex.findall(text):
    matches.append(groups[0])

for groups in emailRagex.findall(text):
    matches.append(groups[0])
    # Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
print(matches)
