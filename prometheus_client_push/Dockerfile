FROM python:3.7.8-slim-stretch

COPY ./apt.conf /etc/apt/

RUN apt update && apt install -y --no-install-recommends vim \
    dnsutils \
    procps \
    busybox-static

WORKDIR /usr/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./src .

ENV TZ=Asia/Tokyo

COPY ./crontab /var/spool/cron/crontabs/root

CMD ["busybox", "crond", "-f", "-L", "/dev/stderr"]