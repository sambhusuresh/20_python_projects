import string
import random

def gen():
    s1 =  string.ascii_uppercase 
    #uppercase letters of A TO Z saved to s1
    #print(s1)
    s2 = string.ascii_lowercase 
    #lowercase letters of A TO Z saved to s2
    #print(s2)
    s3 =  string.digits 
    #0 TO 9 saved to s3
    #print(s3)
    s4 = string.punctuation
    #symbols saved to s4
    #print(s4)
    pl = 0 #password length
    pl = int(input("Enter the password length\n"))

    s = [] #array
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    #saving all letters/numericals into a single array 
    #print(s)
    random.shuffle(s) # randomizing the password
    #print(s)
    password = ("".join(s[0:pl])) #seting the number of digits of password
    print(password)


gen()
