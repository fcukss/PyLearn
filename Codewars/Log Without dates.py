

def check_logs(log):
    days = 1
    if not log:
      return 0
    temp_time = log[0]
    for time in log[1:]:
        if time < temp_time or time == temp_time:
            days+=1
        temp_time = time
    return days



log = ["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"]
print(check_logs(log))