FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y cron

RUN --mount=type=secret,id=DB_URL \
  export DB_URL=$(cat /run/secrets/DB_URL)

WORKDIR /issf_world_rankings

COPY ./requirements.txt /issf_world_rankings/requirements.txt
RUN pip3 install --no-cache-dir -r /issf_world_rankings/requirements.txt

COPY ./rankings /issf_world_rankings/rankings

RUN env > /etc/environment

COPY ./rankings/cronscraper /etc/cron.d/cronscraper
RUN chmod 0644 /etc/cron.d/cronscraper
RUN crontab /etc/cron.d/cronscraper

CMD ["cron", "-f", "-l", "2"]
