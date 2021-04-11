FROM python:latest
WORKDIR /DR_WEB_test
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY app.py app.py
CMD ["python", "-m", "api"]