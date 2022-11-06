
class EmailBuilder:
    """ Structure of email content"""
    @staticmethod
    def content(user):
        message = ""
        message += "<HTML><BODY>"
        message += "<H1>Thank You</H1>"
        message += "Registration is Successfully"
        message += f"<H1>Hi {user.user_name}! Greetings from Us!</H1>"
        message += f"<a href='https://mytasktest.herokuapp.com/verify-user/{user.id}'>Please click here to verify</a>"
        return message
