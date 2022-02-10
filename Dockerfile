FROM python:3.9 as base

# Install ubuntu libraries
RUN apt-get -yqq update && \
    apt-get -yqq install libsndfile1

# Install python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Install dataperf speech code
COPY . /app/dataperf_speech
WORKDIR /app/dataperf_speech

RUN chmod a+x /app/dataperf_speech/scripts/run.sh

ENTRYPOINT ["/app/dataperf_speech/scripts/run.sh"]
