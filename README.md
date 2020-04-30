# youtube-media-bias
Python Version: 3.7

## General Set Up
**Install pymongo**

Reference for installing pymongo with terminal:
https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

Alternatively, you can install the package within the Pycharm IDE.

**Install mongoDB**

Reference for macOS: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

Reference for windows: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

## The following steps can be used create a single node system:
```
Note: My project file Strucutre looks like this:
youtube-media-bias
|_ _youtube.py
|- -wrangle.py
|- -dataset.json
```
**1. Start mongodb**
macOS: 
```
brew services start mongodb-community@4.2
````
**2. Start mongo**
```
mongo
```
**3. Navigate to project file**
```
cd 'youtube-media-bias'
```
**4. Populate database**

the following will create a db called youtube, and populates youtube.channel with documents in dataset.json
```
mongoimport --db youtube --collection channel --file dataset.json --jsonArray
```
**5. Test a query**
```
use youtube
db.channel.find({},{"snippet.title":1})
```
## Use the following to run the Python application
**1. Open your project folder in PyCharm and run youtube.py**

Observe the console in pycharm

