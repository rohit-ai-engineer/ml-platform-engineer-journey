from datetime import datetime, timedelta

# EPG Time Slot Calculator - Week 1 Project
# Calculates show end time given start time and duration

print ("===EPF Time Slot Calculator===")
print()

start_time_input = input("Enter show start time (HH:MM format, e.g., 14:30):")

start_time = datetime.strptime(start_time_input, "%H:%M")

duration_minutes = int(input("Enter show duration in minutes:"))

end_time = start_time + timedelta(minutes=duration_minutes)

print()
print("--- Result ---")
print(f"Show starts: {start_time.strftime('%H:%M')}")
print(f"Duration:    {duration_minutes} minutes")
print(f"Show ends:   {end_time.strftime('%H:%M')}")