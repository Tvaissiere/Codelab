# TODO: Write script which will ensure the users entered password meets the specified criteria (from the password policy)

# Static Variables
org_name = "codelab"
# TODO: Add anymore special chars you want to allow
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*"]
""" TODO: When you add a function, if it hits an error, 
write the error in the array then call the array and specific array placement of the corresponding error """
errors = ["Passwords must contain at least 12 characters.","Passwords cannot exceed 128 characters", "Password must contain at least one special character (e.g. ! @ # $ % ^ & *)", "Password must contain at least one upper case character", "Password must contain at least one lower case character", "Password must contain at least one number"] 

# Initialised Variables
""" NOTE: error message should be set to equal the relevant error from the errors array, 
rather than printed so when this is integrated with frontend you can post the error_message bac """
error_message = ""

# NOTE: Variables for testing. THESE WILL BE REPLACED WITH POST INPUTS FROM REG FORM
password = ""
username = ""
email = ""

""" TODO: Test new logic to see if returning 2 values works"""
def length_check(password, errors, error_message):
    if len(password) < 12:
        error_message = errors[0]
        return False, error_message
    elif len(password) > 128:
        error_message = errors[1]
        return False, error_message
    else:
        return True, error_message

# Checks wether or not the users password contains any array element from special_chars
def special_char_check(password, errors, special_chars):
    for i in range(len(password)):
        if password[i] in special_chars:
            return True
    error_message = errors[2]
    return False, error_message

# Checks if the converted lower case version of the users password matches the original
def upper_case_check(password, errors, error_message):
    if password == password.lower():
        error_message = errors[3]
        return False, error_message
    else:
        return True, error_message

# Checks if the converted upper case version of the users password matches the original
def lower_case_check(password, errors, error_message):
    if password == password.upper():
        error_message = errors[4]
        return False, error_message
    else:
        return True, error_message

# Checks each character to see if it is a number and confirms wether there is at least one num present
def number_check(password, errors, error_message):
    for i in range(len(password)):
        for x in range(9):
            if password[i] == str(x):
                return True
    error_message = errors[5]
    return False, error_message

