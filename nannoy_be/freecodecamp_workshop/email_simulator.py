# In this workshop, you are going to build an Email Simulator that simulates sending, receiving,
#  and managing emails between different users. 
# You'll learn about classes, objects, and how to organize code in an object-oriented way.

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False

    def mark_as_read(self):
        self.read = True

class User:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)

class Inbox:
    def __init__(self):
        self.emails = []