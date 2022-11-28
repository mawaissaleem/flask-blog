from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def hello():
    firstName="awais"
    return render_template("index.html" , name= firstName) # name is passed to the index.html file while firstName is vaiable in python file.

app.run(debug=True)
