FROM python:3.7.4

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /app  # 나의 Django 코드를 컨테이너에 복사합니다.
RUN pip install -r /app/requirements.txt  # requirements.txt에 적혀있는 pip 패키지들을 설치합니다.
RUN chmod 755 /app/start  # start 파일을 실행 가능하게 합니다.
WORKDIR /app  # 워킹디렉토리를 /app으로 합니다.
EXPOSE 8000  # 8000번 포트를 expose합니다.