from flask import *
import password_registration_checker 

app = Flask(__name__, template_folder="../../../frontend/test")

# TODO: Needs modifying so that data when password is successful gets entered into the dummy db
@app.route("/", methods=["GET", "POST"])
def registration(): 
    errors = []
    if request.method == "POST":
        # Get the information from the form
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Pass the form values onto the py variables
        password_registration_checker.username = username
        password_registration_checker.email = email
        password_registration_checker.password = password
        password_registration_checker.final_error_output = []
        # Runs the main function
        errors = password_registration_checker.main(password_registration_checker.functions)
    # NOTE: The file will need updating when we make the real HTML
    return render_template("register.html", errors=errors)

# NOTE: Apparently flask needs to be run this way - I'll let you toy around with it if you want
if __name__ == "__main__":
    # Default port was having issues
    app.run(debug=True, port=8000)