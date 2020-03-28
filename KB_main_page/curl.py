import requests

params = (
    ('url', 'https://twitter.com/Interior/status/507185938620219395'),
)

response = requests.get('https://publish.twitter.com/oembed', params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://publish.twitter.com/oembed?url=https%3A%2F%2Ftwitter.com%2FInterior%2Fstatus%2F507185938620219395')


print(response.content)