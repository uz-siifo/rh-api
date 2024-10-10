
class util:
    @staticmethod
    def is_contact(contact):
        import re as regex
        return regex.match("^(\\+258){0,1}(8)[2-7]\\d{7}$",  contact) is not None
