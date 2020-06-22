import socket
import tkinter
import threading
import json
from Calendar import Calendar
from tkinter import *
from tkinter import messagebox


class Agent:

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65430        # The port used by the server
    calendar = Calendar()
    s = None

    def listen(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))

        while True:
            data = self.s.recv(1024).decode()
            if data.startswith('BOOKING:'):
                newTimeData = json.loads(data.replace('BOOKING:', ''))
                print('Reveived calendar update:\n\n{}\n\n'.format(newTimeData))
                self.calendar = Calendar(newTimeData)
            elif data.startswith('CHECK:'):
                print('Received check request, reponding with calendar')
                self.s.sendall(str.encode('RESPONSE:{}'.format(json.dumps(self.calendar.timeData))))

    def issueBooking(self, hours):
        if self.calendar.canBookAppointment(hours):
            self.s.sendall(str.encode('BOOKING:{}'.format(hours)))
        else:
            print('Booking not possible for timeslot of {} hours'.format(hours))

agent = Agent()

top = tkinter.Tk()
top.geometry("300x500")
top.title("Agent")

bookingHours = Entry(top)
bookingHours.pack()

bookButton = Button(top, text="Make booking", command=lambda: agent.issueBooking(float(bookingHours.get())))
bookButton.pack()

t1 = threading.Thread(target = agent.listen)
t1.daemon = True
t1.start()
top.mainloop()
