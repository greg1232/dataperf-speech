
from transformers import Wav2Vec2Processor, Wav2Vec2Model
import torch
from datasets import load_dataset

def get_embeddings(dataset, config):
    sampling_rate = dataset.features["audio"].sampling_rate

    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")

    for count, example in enumerate(dataset):

        if count >= int(config["data"]["sample_count"]):
            break

        # audio file is decoded on the fly
        inputs = processor(example["audio"]["array"], sampling_rate=sampling_rate, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)

        last_hidden_states = outputs.last_hidden_state
        print(list(last_hidden_states.shape))
        print(example)

        yield (last_hidden_states, example)


