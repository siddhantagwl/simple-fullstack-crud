# contains main routes and main endpoints
from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/")
def home():
    return "welcome to basic flask+react crud app"

# create end point: localhost:8080/create_contact
# we need firstname, lastname and email and submit data to server,
# so a post request
@app.route("/create_contact", methods=["POST"])
def create_contact():
    # get the contact first that was submitted
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    # validate if they exist or not
    if not first_name or not last_name or not email:
        return (jsonify({"message": "First Name, Last Name and email are mandatory"}), 400)
    
    # now we have valid fields and it can be passed to the DB class as constructor
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    # add to DB
    try:
        db.session.add(new_contact) # staging area, not really fully committed to DB yet
        db.session.commit() # actually written to DB
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    # 201 is response code for creating a new entry
    return jsonify({"message": f"User {first_name} created"}), 201


# read
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # uses flask SQLAlchemy ORM to get all the contacts stored inside the Contact DB
    contacts = Contact.query.all() # returns python obj
    # convert to json now
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    # note: status code 200 is by default included
    return jsonify({"contacts": json_contacts}, 200)

# update

# delete

# if we were to run main.py directly, it will run the code in if block
# reason is if we import the functions/variables of main.py into another code, the 
# if block wont be running thus protecting the code from execution
if __name__ == "__main__":

    # instantiate the DB
    # get the context of application
    with app.app_context():
        # create all the different models that we have defined in our DB
        db.create_all()

    # if the debug flag is set the server will automatically
    # reload for code changes and show a debugger 
    # in case an exception happened.
    app.run(debug=True)