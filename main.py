import nltk
import matplotlib

import plotter
import text_processor
import texts_loader

texts_dict = texts_loader.load_texts()
text_processor.prepare_texts(texts_dict)

tokenized_texts = dict[str, list[str]]()

for style in texts_dict:
    merged_texts = ''

    for text in texts_dict[style]:
        tokens = nltk.word_tokenize(text, 'russian')
        tokens = text_processor.prepare_tokens(tokens)
        tokens = text_processor.tokens_phonetic(tokens)

        nltk_text = nltk.Text(tokens)
        most_common = nltk.probability.FreqDist(nltk_text).most_common(50)

        plotter.plot_text(f'Самые частые слова текста "{text[0:30]}" для стиля "{style}"', most_common)
        plotter.plot_sounds(f'Самые частые буквы текста "{text[0:30]}" для стиля "{style}"', text_processor.count_letters(tokens))
        plotter.plot_sounds(f'Самые частые звуки текста "{text[0:30]}" для стиля "{style}"', text_processor.count_sounds(tokens))
