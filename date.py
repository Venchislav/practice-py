import datetime

date = input().split()
days = int(input())
date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
date += datetime.timedelta(days=days)

print(date.year, date.month, date.day)
