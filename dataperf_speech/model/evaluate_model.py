import numpy as np

def evaluate_model(model, embeddings):
    embeddings = list(embeddings)

    embedding_data = [embedding for embedding, metadata in embeddings]
    max_timesteps = max([embedding.shape[1] for embedding in embedding_data])
    padded_embedding_data = [np.pad(embedding, ((0,0), (0, max_timesteps - embedding.shape[1]), (0, 0))) for embedding in embedding_data]

    x = np.concatenate(padded_embedding_data)
    y = np.asarray([0 if metadata["is_unknown"] else 1 for embedding, metadata in embeddings], dtype=np.int)

    x = np.amax(x, 1)

    return model.score(x, y)

