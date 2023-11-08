import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from langdetect import detect
def trans():
    # Loading the model
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
    tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

    # Specify the path to the input file
    input_file_path = 'D:/Capstone/Blabber/blabber_models/voice_cloning/translate text/recorded_audio.txt'

    # Read the contents of the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_text = file.read()

    # Initialize the translated_text variable
    translated_text = ""
    # Detect the source language
    source_lang = detect(input_text)
    print(source_lang)
    if source_lang == "en" :
        # Creating the pipeline and translating from detected source to target language
        translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="eng_Latin" , tgt_lang="hin_Deva", max_length=400)
        # Perform the translation
        translated_text = translator(input_text)
        
    elif source_lang=="hi" or source_lang=="ur" :
        translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="hindi_Deva" or "urdu_Urdu", tgt_lang="eng_Latin", max_length=400)
        # Perform the translation
        translated_text = translator(input_text)

    # Specify the path for the output file
    output_file_path = 'D:\\Capstone\\Blabber\\blabber_models\\voice_cloning\\translated text\\translated_output.txt'

    # Write the translated text to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(translated_text[0]['translation_text'])

    print(f"Translation saved to {output_file_path}")
