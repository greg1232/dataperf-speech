
# Dataperf Speech

A reference implementation of a dataperf speech benchmark.

* The task is keyword spotting using Google Speech commands.
* Wav2Vec is used to generate embeddings for each audio.
* A selection algorithm picks audios to train on.
* A logistic regression model is trained on these embeddings.

# Installation

1. Install docker: https://docs.docker.com/get-docker

2. clone this repo:

```
git clone git@github.com:greg1232/dataperf-speech.git
```

3. Run the benchmark:

```
./run-benchmark
```


