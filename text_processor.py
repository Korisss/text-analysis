import nltk
import string
import pymorphy3
import ruccent
from RusPhonetic import phonetic_module

vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё']
chars_to_remove = string.punctuation + '\n\xa0«»\t—…–:'
stop_words = nltk.corpus.stopwords.words('russian')
morph_analyzer = pymorphy3.MorphAnalyzer()
accentor = ruccent.Accent()


def prepare_texts(texts: dict[str, list[str]]):
    for style in texts:
        for i in range(len(texts[style])):
            texts[style][i] = prepare_text(texts[style][i])


def prepare_text(text: str) -> str:
    text = text.lower()
    text = text.replace('\n', ' ')
    return ''.join([char for char in text if char not in chars_to_remove])


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


def word_phonetic(word: str) -> str:
    accented = accentor.predict(word)
    vowel_position = 0

    try:
        for i in range(len(word)):
            if word[i] in vowels:
                vowel_position += 1

            if accented == i:
                break

        return phonetic_module.Phonetic(word, vowel_position).get_phonetic()
    except Exception:
        return word


def tokens_phonetic(tokens: list[str]) -> list[str]:
    phonetic_tokens: list[str] = []
    for token in tokens:
        phonetic_tokens.append(word_phonetic(token))

    return phonetic_tokens


def count_sounds(tokens: list[str]) -> dict[str, int]:
    sounds_count = dict[str, int]()

    previous_letter = ''
    for token in tokens:
        for letter in token:
            if letter == '\'' and previous_letter != '':
                if f'{previous_letter}\'' not in sounds_count:
                    sounds_count[f'{previous_letter}\''] = 0
                sounds_count[f'{previous_letter}\''] += 1
                sounds_count[previous_letter] -= 1
            else:
                if letter not in sounds_count:
                    sounds_count[letter] = 0
                sounds_count[letter] += 1

            previous_letter = letter

    return sounds_count


def count_letters(tokens: list[str]) -> dict[str, int]:
    letters_count = dict[str, int]()
    for token in tokens:
        for letter in token:
            if letter == '\'':
                continue

            if letter not in letters_count:
                letters_count[letter] = 0

            letters_count[letter] += 1

    return letters_count
