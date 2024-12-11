FROM python:3.12.7
COPY . /code
WORKDIR /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

CMD ["gunicorn", "app.main:app", "-b", "0.0.0.0:7860", "--reload"]