# TODO: Write script which will ensure the users entered password meets the specified criteria (from the password policy)

# Static Variables
org_name = "codelab"
""" TODO: When you add a function, if it hits an error, 
write the error in the array then call the array and specific array placement of the corresponding error """
errors = ["Passwords must contain at least 12 characters.","Passwords cannot exceed 128 characters"] 

# Initialised Variables
""" NOTE: error message should be set to equal the relevant error from the errors array, 
rather than printed so when this is integrated with frontend you can post the error_message bac """
error_message = ""
length_check_result = ""

# NOTE: Variables for testing. THESE WILL BE REPLACED WITH POST INPUTS FROM REG FORM
password = ""
username = ""
email = ""

""" TODO: Make this more efficient. The logic works and it acheives the goal but it seems overly bulky. 
Maybe remove length_check_result variable and just return True or False? """
def length_check(password, length_check_result, errors, error_message):
    if len(password) < 12:
        length_check_result = False
        error_message = errors[0]
    elif len(password) > 128:
        length_check_result = False
        error_message = errors[1]
    else:
        length_check_result = True
    if length_check_result == True:
        return length_check_result
    else:
        return length_check_result, error_message
    

