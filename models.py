import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Указываем путь к локальной папке с моделями
MODEL_PATH_EN_RU = "C:/models/opus-mt-en-ru"
MODEL_PATH_RU_EN = "C:/models/opus-mt-ru-en"
MODEL_PATH_LV_RU = "C:/models/opus-mt-lv-ru"
MODEL_PATH_RU_LV = "C:/models/opus-mt-ru-lv"
MODEL_PATH_ET_RU = "C:/models/opus-mt-et-ru"
MODEL_PATH_RU_ET = "C:/models/opus-mt-ru-et"
MODEL_PATH_NO_RU = "C:/models/opus-mt-no-ru"
MODEL_PATH_RU_NO = "C:/models/opus-mt-ru-no"

# Загружаем токенизаторы и модели из локальных папок

# Английский
tokenizer_en_ru = AutoTokenizer.from_pretrained(MODEL_PATH_EN_RU, local_files_only=True)
model_en_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_EN_RU, local_files_only=True)
model_en_ru.eval()  # Отключаем градиенты

tokenizer_ru_en = AutoTokenizer.from_pretrained(MODEL_PATH_RU_EN, local_files_only=True)
model_ru_en = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_RU_EN, local_files_only=True)
model_ru_en.eval()


# Латышский
tokenizer_lv_ru = AutoTokenizer.from_pretrained(MODEL_PATH_LV_RU, local_files_only=True)
model_lv_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_LV_RU, local_files_only=True)
model_lv_ru.eval()  # Отключаем градиенты

tokenizer_ru_lv = AutoTokenizer.from_pretrained(MODEL_PATH_RU_LV, local_files_only=True)
model_ru_lv = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_RU_LV, local_files_only=True)
model_ru_lv.eval()


# Эстонский
tokenizer_et_ru = AutoTokenizer.from_pretrained(MODEL_PATH_ET_RU, local_files_only=True)
model_et_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_ET_RU, local_files_only=True)
model_et_ru.eval()  # Отключаем градиенты

tokenizer_ru_et = AutoTokenizer.from_pretrained(MODEL_PATH_RU_ET, local_files_only=True)
model_ru_et = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_RU_ET, local_files_only=True)
model_ru_et.eval()


# Норвежский
tokenizer_no_ru = AutoTokenizer.from_pretrained(MODEL_PATH_NO_RU, local_files_only=True)
model_no_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_NO_RU, local_files_only=True)
model_no_ru.eval()  # Отключаем градиенты

tokenizer_ru_no = AutoTokenizer.from_pretrained(MODEL_PATH_RU_NO, local_files_only=True)
model_ru_no = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_RU_NO, local_files_only=True)
model_ru_no.eval()


# Функция для перевода
def batch_translate(texts, tokenizer, model):
    if not texts:
        return []

    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        translated = model.generate(**inputs)

    return tokenizer.batch_decode(translated, skip_special_tokens=True)


# Английский
def translate_from_en_to_ru(words):
    return batch_translate(words, tokenizer_en_ru, model_en_ru)


def translate_from_ru_to_en(words):
    return batch_translate(words, tokenizer_ru_en, model_ru_en)


# Латышский
def translate_from_lv_to_ru(words):
    return batch_translate(words, tokenizer_lv_ru, model_lv_ru)


def translate_from_ru_to_lv(words):
    return batch_translate(words, tokenizer_ru_lv, model_ru_lv)


# Эстонский
def translate_from_et_to_ru(words):
    return batch_translate(words, tokenizer_et_ru, model_et_ru)


def translate_from_ru_to_et(words):
    return batch_translate(words, tokenizer_ru_et, model_ru_et)


# Норвежский
def translate_from_no_to_ru(words):
    return batch_translate(words, tokenizer_no_ru, model_no_ru)


def translate_from_ru_to_no(words):
    return batch_translate(words, tokenizer_ru_no, model_ru_no)
