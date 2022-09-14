FROM python:3
LABEL author="ASW"
WORKDIR /app
RUN pip install webssh
ENTRYPOINT ["/usr/local/bin/wssh"]
CMD ["--port=80", "--maxconn=128", "--redirect=false"]