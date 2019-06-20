FROM python:3.7.3-stretch

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY api/ ./
COPY start.sh ./

CMD ./start.sh
