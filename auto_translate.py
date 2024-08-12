import translators as ts

with open('corpus.txt', 'r', encoding='utf-8') as file:
    data_en: str = file.read()

print(data_en[1:100:1])

params = {
  'query_text': data_en[1:1000:1],
  'from_language': 'en',
  'to_language': 'ru',
  'update_session_after_freq': 1,
  # 'if_show_time_stat' : True,
}

# Строка с предложением
sentence = ts.translate_text(**params, translator='google')

# Открытие файла в режиме записи
with open("corpus_auto-translate.txt", "w", encoding='utf-8') as file:
    # Запись строки в файл
    file.write(sentence)

