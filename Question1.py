import datetime

class Alarm:
    def __init__(self, time: datetime.time, day_of_week: str):
        self.time = time
        self.day_of_week = day_of_week
        self.snooze_count = 0
        self.max_snooze = 3
        self.snooze_interval = datetime.timedelta(minutes=5)
    
    def snooze(self):
        if self.snooze_count < self.max_snooze:
            self.time = (datetime.datetime.combine(datetime.date.today(), self.time) + self.snooze_interval).time()
            self.snooze_count += 1
            print(f"Alarm snoozed to {self.time}")
        else:
            print("Maximum snooze limit reached.")
    
    def reset_snooze(self):
        self.snooze_count = 0
    
    def __str__(self):
        return f"Alarm set for {self.time} on {self.day_of_week}"

class AlarmClock:
    def __init__(self):
        self.alarms = []
    
    def add_alarm(self, time: datetime.time, day_of_week: str):
        new_alarm = Alarm(time, day_of_week)
        self.alarms.append(new_alarm)
        print(f"New alarm added: {new_alarm}")
    
    def delete_alarm(self, alarm: Alarm):
        if alarm in self.alarms:
            self.alarms.remove(alarm)
            print(f"Alarm deleted: {alarm}")
        else:
            print("Alarm not found.")
    
    def show_alarms(self):
        if self.alarms:
            print("Current Alarms:")
            for alarm in self.alarms:
                print(alarm)
        else:
            print("No alarms set.")
    
    def display_time(self):
        current_time = datetime.datetime.now().time()
        print(f"Current time: {current_time.strftime('%H:%M:%S')}")

import datetime

# Create an instance of the AlarmClock
alarm_clock = AlarmClock()

# Display the current time
alarm_clock.display_time()

# Add some alarms
alarm_clock.add_alarm(datetime.time(7, 0), "Monday")
alarm_clock.add_alarm(datetime.time(8, 30), "Tuesday")

# Show current alarms
alarm_clock.show_alarms()

# Snooze the first alarm
if alarm_clock.alarms:
    alarm_clock.alarms[0].snooze()

# Show alarms after snoozing
alarm_clock.show_alarms()

# Delete an alarm
if alarm_clock.alarms:
    alarm_clock.delete_alarm(alarm_clock.alarms[0])

# Show alarms after deletion
alarm_clock.show_alarms()
