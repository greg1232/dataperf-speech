
from dataperf_speech import initialize_config_and_logging
from dataperf_speech import load_keyword_dataset
from dataperf_speech import get_embeddings
from dataperf_speech import split_embeddings
from dataperf_speech import select_embeddings
from dataperf_speech import train_model
from dataperf_speech import evaluate_model

def main():
    config = initialize_config_and_logging()

    keywords = load_keyword_dataset(config)

    embeddings = get_embeddings(keywords, config)

    train_embeddings, test_embeddings = split_embeddings(embeddings)

    selected_embeddings = select_embeddings(train_embeddings)

    model = train_model(selected_embeddings)

    results = evaluate_model(model, test_embeddings)

    save_results(results)

def save_results(results):
    print(results)

main()

