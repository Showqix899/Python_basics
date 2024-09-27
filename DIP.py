# class EmailService:
#     def send(self,message):
#         print(f'Sending email: {message}')


# class Notifiaction:

#     def __init__(self):
#         self.service= EmailService()

#     def notify(self,message):
#         self.service.send(message)

#
class NotifiactionService:

    def send(self,message):
        pass

class EmailServie(NotifiactionService):

    def send(self,message):
        print(f'Sending email: {message}')

class Notification:

    def __init__(self,service: NotifiactionService):
        self.service=service
    
    def notify(self,message):
        self.service.send(message)



email_service= EmailServie()
notification=Notification(email_service)
notification.notify("hello!")