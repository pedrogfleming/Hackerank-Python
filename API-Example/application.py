from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import jsonpickle
import jsonpatch

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello!'


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name':drink.name, 'description':drink.description}
        output.append(drink_data)
    return {"drinks": output }


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name":drink.name, "description": drink.description}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "yeet!@"}
@app.route("/drinks/<id>", methods=["PUT"])
def update_drink(id):
    drink = Drink.query.get(id)
    description = request.json['description']
    name = request.json['name']
    drink.name = name
    drink.description = description
    db.session.commit()
    return jsonpickle.encode(drink)
@app.route("/drinks/<id>",methods=["PATCH"])
def patch_drink(id):
    drink = Drink.query.get(id)
    patch = jsonpatch.JsonPatch(request.json)
    res = jsonpatch.apply_patch(drink, patch)
    db.session.commit()
    # return jsonpickle.encode(result)
    return jsonpickle.encode(res)