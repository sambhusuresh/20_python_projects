import pyshorteners
url =  input("enter url:\n")

print("shortend url: " , pyshorteners.Shortener().tinyurl.short(url))

#install pyshortners