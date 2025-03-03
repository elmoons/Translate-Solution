import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Указываем путь к локальной папке с моделями
MODEL_PATH_EN_RU = "C:/models/opus-mt-en-ru"
MODEL_PATH_RU_EN = "C:/models/opus-mt-ru-en"

# Загружаем токенизаторы и модели из локальных папок
tokenizer_en_ru = AutoTokenizer.from_pretrained(MODEL_PATH_EN_RU, local_files_only=True)
model_en_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_EN_RU, local_files_only=True)
model_en_ru.eval()  # Отключаем градиенты

tokenizer_ru_en = AutoTokenizer.from_pretrained(MODEL_PATH_RU_EN, local_files_only=True)
model_ru_en = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH_RU_EN, local_files_only=True)
model_ru_en.eval()

# Функция для перевода
def batch_translate(texts, tokenizer, model):
    if not texts:
        return []

    inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        translated = model.generate(**inputs)

    return tokenizer.batch_decode(translated, skip_special_tokens=True)

def translate_from_en_to_ru(words):
    return batch_translate(words, tokenizer_en_ru, model_en_ru)

def translate_from_ru_to_en(words):
    return batch_translate(words, tokenizer_ru_en, model_ru_en)
