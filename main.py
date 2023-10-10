import nltk

import text_processor
import texts_loader

texts_dict = texts_loader.load_texts()
text_processor.prepare_texts(texts_dict)

merged_texts = ''

for style in texts_dict:
    for text in texts_dict[style]:
        merged_texts += text
        merged_texts += ' '

tokens = nltk.word_tokenize(merged_texts, 'russian')
tokens = text_processor.prepare_tokens(tokens)

nltk_text = nltk.Text(tokens)
nltk_text.plot()
