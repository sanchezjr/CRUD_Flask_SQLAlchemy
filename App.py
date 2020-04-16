from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
 
 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    id_ct = db.Column(db.String(100))
    gateway = db.Column(db.String(100))
 
 
    def __init__(self, id_ct, gateway):
 
        self.id_ct = id_ct
        self.gateway = gateway
        #self.phone = phone
 
 
 
 
 
#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    all_data = Data.query.all()
 
    return render_template("index.html", employees = all_data)
 
 
 
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        id_ct = request.form['id_ct']
        gateway = request.form['gateway']
 
 
        my_data = Data(id_ct, gateway)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Registro insertado correctamente")
 
        return redirect(url_for('Index'))
 

 
#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.id_ct = request.form['id_ct']
        my_data.gateway = request.form['gateway']
        #my_data.phone = request.form['phone']
 
        db.session.commit()
        flash("Registro actualizado correctamente")
 
        return redirect(url_for('Index'))
 
 
 
 
#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Registro eliminado correctamente")
 
    return redirect(url_for('Index'))
 
 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)