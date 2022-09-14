# ASW
FROM alpine:3.7 as downloader

ARG DOCKER_CLI_VERSION="18.03.1-ce"
ENV DOWNLOAD_URL="https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_CLI_VERSION.tgz"

RUN apk --no-cache add curl \
    && curl -L $DOWNLOAD_URL | tar -xz docker \
    && mv docker/docker /usr/local/bin/docker

#

FROM lscr.io/linuxserver/openssh-server:latest

EXPOSE 2222

COPY --from=downloader /usr/local/bin/docker /usr/local/bin/docker

RUN apk --no-cache add git python3 py3-pip \
    && git clone https://github.com/aweher/lab-lacnog-menu.git /shell \
    && pip install -r /shell/requirements.txt \
    && echo /shell/shellmenu.sh >> /etc/shells \