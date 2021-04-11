FROM python:3.9.4-buster
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
WORKDIR /DR_WEB_test
CMD ["python", "-m", "api"]
