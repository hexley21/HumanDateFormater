from plural_or_single import plural_or_single

class Time():
    def __init__(self, seconds):
        self.years = int(seconds / 31536000)
        self.days = int(seconds / 86400 - self.years * 365)
        self.hours = int(seconds / 3600 - (self.years * 8760 + self.days * 24))
        self.minutes = int(seconds / 60 - (self.years * 525600 + self.days * 1440 + self.hours *  60))
        self.seconds = int(seconds - (self.years * 31536000 + self.days * 86400 + self.hours *  3600 + self.minutes * 60))

    def format_time(self):
        if self.years == 0 and self.days == 0 and self.hours == 0 and self.minutes  == 0 and self.seconds == 0:
            return "now"
        real_time = { "second": self.seconds, "minute" : self.minutes, "hour" : self.hours, "day" : self.days, "year" : self.years}
        result = ""
        count = 0
        for i in real_time:
            if real_time[i] > 0:
                if count == 0:
                    result += plural_or_single(i, real_time[i])
                elif count == 1:
                    result = f"{plural_or_single(i, real_time[i])} and {result}"
                elif count > 1:
                    result = f"{plural_or_single(i, real_time[i])}, {result}"
                count += 1
        return result

if __name__ == "__main__":
    print("please run main.py")
