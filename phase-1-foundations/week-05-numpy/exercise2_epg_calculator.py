import numpy as np

start_times = np.array([600, 630, 900, 1200, 1380, 60, 120])  # minutes since midnight
runtimes = np.array([30, 60, 90, 60, 60, 30, 45])  # duration in minutes

# Q.1 End times — calculate end time for each show (start + runtime)
end_times = start_times + runtimes
print(end_times)

# Q.2 Convert to readable time — convert start_times from minutes to HH:MM format
st_min = start_times % 60
st_hr = start_times // 60
for h,m in zip(st_hr,st_min):
    print(f"{h:02d}:{m:02d}")

# Q.3 Past midnight flag — which shows run past midnight? (end time > 1440)
midnight = start_times[end_times>1440]
print(midnight)

# Q.4 Gaps between shows — calculate the gap between consecutive shows 
st_holes = np.diff(start_times)
print(st_holes)

# Q.5 Scheduling holes

gaps = st_holes[st_holes > 15]
print(gaps)