FROM python:3.12.7
COPY . /code
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["guvicorn", "app.main:app", "-b", "0.0.0.0:7860", "--reload"]