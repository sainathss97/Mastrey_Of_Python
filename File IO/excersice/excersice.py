from translate import Translator
try:
    with open('C:/Study/Python/Python Advance Concepts/File IO/excersice/test.txt', 'r') as f:
        text = f.read()
        translator = Translator(to_lang="ja")
        translation_text = translator.translate(text)
        print(translation_text)

    with open('C:/Study/Python/Python Advance Concepts/File IO/excersice/test_ja.txt', 'w', encoding="utf-8") as f:
        f.write(translation_text)
except FileNotFoundError as err:
    print(f"File not found-{err}")
