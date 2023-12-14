FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y cron

WORKDIR /issf_world_rankings

COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./rankings rankings
RUN chmod +x rankings/entrypoint.sh

ENTRYPOINT ["rankings/entrypoint.sh"]