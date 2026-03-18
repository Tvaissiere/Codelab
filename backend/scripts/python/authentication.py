# NOTE: Apologies, the naming is getting confusing becuase python and db are both using username email and password
# TODO: Update python naming
from flask import *
import password_registration_checker 
from connection import connection_details
import psycopg2

app = Flask(__name__, template_folder="../../../frontend/test")

# TODO: Make the function check wether an existing email is already present in the db, then append to errors = []
# TODO: Passwords need to hash
@app.route("/", methods=["GET", "POST"])
def registration(): 
    errors = []
    if request.method == "POST":
        # Get the information from the form
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check they entered a valid email
        # TODO: Disable the defualt browser error checking so we can test if this works- better to keep errors consistant   
        if "@" not in str(email):
            errors.append("Sorry, you need to enter a valid email address")

        # Pass the form values onto the py variables
        password_registration_checker.username = username
        password_registration_checker.email = email
        password_registration_checker.password = password
        password_registration_checker.final_error_output = []

        # Runs the main function
        errors = password_registration_checker.main(password_registration_checker.functions)
        if not errors:
            # FIXME: Not sure that this needs to be written this way, need to be tested and then shortened
            registration_data = {
                "username": username,
                "email": email,
                "password": password
            }

            duplication_check = "SELECT 1 FROM users WHERE username = %(username)s LIMIT 1"
            registration_query = "INSERT INTO users (username, email, password_hash) VALUES (%(username)s, %(email)s, %(password)s)"


            with psycopg2.connect(**connection_details) as conn:
                with conn.cursor() as cur:
                    cur.execute(duplication_check, {"username": username})
                    conn.commit()
                    duplication_check_answr = cur.fetchone()
                    if duplication_check_answr:
                        errors.append("Sorry this username already exists")
                        return render_template("register.html", errors=errors)
                    cur.execute(registration_query, registration_data)
                    conn.commit()
                    print("info: successfully added")
        else:
            return render_template("register.html", errors=errors)

    return render_template("register.html", errors=errors)


# NOTE: Apparently flask needs to be run this way - I'll let you toy around with it if you want
if __name__ == "__main__":
    # Default port was having issues
    app.run(debug=True, port=8000)