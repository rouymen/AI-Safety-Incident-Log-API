from flask import Flask, request, jsonify, abort
from models import db, Incident
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# 👇 Create tables when app starts
with app.app_context():
    db.create_all()

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    print("incidents",incidents)
    return jsonify([incident.to_dict() for incident in incidents]), 200

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'description', 'severity')):
        return jsonify({'error': 'Missing required fields'}), 400
    if data['severity'] not in ('Low', 'Medium', 'High'):
        return jsonify({'error': 'Invalid severity level'}), 400

    incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )
    db.session.add(incident)
    db.session.commit()
    return jsonify(incident.to_dict()), 201

@app.route('/incidents/<int:incident_id>', methods=['GET'])
def get_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        abort(404)
    return jsonify(incident.to_dict()), 200

@app.route('/incidents/<int:incident_id>', methods=['DELETE'])
def delete_incident(incident_id):
    incident = Incident.query.get(incident_id)
    if not incident:
        abort(404)
    db.session.delete(incident)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)


