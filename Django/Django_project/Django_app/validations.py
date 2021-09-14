# import regular exp.
import re


# Create your validations here.


def isValidIFSCode(str):
    '''
    The function checks if ifsc code is valid or not.

    Parameters:
        str (String): The ifsc code.
    
    Returns:
        (bool) : A boolean value.
    '''
    
    # Regex to check valid IFSC Code.
    regex = "^[A-Z]{4}0[A-Z0-9]{6}$"
    
    # Compile the ReGex
    p = re.compile(regex)
    
    # If the string is empty return false.
    if (str == None):
        return False
    
    # Return if the string matched the ReGex.
    if (re.search(p, str)):
        return True
    else:
        return False


def isValidsortorder(data):
    '''
    The function checks if sort order is valid or not.

    Parameters:
        data (String): The sort order.
    
    Returns:
        (bool) : A boolean value.
    '''

    # If the string is empty return.
    if data == '':
        return True
    elif data == 'DESC':
        return True
    elif data == 'ASC':
        return True
    else:
        return False


def isValidfetchcount(data):
    '''
    The function checks if fetch count is valid or not.

    Parameters:
        data (String): The fetch count.
    
    Returns:
        (bool) : A boolean value.
    '''

    # If the string is empty return.
    if data == '':
        return True
    elif int(data) >= 0:
        return True
    else:
        return False

