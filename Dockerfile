FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/Ottermad/vle-internals.git
ADD . /code/

CMD ["python", "manage.py","--config", "minikube", "run"]

