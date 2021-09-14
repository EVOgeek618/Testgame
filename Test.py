class Time:
    now = 0
    all_time = ["m", "a", "e", "n"]
    time = all_time[now]

    def change_time(self):
        self.now += 1
        self.time = self.all_time[self.now % 4]

t = Time()
print(t.time)
t.change_time()
print(t.time)