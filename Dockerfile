FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install requests fastapi uvicorn

ENV VK_API_TOKEN=""
ENV VK_USER_ID=""

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
