import psycopg2

# TODO: Speak to alex about creating matching user credentials with a temp password for sharing
connection_details = {
    'dbname': 'codelab_test',
    'user': 'admin',
    # For me this was the pc password, since you don't have one I don't know what it will be, maybe leave blank?
    'password': '', 
    'host': 'localhost',
    # Start the db then run nmap on your ip and it will say
    'port': 5432
}