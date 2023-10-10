import nltk
import string
import pymorphy3

chars_to_remove = string.punctuation + '\n\xa0«»\t—…'
stop_words = nltk.corpus.stopwords.words('russian')
morph_analyzer = pymorphy3.MorphAnalyzer()


def prepare_texts(texts: dict[str, list[str]]):
    for style in texts:
        for i in range(len(texts[style])):
            texts[style][i] = prepare_text(texts[style][i])


def prepare_text(text: str) -> str:
    text = text.lower()
    text = text.replace('\n', ' ')
    return "".join([char for char in text if char not in chars_to_remove])


def tokenize_text(text: str) -> list[str]:
    return nltk.word_tokenize(text, 'russian')


def prepare_tokens(tokens: list[str]) -> list[str]:
    filtered_tokens: list[str] = []
    for token in tokens:
        if token not in stop_words:
            filtered_tokens.append(token)

    normalized_tokens = []
    for word in filtered_tokens:
        normalized_tokens.append(morph_analyzer.normal_forms(word)[0])

    return normalized_tokens
