FROM python:3.10-alpine
ENV Home=/SPA-task
WORKDIR $HOME
COPY . $HOME
RUN pip install -r requirements.txt
WORKDIR /SPA
EXPOSE 8000
CMD python manage.py runserver 127.0.0.1:8000