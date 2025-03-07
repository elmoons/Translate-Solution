from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_DIR_EN_RU = "models/opus-mt-en-ru"
MODEL_DIR_RU_EN = "models/opus-mt-ru-en"
MODEL_DIR_LV_RU = "models/opus-mt-lv-ru"
MODEL_DIR_RU_LV = "models/opus-mt-ru-lv"
MODEL_DIR_ET_RU = "models/opus-mt-et-ru"
MODEL_DIR_RU_ET = "models/opus-mt-ru-et"
MODEL_DIR_NO_RU = "models/opus-mt-no-ru"
MODEL_DIR_RU_NO = "models/opus-mt-ru-no"

# Скачиваем модели в папку

# Английский
tokenizer_en_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model_en_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
tokenizer_en_ru.save_pretrained(MODEL_DIR_EN_RU)
model_en_ru.save_pretrained(MODEL_DIR_EN_RU)

tokenizer_ru_en = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
model_ru_en = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
tokenizer_ru_en.save_pretrained(MODEL_DIR_RU_EN)
model_ru_en.save_pretrained(MODEL_DIR_RU_EN)

# Латышский
tokenizer_lv_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-lv-ru")
model_lv_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-lv-ru")
tokenizer_lv_ru.save_pretrained(MODEL_DIR_LV_RU)
model_lv_ru.save_pretrained(MODEL_DIR_LV_RU)

tokenizer_ru_lv = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-lv")
model_ru_lv = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-lv")
tokenizer_ru_lv.save_pretrained(MODEL_DIR_RU_LV)
model_ru_lv.save_pretrained(MODEL_DIR_RU_LV)

# Эстонский
tokenizer_et_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-et-ru")
model_et_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-et-ru")
tokenizer_et_ru.save_pretrained(MODEL_DIR_ET_RU)
model_et_ru.save_pretrained(MODEL_DIR_ET_RU)

tokenizer_ru_et = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-et")
model_ru_et = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-et")
tokenizer_ru_et.save_pretrained(MODEL_DIR_RU_ET)
model_ru_et.save_pretrained(MODEL_DIR_RU_ET)

# Норвежский
tokenizer_no_ru = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-no-ru")
model_no_ru = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-no-ru")
tokenizer_no_ru.save_pretrained(MODEL_DIR_NO_RU)
model_no_ru.save_pretrained(MODEL_DIR_NO_RU)

tokenizer_ru_no = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-no")
model_ru_no = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-no")
tokenizer_ru_no.save_pretrained(MODEL_DIR_RU_NO)
model_ru_no.save_pretrained(MODEL_DIR_RU_NO)


print("✅ Модели скачаны и сохранены!")
