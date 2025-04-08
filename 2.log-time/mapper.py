import sys
import re

# r = 정규표현식입니다. 이후 찾을 패턴값
# 54.36.149.41 - - [22/Jan/2019:03:56:14 +0330] "GET /filter/27|13%20%D9%85%DA%AF%D8%A7%D9%BE%DB%8C%DA%A9%D8%B3%D9%84,27|%DA%A9%D9%85%D8%AA%D8%B1%20%D8%A7%D8%B2%205%20%D9%85%DA%AF%D8%A7%D9%BE%DB%8C%DA%A9%D8%B3%D9%84,p53 HTTP/1.1" 200 30577 "-" "Mozilla/5.0 (compatible; AhrefsBot/6.1; +http://ahrefs.com/robot/)" "-"

time_pattern = re.compile(r':(\d{2}):(\d{2}):(\d{2})')
# 어떤 숫자던간(\d)에 {2칸}이어야 함, 위의 패턴식을 찾아줘, ()는 각 값들을 그룹으로 만들어줌

for line in sys.stdin:
    line = line.strip() # 공백제거
    # 정규표현식
    # 내가 특정한 패턴이 일치하는 부분을 기준으로 데이터에 접근할 때

    match = time_pattern.search(line) # 한 줄 안에 있는 패턴을 찾아서 그 값을 match라고 할게

    if match: # match값이 있으면
        hour = match.group(1) # 여기서 0번째는 전체값이 나옴
        print(f'{hour}\t1') # \t = 탭, 1 = 1을 작성
        # 이거 print 값 확인하려면 어떻게 해야했지?