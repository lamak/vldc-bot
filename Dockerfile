FROM python:3.7-slim

COPY . /app
WORKDIR /app

#RUN pip install -r requirements.txt
RUN python setup.py install

CMD ["python", "bot.py"]