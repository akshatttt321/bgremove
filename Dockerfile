FROM python:3.12.7
COPY . .
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["guvicorn", "/code/app/main.py:app", "-b", "0.0.0.0:7860", "--reload"]

