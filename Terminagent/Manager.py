import socket
from Calendar import Calendar

class Manager:
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65430        # Port to listen on (non-privileged ports are > 1023)
    calendar = Calendar()
    
    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((self.HOST, self.PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by {}'.format(addr))
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data.startswith('BOOKING:'):
                    timeToBook = float(data.replace('BOOKING:', ''))
                    for i in range(6):
                        timeAvailable = self.calendar.getFreeHoursOfDay(i)
                        if timeAvailable >= timeToBook and self.checkOtherAgents(i, timeToBook):
                            self.calendar.bookAppointment(i, timeToBook)
                            break
## add missing logic

                print('Checking for {} free hours in week'.format(int(data)))
                conn.sendall(data)

    def checkOtherAgents(self, day, timeNeeded):
        print('checking...')
