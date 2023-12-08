FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DB_URL=""

RUN apt-get update && apt-get install -y cron

WORKDIR /issf_world_rankings

COPY ./requirements.txt /issf_world_rankings/requirements.txt
RUN pip3 install --no-cache-dir -r /issf_world_rankings/requirements.txt

COPY ./rankings /issf_world_rankings/rankings

RUN env > /etc/environment

COPY ./rankings/cronscraper /etc/cron.d/cronscraper
RUN chmod 0644 /etc/cron.d/cronscraper
RUN crontab /etc/cron.d/cronscraper

CMD ["cron", "-f", "-l", "2"]
