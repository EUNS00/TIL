T = int(input())
TO = (1, 3, 5, 7, 8, 10, 12)
TT = (4, 6, 9, 11)
TE = 2
for i in range(T):
    date = input()
    date_year = date[0:4]
    date_month = date[4:6]
    date_day = date[6:]
    if int(date_month) in TO:
        if int(date_day) <= 31:
            print(f'#{i+1} {date_year}/{date_month}/{date_day}')
        else:
            print(f'#{i+1} -1')
    elif int(date_month) in TT:
        if int(date_day) <= 30:
            print(f'#{i+1} {date_year}/{date_month}/{date_day}')
        else:
            print(f'#{i+1} -1')
    elif int(date_month) == TE:
        if int(date_day) <= 28:
            print(f'#{i+1} {date_year}/{date_month}/{date_day}')
        else:
            print(f'#{i+1} -1')
    else:
        print(f'#{i+1} -1')