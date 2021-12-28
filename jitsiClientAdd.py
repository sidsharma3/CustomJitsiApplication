#!/usr/bin/python
import webbrowser
import sys

argList = sys.argv
# sample use case: python jitsiClientAdd.py 3 https://meet.example.com EasyAppreciationsInterFiercely
# check parameters
if len(argList) != 4:
    print("Invalid Number of Arguments")
elif argList[1].isdigit() == False:
    print("Invalid Number of Clients to add")
elif argList[2].isdigit() == True:
    print("Invalid Jitsi Server URL")
elif argList[3].isdigit() == True:
    print("Invalid Meeting Time")
else:
    # Create the correct server url
    # https must be used otherwise disconnection error occurs
    serverName = ""
    if argList[2][0:8] == "https://":
        serverName = argList[2]
    elif argList[2][0:7] == "http://":
        serverName = "https://" + argList[2][7:]
    else:
        serverName = "https://" + argList[2]
    # Loop through number of clients to be added
    # Make sure that jitsi server prevent join page
    # If join page prevented then opening url will not add client to the meeting
    clients = int(argList[1])

    meetingUrl = argList[2] + "/" + argList[3]

    for i in range(0, clients, 1):
        print("3")
        webbrowser.open(meetingUrl)
