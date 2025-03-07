import pandas as pd
from models import translate_from_en_to_ru, translate_from_ru_to_en, translate_from_lv_to_ru, translate_from_ru_to_lv, \
    translate_from_et_to_ru, translate_from_ru_to_et, translate_from_no_to_ru, translate_from_ru_to_no


def process_excel(input_path: str, output_path: str, language: str, direction: str):
    # Загружаем данные из Excel
    df_input = pd.read_excel(input_path, header=None)

    # Фильтруем пустые строки и запоминаем индексы
    words = df_input[0].dropna().astype(str)
    indexes = words.index  # Индексы непустых строк

    # Переводим слова
    # Английский
    if direction == "на Русский" and language == "Английский":
        translated_words = translate_from_en_to_ru(words.tolist())
    elif direction == "на выбранный" and language == "Английский":
        translated_words = translate_from_ru_to_en(words.tolist())
    # Латышский
    elif direction == "на Русский" and language == "Латышский":
        translated_words = translate_from_lv_to_ru(words.tolist())
    elif direction == "на выбранный" and language == "Латышский":
        translated_words = translate_from_ru_to_lv(words.tolist())
    # Эстонский
    elif direction == "на Русский" and language == "Эстонский":
        translated_words = translate_from_et_to_ru(words.tolist())
    elif direction == "на выбранный" and language == "Эстонский":
        translated_words = translate_from_ru_to_et(words.tolist())
    # Норвежский
    elif direction == "на Русский" and language == "Норвежский":
        translated_words = translate_from_no_to_ru(words.tolist())
    elif direction == "на выбранный" and language == "Норвежский":
        translated_words = translate_from_ru_to_no(words.tolist())

    # Вставляем перевод обратно с сохранением индексов
    df_input.loc[indexes, 1] = translated_words

    # Сохраняем результат в файл
    df_input.to_excel(output_path, index=False, header=False)
