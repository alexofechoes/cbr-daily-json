FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
RUN mkdir /code
WORKDIR /code
ADD Pipfile* /code/
RUN pipenv install
ADD . /code/
EXPOSE 8000
ENTRYPOINT ["pipenv", "run", "gunicorn", "wsgi:app", "--bind=0.0.0.0:80"]
