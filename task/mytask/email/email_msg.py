from task.settings import EMAIL_HOST_USER


class EmailMessage:
    """ Email messages section """
    def __init__(self):
        self.frm = EMAIL_HOST_USER
        self.to = []
        self.cc = []
        self.bcc = []
        self.subject = ""
        self.text = ""
        self.user = ""
        self.type = "html"
