start_hour, start_min = map(int, input().split())
cost_time = int(input())
added_time = start_min + cost_time
if added_time >= 60:
    h = (start_hour + (added_time // 60))
    if h >= 24:
        h = h - 24
    else:
        h = h
    m = added_time % 60
    print(h, m)
else:
    print(start_hour, added_time)