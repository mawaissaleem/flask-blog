from flask  import Flask
app= Flask(__name__)

@app.route("/") # routing the below functions on the following endpoints.
def hello():
    return "hello world"
@app.route("/awais")
def awais():
    return "welcome to the first flask application!"

#this line is to start the server automatically
app.run(debug=True) # debug=true detects changes and do not need to restart the server again and again