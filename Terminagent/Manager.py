import socket
import tkinter
import threading
from tkinter import *
from tkinter import messagebox
from Calendar import Calendar


class Manager:
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65430        # Port to listen on (non-privileged ports are > 1023)
    AGENT_COUNT = 1
    calendar = Calendar()
    socket = None
    addr = None
    conn = None

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))

    def listen(self):
        print("Listening...")
        self.socket.listen(1)
        
        self.conn, self.addr = self.socket.accept()
        data = str(self.conn.recv(1024))
        if data.startswith('BOOKING:'):
            timeToBook = float(data.replace('BOOKING:', ''))
            print("Received booking over {} hours".format(timeToBook))
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

    def issueBooking(self, hours):
        if self.calendar.canBookAppointment(hours):
            if self.checkOtherAgents(hours, self.conn):
                self.calendar.bookAppointment(hours)
                self.bookOtherAgents(hours, self.conn)


manager = Manager()

top = tkinter.Tk()
top.geometry("300x500")

bookingHours = Entry(top)
bookingHours.pack()

bookButton = Button(top, text="Make booking", command=lambda: manager.issueBooking(float(bookingHours.get())))
bookButton.pack()

t1 = threading.Thread(target=manager.listen)
t1.start()
t0 = threading.Thread(target = top.mainloop)
t0.run()

