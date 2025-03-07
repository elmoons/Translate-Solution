from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_DIR_EN_RU = "models/opus-mt-en-ru"
MODEL_DIR_RU_EN = "models/opus-mt-ru-en"
MODEL_DIR_LV_RU = "models/opus-mt-lv-ru"
MODEL_DIR_RU_LV = "models/opus-mt-ru-lv"
MODEL_DIR_ET_RU = "models/opus-mt-et-ru"
MODEL_DIR_RU_ET = "models/opus-mt-ru-et"
MODEL_DIR_NO_RU = "models/opus-mt-no-ru"
MODEL_DIR_RU_NO = "models/opus-mt-ru-no"

try:
    # Английский
    tokenizer_en_ru = AutoTokenizer.from_pretrained(MODEL_DIR_EN_RU, local_files_only=True)
    model_en_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_EN_RU, local_files_only=True)

    tokenizer_ru_en = AutoTokenizer.from_pretrained(MODEL_DIR_RU_EN, local_files_only=True)
    model_ru_en = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_RU_EN, local_files_only=True)

    # Латышский
    tokenizer_lv_ru = AutoTokenizer.from_pretrained(MODEL_DIR_LV_RU, local_files_only=True)
    model_lv_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_LV_RU, local_files_only=True)

    tokenizer_ru_lv = AutoTokenizer.from_pretrained(MODEL_DIR_RU_LV, local_files_only=True)
    model_ru_lv = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_RU_LV, local_files_only=True)

    # Эстонский
    tokenizer_et_ru = AutoTokenizer.from_pretrained(MODEL_DIR_ET_RU, local_files_only=True)
    model_et_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_ET_RU, local_files_only=True)

    tokenizer_ru_et = AutoTokenizer.from_pretrained(MODEL_DIR_RU_ET, local_files_only=True)
    model_ru_et = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_RU_ET, local_files_only=True)

    # Норвежский
    tokenizer_no_ru = AutoTokenizer.from_pretrained(MODEL_DIR_NO_RU, local_files_only=True)
    model_no_ru = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_NO_RU, local_files_only=True)

    tokenizer_ru_no = AutoTokenizer.from_pretrained(MODEL_DIR_RU_NO, local_files_only=True)
    model_ru_no = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR_RU_NO, local_files_only=True)

    print("✅ Модели загружены успешно!")
except Exception as e:
    print("❌ Ошибка загрузки модели:", e)
