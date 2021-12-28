# CustomJitsiApplication
This repository contains all the development I did to the Jitsi Video calling application.

The jitsiClientAdd.py file is a script that when run takes in how many participants to add and a meeting name and using these arguments adds the given number of participants to the jitsi meeting.

The getStats.py file is a scrip that when run gets the Colibri stats from the Jitsi Videobridge every 6 seconds or a certain amount of iterations that can be adjusted in the script.

The jitsi-Media-Transform-mod directory contains the development and changes I did to the jitsi-media-transfrom module in order to set the bandwidth estimation to always be 2.5mbps.

The newJMT directory contains the development and changes I did to the jitsi-media-transform modules in order to implement the Dummy congestion control algorthim

The newJVB directory contains all the development and changes I did to the jitsi-videobridge repository and includes log statements which ensure the bandwidth estimation changes as required

The MLRESTAPI directory contains all the libaries and modules used in the Flask REST API in the requirements.txt file. The app.py file sets up the rest api and a post and get endpoint and the model itself and the basic training data. The test.py file is a file showing how to run a post and a get request to the REST API and how to print the responses. The REST API is build such that the post request will train the model and the get request will run the model. In order to actually start the REST API simple open a terminal or command line window in the MLRESTAPI directory and run the command "python3 app.py" in order to run the test.py file simply open another command line or terminal window in the same directory while the REST API is running and run the command "python3 test.py"