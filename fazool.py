from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/shadow_coding'
#app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://username:password@server/db'  pattern to write above command
db = SQLAlchemy(app)

class Contact(db.Model):
    ''' name, phone_num, date, email '''

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.String(10), nullable=True)
    msg= db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/contact', methods=['GET', 'POST'])
def contact(name,email,phone,message):
 #   if (request.method=='POST'):

    name=name
    email=email
    phone=phone
    message=message

    entry= Contact(name=name, phone_num=phone, email=email, msg=message)
    db.session.add(entry)
    db.session.commit()

    #return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')


app.run(debug=True)

from tkinter import *
root = Tk()

def getvals():
    print("It works!")
    contact('abc','abcd@gmail.com', '34234','fhdsfbdks')
root.geometry("644x344")
#Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)



root.mainloop()
