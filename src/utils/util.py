
import re as regex

class util:
    @staticmethod
    def is_contact(contact):
        return bool(regex.match("^(\\+258){0,1}(8)[2-7]\\d{7}$",  contact))

    @staticmethod
    def is_number(number):
        return bool(regex.match("^\\d+$", number))
    
    @staticmethod
    def is_email(email):
        return bool(regex.match("^\\w+(.){0,1}\\w+@(gmail|outlook|icloud|hotmail|yahoo)(.)(com)$", email))

    @staticmethod
    def is_username(username):
        return bool(regex.match("^\\w+(-)\\w+$", username))

    # tunisha-nhaquel
    # nome-apelido
# print(util.is_email("eloide.novela@gmail.com"))

# print(util.is_username("eloide"))