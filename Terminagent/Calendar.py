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

    

    def bookAppointment(self, day, hours):
        dayData = self.timeData[day]
        upper = dayData[self.UPPER_BOUND_KEY]
        lower = dayData[self.LOWER_BOUND_KEY]
        if upper - lower < hours:
            return None
        appointment = {'start':lower, 'end':lower+hours}
        self.timeData[day][self.APPOINTMENTS_KEY].append(appointment)
        self.timeData[day][self.LOWER_BOUND_KEY] = lower+hours
        return appointment

    def getFreeHoursOfDay(self, day):
        return self.timeData[day][self.UPPER_BOUND_KEY] - self.timeData[day][self.LOWER_BOUND_KEY]

