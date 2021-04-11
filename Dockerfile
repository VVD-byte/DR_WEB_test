FROM python:3.9.4-buster
ADD requirements.txt requirements.txt
RUN apt update && pip install -r requirements.txt
WORKDIR /DR_WEB_test
COPY . .
EXPOSE 8080
CMD ["python", "-m", "api"]
