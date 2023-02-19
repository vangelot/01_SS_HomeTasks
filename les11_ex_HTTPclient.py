import http.client
import pprint

connection = http.client.HTTPSConnection("www.youtube.com")
connection.request("GET", "/")
response = connection.getresponse()
headers = response.getheader('')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Headers: {}".format(headers))

