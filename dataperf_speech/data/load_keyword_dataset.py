
from datasets import load_dataset

def load_keyword_dataset(config):

    dataset = load_dataset("speech_commands", "v0.02", split="validation", cache_dir="/tmp", streaming=True)

    dataset = dataset.shuffle(2048)

    print(dataset)

    return dataset

