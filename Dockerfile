FROM python:3.11-alpine

VOLUME /usr/src/app/config
VOLUME /usr/src/app/query

WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "main", "--help" ]
