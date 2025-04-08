# hadoop command
- `ls`
    - `hdfs dfs -ls /` 
    - hdfs dfs -ls <확인하고 싶은 경로>

- `hdfs dfs -mkdir /<폴더명>`
    - 폴더 생성

- `put`
    - hdfs dfs -put <업로드할 파일> <업로드할 위치>
    - hdfs dfs -put ml-25m/movies.csv /input (외부에 있는 하둡 폴더이기 때문에 자동완성X)

- `cat`
    - hdfs dfs -cat <출력하고싶은 파일 경로>
    - txt파일만 읽을 수 있음

- `head`, `tail`
    - hdfs dfs -head <출력하고싶은 파일 경로>

- `rm`
    - hdfs dfs -rm <삭제하고싶은 파일>
    - hdfs dfs -rm -r <삭제하고싶은 폴더>