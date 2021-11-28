#import all python libaries needed to run this flask application
import flask
import json
import flask
from flask import request, jsonify
#from flask import Flask, render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = False

#Open the json file and assign it to data
with open('cars.json') as f:
  data = json.load(f)

#Returns to Home when you hit the local host url 
@app.route('/', methods=['GET'])
def home():
    return flask.render_template('home.html')

#This returns all the json data when you enter '/api/cars/data/all' in front of the local host url
@app.route('/api/cars/data/all', methods=['GET'])
def api_all():
    return flask.jsonify(data)

def if_name_in_request(args: dict):
    if "Name" in args:
        return str(args["Name"])
    else:
        return "Error: No name field provided. Please specify a name."

#This returns the json data when you enter a specific car name after /api/cars/data/'
@app.route('/api/cars/data/', methods=['GET'])
def api_name():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    name = if_name_in_request(request.args)
    # if "Name" in flask.request.args:
    #     name = str(flask.request.args["Name"])
    # else:
    #     return "Error: No name field provided. Please specify a name."

    # Create an empty list for your results
    results = []
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for car in data:
        if car['Name'] == name:
            results.append(car)

    # Use the jsonify function from Flask to convert your list of
    # Python dictionaries to the JSON format.
    return flask.jsonify(results)

#Specifying the rouute for the search
@app.route('/api/cars/data/search', methods=['GET', 'POST'])
def api_search():

#Checks if method is POST
#Runs the for loop and check if the search item matches Json content name

    if request.method == "POST":
        results = []
        for car in data:
            print(car['Name'])
#If statement below checks if the value in the search box matches any of the car names in data
#If there's a match, the name is then appended to the attributes of the car name in data
            if car['Name'] == request.values.get("search"):
                fname = request.values.get("search")
                print(fname)
                results.append(car)    
    if results:
        return flask.jsonify(results)

    else:
        return "Error: Please specify a correct car name." 

if __name__ == "__main__":
    app.run(host='0.0.0.0')