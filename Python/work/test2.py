import sys, os

filename = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test.txt"
filename2 = "C:\\Users\\dalec\\Desktop\\Code\\python\\test\\test_ppt_old.ppt"
# filepath2 = "C:/Users/dalec/Desktop/Code/python/test/test_ppt_old.ppt"
# print("Hello")
# import io

import re 
  
def Find(string): 
  
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 
      
# Driver Code 
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
print("Urls: ", Find(string)) 

links = []
with open(filename2, 'r', encoding='ansi') as f:
    text = f.read().split(" ")
    for i in text:
        links.append(Find(i))
# process Unicode text
# with io.open(filename, 'w', encoding='utf8') as f:
#     f.write(text)

print(links)