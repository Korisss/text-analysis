import os

textsDir = './texts'


def load_texts() -> dict[str, list[str]]:
    texts = dict[str, list[str]]()

    for style in os.listdir(textsDir):
        file_names = os.listdir(f'{textsDir}/{style}')
        if len(file_names) > 0:
            texts[style] = []

        for fileName in file_names:
            texts[style].append(open(f'{textsDir}/{style}/{fileName}', 'r', encoding='utf-8').read())

    return texts
