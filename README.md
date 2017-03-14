# Resize photos – SkyHub challenge

Consume a webservice endpoint (http://54.152.221.29/images.json) that returns a JSON of
photos. There are 10 photos.

• Generate three different formats for each photo. The dimensions are: small (320x240),
medium (384x288) and large (640x480).

• Write a webservice endpoint that lists (in JSON format) all the ten photos with their
respective formats, providing their URLs.



##Running

You need Python 3.5 or higher in order to run this script and a MongoDB server running (check instructions on <https://docs.mongodb.com/manual/installation/>)

You will also need to download some dependecies

Open terminal and run the following commands:

```
pip install pymongo
pip install flask

```

Then start the application

```
python app.py
```

Open <http://127.0.0.1:5000> when the app is up and running

##Running tests

Open terminal and run the following command:

```
python -m unittest -v TestSkyHub

```

##Why Python (and flask)

First of all I'm trying to improve my Python skills since my current main language (the one I use everyday in my job) is Java.
Besides that, I've never done anything web-related using Python until now. I chose Flask because it's a very simple framework that allowed me to write a solution for this challenge in just few lines of code (179 lines including tests).



