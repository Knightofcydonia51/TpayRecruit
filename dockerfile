FROM python:3.7.4
ARG PROJECT_DIR="/tpayRecruit"

COPY . ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}

RUN pip install --upgrade pip && pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000