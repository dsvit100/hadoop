# 실행코드 : cat text.txt | python3 mapper.py | sort | python3 reducer.py
#!/suer/bin/env python3

import sys

# apple 1
# apple 1
# hello 1
# hello 1
# ... 과 같이 정렬된 상태로 sys.stdin으로 들어감

last_word = None # 글자가 바뀌는 시점을 알기 위해서
total_count = 0

for line in sys.stdin:
    word, value = line.split('\t') # \tap 기준으로 자르는데, 첫번째 데이터는 word에 두번째 데이터는 value에 넣어줘
    value = int(value) # sys.stdin은 숫자처럼 보여도 모두 str으로 생각함, 따라서 int로 감싸주기

    if last_word == word: # 만약 last_word가 내가 보고 있는 현재 word와 같다면 / 1회차 last_word는 None, 따라서 첫번째는 else가 실행됨
        total_count += value
    else:
        if last_word is not None:
            print(f'{last_word}\t{total_count}')
        last_word = word # 첫번째 반복인 경우 진행되는 코드 - last_word(None) 가 last_word(apple)로 바뀜, 다시 for문 돌림
        # word값이 바뀌면 값을 초기화해줌
        total_count = value # 다른 워드로 바뀌었기 때문에 값을 바꿔주는 것

if last_word == word:
    print(f'{last_word}\t{total_count}')
