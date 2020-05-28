import socket
from Calendar import Calendar


class Manager:
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65430        # Port to listen on (non-privileged ports are > 1023)
    AGENT_COUNT = 3
    calendar = Calendar()
    addr = None
    conn = None

    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            self.conn, self.addr = s.accept()

    def listen(self):
        print('Connected by {}'.format(self.addr))
        data = str(self.conn.recv(1024))
        if data.startswith('BOOKING:'):
            timeToBook = float(data.replace('BOOKING:', ''))
            if self.calendar.canBookAppointment(timeToBook):
                if self.checkOtherAgents(timeToBook, self.conn):
                    self.calendar.bookAppointment(timeToBook)
                    self.bookOtherAgents(timeToBook, self.conn)

    def checkOtherAgents(self, timeNeeded, conn):
        conn.sendall(str.encode('CHECK:{}'.format(timeNeeded)))
        responseCount = 0
        possible = True
        while responseCount < self.AGENT_COUNT:
            response = str(conn.recv(1024))
            if response.startswith('RESPONSE:'):
                responseCount += 1
                responseValue = bool(response.replace('RESPONSE:', ''))
                if not responseValue:
                    possible = False
        return possible

    def bookOtherAgents(self, hours, conn):
        conn.sendall(str.encode('BOOKING:{}'.format(hours)))


manager = Manager()

while True:
    manager.listen()
