text = "The agent's phone number is 408-555-1234. Call soon!"

import re

pattern2 = 'NOT IN TEXT'
print(re.search(pattern2, text))

pattern = 'phone'
# Search only finds the first match
match = re.search(pattern, text)
print(match)

print(match.span())
print(match.start())
print(match.end())

text2 = 'phone once, phone twice.'

# findall finds all matches
matches = re.findall('phone', text2)
print(matches)

# to get back match objects we use the iterator
for match in re.finditer('phone', text2):
    print(match)
    print(match.span())
    # group returns text that matched
    print(match.group())