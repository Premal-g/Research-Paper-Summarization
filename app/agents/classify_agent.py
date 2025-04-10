from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_topic(text: str, candidate_topics: list[str]) -> str:
    result = classifier(text, candidate_topics)
    return result['labels'][0]  # Top predicted topic
