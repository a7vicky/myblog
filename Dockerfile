FROM python:3.7

MAINTAINER "abhishekvicky18dec@gmail.com"

WORKDIR /usr/src/app

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT [ "python" ]

EXPOSE 5555

CMD [ "runserver.py" ]
