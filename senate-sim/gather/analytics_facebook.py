import requests
import json
ACCESS_TOKEN = 'EAADsWaJuHxsBAMo9q135brbfEcrdpTdcBGrBOtrpzANH3qqIcMv8ZBXEgU25lzs4LcZC1tvb1fUH46Cgg2Bozfgjd4jdABeF0uEzZBVLAnVY4UCDexBdf2DTOWZBpsjvnLBB9RoSV6bKTZAWStmV8ehmsEuMIk0PZCHzxc30FIzgZDZD'

base_url = 'https://graph.facebook.com/me'

# Get 10 likes for 10 friends
fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN,)

# This API is HTTP-based and could be requested in the browser,
# with a command line utlity like curl, or using just about
# any programming language by making a request to the URL.
# Click the hyperlink that appears in your notebook output
# when you execute this code cell to see for yourself...
print(url)

# Interpret the response as JSON and convert back
# to Python data structures
content = requests.get(url).json()

# Pretty-print the JSON and display it
print(json.dumps(content, indent=1))