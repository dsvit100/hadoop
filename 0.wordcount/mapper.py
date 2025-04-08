# 데이터를 쪼갤 것
#!/suer/bin/env python3
import sys

# stdin -> 시스템 기본 standard input 약어
# standard input은 우리가 올릴 파일 전체를 가르킴
# 내용을 한줄한줄 나눠 line으로 만들 것

for line in sys.stdin:
    # 좌우 공백 없애기
    line = line.strip()
    words = line.split()
    # 출력내용 = ['apple', 'hello', 'world']

    for word in words:
        # \t = 들여쓰기(tap)
        print(f'{word}\t1')
        # cat text.txt | python3 mapper.py => 왼쪽을 작업한 후 오른쪽에 넘겨줘
        # 각 단어들로 쪼개주고 모든 단어에 1을 붙여주는 작업