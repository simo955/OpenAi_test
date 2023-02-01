FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV OPENAI_API_KEY=
CMD [ "python3", "-m" , "app"]


