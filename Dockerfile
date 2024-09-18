FROM python:3.12.5-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5656
CMD ["python", "./index.py"]
