from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_DIR_EN_RU = "models/opus-mt-en-ru"
MODEL_DIR_RU_EN = "models/opus-mt-ru-en"

# Скачиваем модели в папку
tokenizer_en_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model_en_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
tokenizer_en_ru.save_pretrained(MODEL_DIR_EN_RU)
model_en_ru.save_pretrained(MODEL_DIR_EN_RU)

tokenizer_ru_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
model_ru_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
tokenizer_ru_en.save_pretrained(MODEL_DIR_RU_EN)
model_ru_en.save_pretrained(MODEL_DIR_RU_EN)

print("✅ Модели скачаны и сохранены!")
