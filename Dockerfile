FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get -y install graphviz graphviz-dev pkg-config
RUN mkdir /code
WORKDIR /code
ADD entrypoint.sh /code/
RUN chmod +x entrypoint.sh
ADD requirements.pip /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.pip
ADD . /code/
ENTRYPOINT ["sh", "/code/entrypoint.sh" ]