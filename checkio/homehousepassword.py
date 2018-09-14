# Stephan and Sophia forget about security and use simple passwords for everything.
#  Help Nikola develop a password security check module. 
# The password will be considered strong enough if its length is greater than or
#  equal to 10 symbols, it has at least one digit, 
# as well as containing one uppercase letter and one lowercase letter in it. 
# The password contains only ASCII latin letters or digits.

# Input: A password as a string.

# Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.

# Example:

# checkio('A1213pokl') == False
# checkio('bAse730onE') == True
# checkio('asasasasasasasaas') == False
# checkio('QWERTYqwerty') == False
# checkio('123456123456') == False
# checkio('QwErTy911poqqqq') == True
import re 
def house_password_check(password):
    # len >= 10 digits
    if len(password) < 10 :
        return False
    # at leat one lowercase and one uppercase letter    
    # must all is not lowercase
    if password.islower():
        return False
    # must all is not uppercase
    if password.isupper():
        return False
    # must not be digit
    if password.isdigit():
        return False
    # at lest one digit &  only ASCII latin letters by regular expression
    if not re.match('[a-zA-Z0-9]+[0-9]', password):
        return False
    else:
        return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house_password_check('A1213pokl') == False, "1st example"
    assert house_password_check('bAse730onE4') == True, "2nd example"
    assert house_password_check('asasasasasasasaas') == False, "3rd example"
    assert house_password_check('QWERTYqwerty') == False, "4th example"
    assert house_password_check('123456123456') == False, "5th example"
    assert house_password_check('QwErTy911poqqqq') == True, "6th example"
