print("Module: Regular expressions")
import re

patterns = ["term1","term2"]

text = "This is a string with term1, But not the other!"

# for pattern in patterns:
#     print("I am searching for pattern: " + pattern)

#     if re.search(pattern,text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

# #Ideal way to search for matches

# match = re.search("term1",text)
# print(match.start()) #Gives the position of the matched pattern

# #Split
# email = "user@gmail.com"
# split_term="@"
# split_string = email.split(split_term)
# print(split_string)
# # print(re.split(split_term,email))

# #findall - Finds all the matches
# text1 = "The text matches at times, Sometimes matches twice."
# print(re.findall("match",text1))

#Multi_re_find

def multi_re_find(patterns,phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")


test_phrase = 'sdsd..ssddd.sdddsddd...dsds...dssssss...sddddd'

# test_patterns = ['sd+']
# test_patterns = ['sd{2,3}'] #s followed by 2 or 3d's/
# test_phrase2 = "This is a string! But is has punctuation. How can we remove it?"
# test_patterns = ['[^!.?]+'] #The special characters specified after ^ symbol ("!.?") will be removed and the rest of the string will be returned.
test_phrase3 = "This is a string with numbers 12312 and a symbol #hashtag"
# test_patterns = ['[A-Z]+'] #Sequences of uppercase characters.
test_patterns = [r'\d+'] #Digits

multi_re_find(test_patterns,test_phrase3)