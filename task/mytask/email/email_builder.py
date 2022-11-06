
class EmailBuilder:

    @staticmethod
    def content(user):
        message = ""
        message += "<HTML><BODY>"
        message += "<H1>Thank You</H1>"
        message += "Registration is Successfully"

        message += f"<H1>Hi {user.user_name}! Greetings from Us!</H1>"
        message += f"<a href='http://127.0.0.1:8000/verify-user/{user.id}'>Please click here to verify</a>"
        return message
