from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
import datetime
import os
from werkzeug.utils import secure_filename
import math
from flask_mail import Mail

local_server = True
with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
app.config['UPLOAD_FOLDER']='static'
# app.config.update(
#     MAIL_SERVER= 'smtp.gmail.com',
#     MAIL_PORT= '465',
#     MAIL_USE_SSL= True,
#     MAIL_USERNAME= params['gmail_user'],
#     MAIL_PASSWORD= params['gmail_password']
# )
# mail=Mail(app)

if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://username:password@server/db'  pattern to write above command
else:
    app.config['SQLACHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)


class Contact(db.Model):
    ''' name, phone_num, date, email '''

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.String(10), nullable=True)
    msg = db.Column(db.String(50), nullable=False)


class Post(db.Model):
    ''' name, phone_num, date, email '''

    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String(12), nullable=False)
    content = db.Column(db.String(500), unique=False, nullable=False)
    date = db.Column(db.String(10), nullable=True)
    img_file = db.Column(db.String(20), nullable=False)


@app.route('/')
def home():
#    posts_preview = Post.query.filter_by().all()[0:params['post_per_page']]
 #   return render_template('index.html', params=params, posts=posts_preview)
    posts = Post.query.filter_by().all()
    last = math.ceil(len(posts) / int(params['post_per_page']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page - 1) * int(params['post_per_page']):(page - 1) * int(params['post_per_page']) + int(params['post_per_page'])]
    if page == 1:
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif page == last:
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contact(name=name, phone_num=phone, email=email, msg=message)
        db.session.add(entry)
        db.session.commit()
        # mail.send_message('new message from' + name,
        #     sender= email,
        #     recipients=[params['gmail_user']],
        #     body=message + "\n" + phone
        # )

    return render_template('contact.html', params=params)


@app.route('/about')
def about():
    return render_template('about.html', params=params)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user'] == params['admin_username']:
        posts = Post.query.all()
        return render_template('adminpanel.html', params=params, posts=posts)

    if request.method == 'POST':
        admin_username = request.form.get('username')
        admin_password = request.form.get('password')
        if admin_password == params['admin_password'] and admin_username == params['admin_username']:
            session['user'] = admin_username
            posts = Post.query.all()
            return render_template('adminpanel.html', params=params, posts=posts)
    # redirect to admin panel
    else:
        return render_template('login.html', params=params)


@app.route('/edit/<string:sno>', methods=['GET', 'POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_username']:
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.datetime.now()

            print("inside post")
            if (sno =="0"):
                post = Post(title=title, slug=slug, content=content, img_file=img_file, date=date)
                #print(post)
                db.session.add(post)
                db.session.commit()
#                sno='1'
                #post = Post.query.filter_by(sno=0).first()
                #return redirect('/edit/' + sno)
#                return render_template('edit.html', params=params, post=post)
            else:
                post = Post.query.filter_by(sno=sno).first()
                print(type(sno))
                post.title = title
                post.date = date
                post.slug = slug
                post.content = content
                post.img_file = img_file
                db.session.commit()

                #post = Post.query.filter_by(sno=sno).first()
                return redirect('/edit/'+sno)

    print("before post")
 #   post = Post.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, sno=sno)



@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    blog_post = Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, blog_post=blog_post)

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_username']:
        if request.method=="POST":
            uploaded_file=request.files['myfile']
            uploaded_file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),  app.config['UPLOAD_FOLDER'], secure_filename(uploaded_file.filename)))
            return "file uploaded succesfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/delete/<string:sno>", methods=['GET','POST'])
def delete(sno):
    if 'user' in session and session['user']==params['admin_username']:
        post = Post.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    else:
        return redirect('/dashboard')
    return redirect('/dashboard')


app.run(debug=True)
