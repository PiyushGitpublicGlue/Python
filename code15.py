class FitnessTracker:
    def __init__(self,username):
        self.username = username
        self.workout_logs = []
        self.count=0

    def log_workout(self,minutes):
        self.workout_logs.append(minutes)
    
    def get_total_minutes(self):
        for total in self.workout_logs:
            self.count+=total
        return self.count
    
    def get_average_workout(self):
        return sum(self.workout_logs)/len(self.workout_logs)
    

tracker = FitnessTracker("Piyush")
tracker.log_workout(30)
tracker.log_workout(45)
tracker.log_workout(60)

print(tracker.get_total_minutes())    # Should print 135
print(tracker.get_average_workout())  # Should print 45.0