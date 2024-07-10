FROM python:3.10.2-slim

COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]