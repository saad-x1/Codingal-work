total_days = int(input("Enter total working days: "))
absent_days = int(input("Enter absent days: "))

attended = total_days - absent_days
percentage = (attended / total_days) * 100

print("Attendance percentage:", percentage)

if percentage < 75:
    print("Not allowed to sit in exam")
else:
    print("Allowed to sit in exam")
