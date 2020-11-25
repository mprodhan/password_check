import requests
# the most common library used in any code involving apis.
import hashlib

# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'

# the url variable takes the api plus the hashed password.
# Hashed passwords are one way and the output anonymizes the users password.
# If the password is modified, the hash is modified each time the password is changed.

# res = requests.get(url)
# print(res)

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again!')
    return res
def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

request_api_data('41810')