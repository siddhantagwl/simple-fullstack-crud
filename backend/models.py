# contains DB models and how we interact with it

from config import db

# database Model represented as python class
class Contact(db.Model):

    # define different fields that this model will have
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def to_json(self):
        # takes all the columns above and converts them to python dict
        # and then convert to json to communicate with api
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }