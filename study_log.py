day = {'mon':0,'tue':0,'wed':0,'thu':0,'fri':0,'sat':0,'sun':0}

days = list(day.keys())
count = 0

while True:
    x = int(input('勉強時間(分)：'))

    today = days[count]
    day[today] += x

    print(f'{today}の勉強時間は{day[today]}分')

    count += 1

    # 7日経過
    if count == 7:
        print(f'今週は{sum(day.values())}分勉強しました')

        # リセット
        for d in day:
            day[d] = 0

        count = 0
