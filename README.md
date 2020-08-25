## :credit_card: Tpay backend 코딩테스트

본 문서는 Tpay backend 개발자 코딩 테스트를 위해 작성되었습니다.



### 실행방법

```python -m venv venv
python -m venv venv 

source venv/Scripts/activate 

pip install -r requirements.txt 

python manage.py makemigrations 

python manage.py migrate

python manage.py runserver
```



### 접속주소

http://127.0.0.1:8000/

``/doc/``에 접속하게 되면 API와 실행 가능한 http method들이 명시되어 있습니다.



### 파일목록

Tpay_Backend.postman_collection.json : Postman Export 파일입니다.





### Docker 실행방법

* 도커가 설치되어 있어야 합니다.
* Docker Desktop for windows(https://hub.docker.com/editions/community/docker-ce-desktop-windows/ )

```
# dockerfile이 있는 디렉토리에서

docker pull django

docker build -t tpay .

docker run -it -p 8000:8000 --volume $(PWD):/tpayRecruit --name tpayContainer tpay

# 컨테이너 켜기
docker start -i tpayContainer

# 컨테이너 끄기
docker stop tpayContainer
```