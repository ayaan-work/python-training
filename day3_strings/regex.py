# A regular expression is a sequence of characters that defines a search pattern. It is used to find and manipulate strings based on specific patterns.
#youtube link: https://www.youtube.com/watch?v=sHw5hLYFaIw

import re
text = "Python is fun"
result=re.match(r"Python",text)   #re.match() Checks whether the beginning of the string matches the pattern.
print(result)
print(result.group()) #prints Python
#Key Point: match() only checks from index 0.

print("\n")

#re.search() checks for a match anywhere in the string.
text = "I love Python programming"
result = re.search(r"Python", text)
print(result.group())
print(result.start())
print(result.end())

print("\n")

text = "My marks are 90, 85, and 78."
numbers = re.findall(r"\d+", text)
print(numbers)

text = "cat bat rat mat"
words = re.findall(r"\w+at", text)
print(words)

#re.sub() replaces occurrences of a pattern with a specified string.
text = "I like Java"
new_text = re.sub(r"Java", "Python", text)
print(new_text)

text = "Python123"
print(re.sub(r"\d", "", text))

#re.split() splits a string into a list based on a specified pattern.
text = "apple,banana;orange mango"
result = re.split(r"[,; ]+", text)
print(result)

print("\n")

#groups 
text = "John 25"
match = re.search(r"(\w+)\s(\d+)", text)
print(match.group(1))
print(match.group(2))


text = "Alice 30"
match = re.search(r"(?P<name>\w+)\s(?P<age>\d+)", text)
print(match.group("name"))
print(match.group("age"))

print("\n")
#common regex patterns

text = "Price: 250 Rs"
print(re.findall(r"\d+", text))

text = "Contact: abc@gmail.com"
email = re.findall(r"\S+@\S+", text)
print(email)

text = "Python is easy"
print(re.findall(r"\w+", text))

text = "Python123"
print(re.findall(r"[A-Za-z]+", text))

text = "abc123xyz456"
print(re.findall(r"\d+", text))

print("\n")

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern = r'https://twitter\.com/[a-z_0-9]+' # todo: type your regex here
pattern1 = r'https://twitter\.com/([a-z_0-9]+)'

print(re.findall(pattern, text))
print(re.findall(pattern1, text))

print("\n")

text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern = r'Concentration of Risk:\s*([a-zA-Z]+)' # todo: type your regex here

print(re.findall(pattern, text))
