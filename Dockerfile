FROM python:3.8.5

WORKDIR /code
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .
CMD python3 main.py