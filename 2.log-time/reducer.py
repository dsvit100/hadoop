import sys

last_hour = None
total_count = 0

# 03   1
# 03   1
# 04   1 ...
for line in sys.stdin:
    line = line.strip()

    hour, value = line.split()
    value = int(value) # 현재 데이터가 글자이기 때문에 숫자로 바꿔주기

    if last_hour == hour: # 마지막 시간이 내가 보고 있는 시간과 같다면
        total_count += value

    else: # 바뀌는 경계점
        last_hour is not None: # None이 아닐 때만 실행할 것 (첫번째 값 때문에)
            print(f'{last_hour}\t{total_count}')

        
        # 초기화
        last_hour = hour
        total_count = value

print(f'{last_hour}\t{total_count}')