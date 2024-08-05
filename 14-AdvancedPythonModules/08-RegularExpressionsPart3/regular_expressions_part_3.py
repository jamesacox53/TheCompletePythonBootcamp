import re

match1 = re.search(r'cat|dog', 'The cat is here')
print(match1)

match2 = re.search(r'cat|dog', 'The dog is here')
print(match2)

matches1 = re.findall(r'.at', 'The cat in the hat sat there')
print(matches1)

matches2 = re.findall(r'^\d', '1 is a number')
print(matches2)

matches3 = re.findall(r'^\d', 'The 2 is a number')
print(matches3)

matches4 = re.findall(r'\d$', 'A number is 5')
print(matches4)

phrase = "There are 3 numbers 34 inside 5 this sentence"
# exclude all numbers and whitespace
no_numbers_pattern = r'[^\d\s]+'

matches5 = re.findall(no_numbers_pattern, phrase)
print(matches5)
print(' '.join(matches5))

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
clean = re.findall(r'[^!.? ]+', test_phrase)
print(clean)
print(' '.join(clean))

text = "Only find the hypen-words in this sentence. But you don not know how long-ish they are."
hypen_pattern = r'[\w]+-[\w]+'
hypen_words = re.findall(hypen_pattern, text)
print(hypen_words)

text1 = "Hello, would you like some catfish?"
text2 = "Hello, would you like to take a catnap?"
text3 = "Hello, have you seen this caterpillar?"

match6 = re.search(r'cat(fish|nap|claw)', text1)
print(match6)
match7 = re.search(r'cat(fish|nap|claw)', text2)
print(match7)
match8 = re.search(r'cat(fish|nap|claw)', text3)
print(match8)