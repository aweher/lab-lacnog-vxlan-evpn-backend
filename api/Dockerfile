FROM python:3.10-alpine

EXPOSE 6789

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["api.py"]