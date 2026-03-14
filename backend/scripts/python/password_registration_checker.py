# NOTE: When testing, enter any value for email and user as blank exists in every string

# Static Variables
org_name = "codelab"
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*"]
keybrd_wlks = ["qwerty"]
# TODO: Find better password list (this is too restrictive)
leaks = ["assets/pass_lists/10k-most-common.txt"]

functions = [
    lambda: length_check(password, errors, error_message),
    lambda: special_char_check(password, errors, special_chars),
    lambda: upper_case_check(password, errors, error_message),
    lambda: lower_case_check(password, errors, error_message),
    lambda: number_check(password, errors, error_message),
    lambda: disallowed_words(password, username, errors, error_message),
    lambda: keybrd_wlk_check(password, errors, error_message, keybrd_wlks),
    lambda: leak_check(password, errors, error_message, leaks),
]

errors = ["Passwords must contain at least 12 characters.",
          "Passwords cannot exceed 128 characters", 
          "Password must contain at least one special character (e.g. ! @ # $ % ^ & *)", 
          "Password must contain at least one upper case character", 
          "Password must contain at least one lower case character", 
          "Password must contain at least one number", 
          "Your password cannot contain your username, email or the platform name", 
          "Please avoid keyboard walking (i.e. qwerty, etc.)", 
          "This password was found in a data leak, please try another."] 

# Initialised Variables
error_message = ""
final_error_output = []
# NOTE: Variables for testing. THESE WILL BE REPLACED WITH POST INPUTS FROM REG FORM
password = ""
username = ""
email = ""

# Checks if the length of the password is acceptable
def length_check(password, errors, error_message):
    if len(password) < 12:
        error_message = errors[0]
        return False, error_message
    elif len(password) > 128:
        error_message = errors[1]
        return False, error_message
    else:
        return True, None

# Checks wether or not the users password contains any array element from special_chars
def special_char_check(password, errors, special_chars):
    for i in range(len(password)):
        if password[i] in special_chars:
            return True, None
    error_message = errors[2]
    return False, error_message

# Checks if the converted lower case version of the users password matches the original
def upper_case_check(password, errors, error_message):
    if password == password.lower():
        error_message = errors[3]
        return False, error_message
    else:
        return True, None

# Checks if the converted upper case version of the users password matches the original
def lower_case_check(password, errors, error_message):
    if password == password.upper():
        error_message = errors[4]
        return False, error_message
    else:
        return True, None

# Checks each character to see if it is a number and confirms wether there is at least one num present
def number_check(password, errors, error_message):
    for i in range(len(password)):
        for x in range(9):
            if password[i] == str(x):
                return True, None
    error_message = errors[5]
    return False, error_message

# Checks specific disallowed words
def disallowed_words(password, username, errors, error_message):
    if username.lower() in password.lower():
        error_message = errors[6]
        return False, error_message
    elif email.lower() in password.lower():
        error_message = errors[6]
        return False, error_message
    elif org_name.lower() in password.lower():
        error_message = errors[6]
        return False, error_message
    else:
        return True, None
    
# Checks if the password contains specific keyboard walks
def keybrd_wlk_check(password, errors, error_message, keybrd_wlks):
    for i in range(len(keybrd_wlks)):
        if keybrd_wlks[i] in password.lower():
            error_message = errors[7]
            return False, error_message
    return True, None

# Checks if the users password has been recently leaked
def leak_check(password, errors, error_message, leaks):
    for i in range(len(leaks)):
        with open(leaks[i]) as file:
            for x in file:
                if x.strip("\n") in password.lower():
                    error_message = errors[8]
                    return False, error_message
    return True, None

def main(functions):
    for function in functions:
        result, error_message = function()
        if result:
            pass
        else:
            final_error_output.append(error_message)
    return final_error_output
        
main(functions)