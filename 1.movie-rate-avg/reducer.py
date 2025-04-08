import sys
# '296\t5.0'

currunt_movie_id = None
currunt_sum = 0
currunt_count = 0

for line in sys.stdin:
    movie_id, rating = line.split()
    # 빈 칸을 기준으로 movie_id와 rating 값을 나눠줌

    try:
    rating = float(rating) # 중간에 에러 발생을 하먄
    except:
        continue
        # 글자라면 넘어감

    if currunt_movie_id == movie_id
        currunt_count += 1
        currunt_sum += rating
    # 영화가 바뀐 지점 = else
    
 else:
    if currunt_movie_id is not None: # 값이 None이 아닐 때만 아래를 진행해주세요
        currunt_avg = currunt_sum / currunt_count
        print(f'{currunt_movie_id}')

    # 현재 커런트의 정보를 새로 저장함
    currunt_movie_id = movie_id
    currunt_count = 1
    currunt_sum = rating

currunt_avg = currunt_sum ; currunt_count
print('f{currunt_movie_id}\t{currunt_avg}')