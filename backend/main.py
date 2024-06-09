# contains main routes and main endpoints
from flask import request, jsonify
from config import app, db
from models import Contact

# create end point: localhost:8080/create_contact
# we need firstname, lastname and email and submit data to server,
# so a post request


# read

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