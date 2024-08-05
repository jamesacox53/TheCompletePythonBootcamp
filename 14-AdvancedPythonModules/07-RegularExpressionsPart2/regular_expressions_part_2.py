import re

text = 'My phone number is 408-555-1234'

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print(phone.group())

phone2 = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone2.group())

# This is the same regular expression as above but uses
# grouping. A group is in (). Python understands that
# the three () are spearate groups but they are part
# of the same pattern.
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
# get first group (the area code). Here we start indexing
# at 1.
print(results.group(1))

# group with no number returns the whole match
print(results.group())