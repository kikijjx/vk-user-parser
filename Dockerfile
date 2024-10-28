FROM python:3.12-slim

RUN pip install requests

WORKDIR /app

COPY . .

ENV VK_API_TOKEN=""
ENV VK_USER_ID=""

CMD ["python", "main.py"]
