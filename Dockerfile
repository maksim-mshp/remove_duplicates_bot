FROM python

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]