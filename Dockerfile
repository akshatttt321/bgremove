FROM python:3.12.7
COPY . .
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
CMD ["guvicorn", "/app/main.py:app", "-b", "0.0.0.0:7860", "--reload"]

