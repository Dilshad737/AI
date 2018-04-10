"""
Google GeoLocation API for Python v. 1.2
Coded by Kuba Siekierzynski 2016-2017

The code is a small demonstration on how to use Google API in Python for some geolocation fun :)

Added in v. 1.2:
- location_type, place_id
- Google Places API support (beta)

Added in v. 1.1:
- better formatting

"""

from urllib.request import urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML
# importing only the necessary for memory saving

api_url = 'http://maps.googleapis.com/maps/api/geocode/xml?'
# the location of Google's geolocation API

address = input('Enter location: ')
if len(address) < 1:
    address = "Warsaw, Poland"
    # if no address specified, try my home city :)
url = api_url + ENCODE({'sensor': 'false', 'address': address})
# putting the parts together in UTF-8 format
print ('\nRetrieving location for:', address)
data = OPEN(url).read()
# getting that data
# print ('Retrieved',len(data),'characters')
tree = XML.fromstring(data)
# digging into the XML tree

res = tree.findall('result')
# let's see the results now

lat = res[0].find('geometry').find('location').find('lat').text
# dig into the XML tree to find 'latitude'
lng = res[0].find('geometry').find('location').find('lng').text
# and longitude
lat = float(lat)
lng = float(lng)
if lat < 0:
    lat_c = chr(167)+'S'
else:
    lat_c = chr(167)+'N'
if lng < 0:
    lng_c = chr(167)+'W'
else:
    lng_c = chr(167)+'E'
# format the coordinates to a more appealing form

location = res[0].find('formatted_address').text
location_type = res[0].find('geometry').find('location_type').text
# location holds the geomap unit found by API, based on user input
place_id = res[0].find('place_id').text


# Time for the second part...
url = 'http://maps.googleapis.com/maps/api/place/details/xml?'
# the location of Google Places API
# will need a valid key for that 
# url = api_url + ENCODE({'placeid': place_id, 'key': ''})

data = OPEN(url).read()
tree = XML.fromstring(data)
res = tree.findall('status')[0].text
# rating = res[0].find('rating').text

print("\n==>", location, "<==")
print('Latitude: {0:.3f}{1}'.format(abs(lat), lat_c))
print('Longitude: {0:.3f}{1}'.format(abs(lng), lng_c))
print('Location type:', location_type)
print('Place ID:', place_id)
print('Rating:', res) # REQUEST_DENIED so far...

"""
There are many more interesting parameters in the XML tree returned by the Google API. Explore them and learn more on this at:
https://developers.google.com/maps/
                                        Happy coding!
"""
