from setUp.GameRules import MINUTES_PER_PERIOD, CLOCK_INTERVAL, NUMBER_OF_PERIODS

class TimeKeeper:
    def __init__(self):
        self.period = 1
        self.minutes = MINUTES_PER_PERIOD
        self.seconds = 0
        self.has_game_started = False
        self.is_it_halftime = False
        self.is_game_over = False

    def advance_time(self, interval=CLOCK_INTERVAL):
        if self.seconds <= 0:
            self.minutes -= 1
            self.seconds = 60
        self.seconds -= interval
        if self.minutes < 0:
            self.reset_time()

    def get_time_remaining(self):
        if self.seconds == 0:
            return self.minutes
        else:
            return self.minutes + 1

    def display_time(self):
        return f"{self.minutes:02}:{self.seconds:02}"

    def reset_time(self):
        self.minutes = 20
        self.seconds = 0
        self.period += 1

        if self.period > NUMBER_OF_PERIODS:
            self.is_game_over = True
        else:
            self.is_it_halftime = True

    def start_overtime(self):
        self.minutes = 5
        self.seconds = 0

        self.is_game_over = False

