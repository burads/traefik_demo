from python:3.9.6-bullseye

WORKDIR /usr/src/app

COPY ./requerements.txt /usr/src/app/
COPY ./flaskHost.py /usr/src/app/

RUN pip3 install -r requerements.txt

EXPOSE 8080/tcp

CMD [ "python3", "/usr/src/app/flaskHost.py" ]