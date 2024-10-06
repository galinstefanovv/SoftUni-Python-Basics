exam_hour = int(input()) * 60
exam_minute = int(input())
arrival_hour = int(input()) * 60
arrival_minute = int(input())
exam_minutes = exam_hour + exam_minute
arrival_minutes = arrival_hour + arrival_minute
difference = exam_minutes-arrival_minutes
minutes = abs(difference) % 60
if minutes < 10 and abs(difference) >= 60:
    minutes = f"0{minutes}"
hours = abs(difference) // 60
if 0 <= difference <= 30:
    print("On time")
    if difference != 0:
        print(f"{minutes} minutes before the start")
elif 30 < difference < 60:
    print("Early")
    print(f"{minutes} minutes before the start")
elif 60 <= difference:
    print("Early")
    print(f"{hours}:{minutes} hours before the start")
elif 0 > difference > -60:
    print("Late")
    print(f"{minutes} minutes after the start")
elif -60 >= difference:
    print("Late")
    print(f"{hours}:{minutes} hours after the start")