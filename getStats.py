# url library to actually get the data
# and the json library to format the data
# need time to run the loop everytime an update occurs
from urllib.request import urlopen
import json
import time
# the url for colibri stat is by default the value for the url variable.
# Unless specifically set the colibri
# statistics are updated every 5 seconds so this script can also 
# be run every 5 seconds or at a certain time interval as well.
url = "http://127.0.0.1:8080/colibri/stats"
response = urlopen(url)
# the response is the json data but we need it in a more useful format
# this line turns the data into a dictionary
jsonDict = json.loads(response.read())
print(jsonDict)
# count is how many time you would like the script 
# to get the statistics from Colibri
count = 3
while(count != 0):
    response = urlopen(url)
    jsonDict = json.loads(response.read())
    print(jsonDict)
    count -= 1
    # kept at 6 seconds since default stats refresh is 5 seconds
    time.sleep(6)


