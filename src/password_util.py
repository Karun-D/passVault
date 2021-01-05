"""
------------------------------------------------------------------------
password_util Module
------------------------------------------------------------------------
"""

# Imports
import random
import sqlite3 as sq

def random_password():
    """
    -------------------------------------------------------
    Generates a random secure password to be stored in
    database
    -------------------------------------------------------
    Parameters:
        No Parameters
    Returns:
        password - A random generated password
    -------------------------------------------------------
    """
    length = 10
    characters = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$&*?"
    password = []

    for i in range(length):
        # Chooses a random character from acceptable character string
        char = random.choice(characters)

        # If the character is a letter, function randomly selects the letter in uppercase form
        if char.isalpha():
            num = random.uniform(0, 1)
            if num >= 0.5:
                char = char.upper()

        # Adds character to password list
        password.append(char)

    # Converts password list into a string
    password = "".join(password)

    return password


def store_password(conn, platform, password, user_id):
    """
    -------------------------------------------------------
    Store's user's account name and password in database
    -------------------------------------------------------
    Parameters:
        platform - Name of account (String)
        choice - User's choice between a generated/custom
            password
        conn - Connection object to connect to
            database (sq.connect)
    Returns:
        No return
    -------------------------------------------------------
    """

    formatted_row = (platform.upper(), password, user_id)                   # Create row of data
    c = conn.cursor()                                                       # Create a Cursor object from Database Connnection
    c.execute('INSERT INTO passwords VALUES (?,?,?)', formatted_row)        # Insert row of data into db
    conn.commit()                                                           # Save (commit) the changes


def retrieve_password(conn, platform, user_id):
    """
    -------------------------------------------------------
    Store's user's account name and password in database
    -------------------------------------------------------
    Parameters:
        platform - Name of account (String)
        conn - Connection object to connect to
            database (sq.connect)
    Returns:
        No return
    -------------------------------------------------------
    """

    formatted_search = (platform.upper(), user_id)                                          # Create row of search values
    c = conn.cursor()                                                                       # Create a Cursor object from Database Connnection
    c.execute('SELECT * FROM passwords WHERE platform=? AND user_id=?', formatted_search)   # Search database for data based on filter
    conn.commit()                                                                           # Save (commit) the changes
    password = c.fetchone()                                                                 # Retrieve matching row (list)

    return password[1]                                                                      # Return password








