
import random

def split_embeddings(embeddings):
    seed = 42
    train_ratio = 0.5

    embeddings = list(embeddings)

    return (get_train_embeddings(seed, train_ratio, embeddings),
        get_test_embeddings(seed, train_ratio, embeddings))

def get_train_embeddings(seed, train_ratio, embeddings):

    generator = random.Random(seed)

    for embedding in embeddings:
        if generator.random() < train_ratio:
            yield embedding

def get_test_embeddings(seed, train_ratio, embeddings):

    generator = random.Random(seed)

    for embedding in embeddings:
        if generator.random() >= train_ratio:
            yield embedding

