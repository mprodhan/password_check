import requests
# the most common library used in any code involving apis.

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
# the url variable takes the api plus the hashed password.
# Hashed passwords are one way and the output anonymizes the users password.
# If the password is modified, the hash is modified each time the password is changed.
res = requests.get(url)
print(res)