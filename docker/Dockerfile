FROM python:3.10.5-alpine3.16
LABEL maintainer="digitaltree.app"

ENV APP_HOME=/digitaltree
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /digitaltree/requirements.txt 

COPY . /digitaltree

COPY ./docker/scripts /scripts

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install setuptools wheel --upgrade && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /digitaltree/requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app &&\
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    mkdir -p /digitaltree/logs && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R 777 /digitaltree/logs && \
    chmod -R +x /digitaltree/docker/scripts

COPY ./staticfiles/images/avatars/profile_default.png /vol/web/media/profile_default.png

ENV PATH="/digitaltree/docker/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]