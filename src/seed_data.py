from app import db
from models import Incident

incident1 = Incident(title='Bias detected', description='AI showed racial bias in hiring decisions.', severity='High')
incident2 = Incident(title='False claim by AI', description='AI chatbot gave wrong health advice.', severity='Medium')

db.session.add_all([incident1, incident2])
db.session.commit()
print("Sample incidents added.")
