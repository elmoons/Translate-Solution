from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_DIR_EN_RU = "models/opus-mt-en-ru"
MODEL_DIR_RU_EN = "models/opus-mt-ru-en"

try:
    tokenizer_en_ru = AutoTokenizer.from_pretrained(MODEL_DIR_EN_RU, local_files_only=True)
    model_en_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_EN_RU, local_files_only=True)

    tokenizer_ru_en = AutoTokenizer.from_pretrained(MODEL_DIR_RU_EN, local_files_only=True)
    model_ru_en = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_RU_EN, local_files_only=True)

    print("✅ Модели загружены успешно!")
except Exception as e:
    print("❌ Ошибка загрузки модели:", e)
