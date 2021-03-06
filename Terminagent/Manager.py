import socket
import tkinter
import threading
import time
import json
from tkinter import *
from tkinter import messagebox
from Calendar import Calendar


class Manager:
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65430        # Port to listen on (non-privileged ports are > 1023)
    agentCount = 0
    calendar = Calendar()
    socket = None
    respondingClients = []
    connections = set()

    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))
        
        print("Listening...")
        while True:
            self.socket.listen(1)
            conn, addr = self.socket.accept()
            print('New connection accepted from {}'.format(addr))
            self.connections.add(conn)
            self.agentCount += 1
            print('Added an agent - current agent count: {}'.format(self.agentCount))
            thread = threading.Thread(target=self.processConnection, args=[conn])
            thread.start()
            

    def processConnection(self, conn):
        print('Processing new connection {}'.format(conn))
        while True:
            data = conn.recv(1024).decode()
            if data.startswith('BOOKING:'):
                timeToBook = float(data.replace('BOOKING:', ''))
                thread = threading.Thread(target = self.issueBooking, args = [timeToBook])
                thread.start()
            elif data.startswith('RESPONSE:'):
                responseValue = json.loads(data.replace('RESPONSE:', ''))
                clientCalendar = Calendar(responseValue)
                self.respondingClients.append({'conn': conn, 'calendar': clientCalendar})

        self.connections.remove(conn)
        self.agentCount -= 1
        print('Removed an agent - current agent count: {}'.format(self.agentCount))
        conn.close()

    def issueBooking(self, hours):
        print('Booking request received for {} hours'.format(hours))
        if self.calendar.canBookAppointment(hours):
            if self.tryBookingAllClients(hours):
                print('Booking is possible')
                self.calendar.bookAppointment(hours)

    def tryBookingAllClients(self, timeNeeded):
        for conn in self.connections:
            conn.sendall(str.encode('CHECK:'))
        timeoutCount = 0
        possible = True
        respondingClients = []

        while len(self.respondingClients) < self.agentCount and timeoutCount < 3:
            print('waiting for response')
            timeoutCount += 1
            time.sleep(3)

        for rc in self.respondingClients:
            conn = rc['conn']
            clientCalendar = rc['calendar']
            if not clientCalendar.canBookAppointment(timeNeeded):
                possible = False   
                
        if (possible):
            for rc in self.respondingClients:
                conn = rc['conn']
                clientCalendar = rc['calendar']
                clientCalendar.bookAppointment(timeNeeded)
                print('Sending updated calendar back to {}'.format(conn.getpeername()))
                conn.sendall('BOOKING:{}'.format(json.dumps(clientCalendar.timeData)).encode())

        self.respondingClients = []
        return possible


manager = Manager()

top = tkinter.Tk()
top.geometry("300x500")
top.title("Manager")

bookingHours = Entry(top)
bookingHours.pack()

bookButton = Button(top, text="Make booking", command=lambda: manager.issueBooking(float(bookingHours.get())))
bookButton.pack()

t1 = threading.Thread(target = manager.listen)
t1.daemon = True
t1.start()
top.mainloop()

