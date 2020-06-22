class Calendar:
    LOWER_BOUND_KEY = 'lowerBound'
    UPPER_BOUND_KEY = 'upperBound'
    APPOINTMENTS_KEY = 'appointments'
    

    timeData = [
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []},
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []},
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []},
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []},
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []},
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []},
            {LOWER_BOUND_KEY: 8.0, UPPER_BOUND_KEY: 18.0, APPOINTMENTS_KEY: []}
        ]

    def __init__(self, timeData = None):
        if not timeData is None:
            self.timeData = timeData

    def canBookAppointment(self, hours):
        for i in range(len(self.timeData)):
            if self.getFreeHoursOfDay(i) >= hours:
                return True
        return False


    def bookAppointment(self, hours):
        for i in range(len(self.timeData)):
            if self.getFreeHoursOfDay(i) >= hours:
                self.bookAppointmentByDay(i, hours)
                return True
        return False

    def bookAppointmentByDay(self, day, hours):
        dayData = self.timeData[day]
        upper = dayData[self.UPPER_BOUND_KEY]
        lower = dayData[self.LOWER_BOUND_KEY]
        if upper - lower < hours:
            return None
        appointment = {'start':lower, 'end':lower+hours}
        self.timeData[day][self.APPOINTMENTS_KEY].append(appointment)
        self.timeData[day][self.LOWER_BOUND_KEY] = lower+hours
        print('\n========\nAppointment was booked for day {} with {} hours.\nCurrent time data:\n{}\n========\n'.format(day, hours, self.timeData))
        return appointment

    def getFreeHoursOfDay(self, day):
        return self.timeData[day][self.UPPER_BOUND_KEY] - self.timeData[day][self.LOWER_BOUND_KEY]

