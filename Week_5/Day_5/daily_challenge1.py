# Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

# requests.get("http://127.0.0.1").elapsed.total_seconds()


import requests 
  
# Making a get request 
response1 = requests.get('http://google.com/') 
response2 = requests.get('http://yahoo.com/') 
response3 = requests.get('http://stackoverflow.com/') 
   
  
# print elapsed time 
print(response1.elapsed.total_seconds())
print(response2.elapsed.total_seconds())
print(response3.elapsed.total_seconds())

# requests.get("http://ynet").elapsed.total_seconds()