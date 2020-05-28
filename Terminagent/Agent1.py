import socket
from Calendar import Calendar


class Agent:

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65430        # The port used by the server
    calendar = Calendar()
    s = None

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

    def listen(self):
        data = str(self.s.recv(1024))
        if data.startswith('BOOKING:'):
            timeToBook = float(data.replace('BOOKING:', ''))
            if self.calendar.canBookAppointment(timeToBook):
                self.calendar.bookAppointment(timeToBook)
        elif data.startswith('CHECK:'):
            timeToCheck = float(data.replace('CHECK:', ''))
            if self.calendar.canBookAppointment(timeToCheck):
                self.s.send('RESPONSE:True')

    def issueBooking(self, hours):
        if self.calendar.canBookAppointment(hours):
            self.s.send(str.encode('BOOKING:{}'.format(hours)))

agent = Agent()

agent.issueBooking(3.0)
while True:
    agent.listen()
