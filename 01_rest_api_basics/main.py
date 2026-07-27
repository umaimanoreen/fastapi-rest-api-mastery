from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(200), nullable=False)


def to_dict(self):
    return {
        'id': self.id,
        'destination': self.destination,
        'country': self.country
    }


@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, World!'})


@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])


if __name__ == '__main__':
    app.run(debug=True)
