from preprocessing import clear_special_mark
from tokenizer import kor_manuscript_spacer, kor_sentence_separater
from spellCorrecter import spell_corrector

if __name__ == "__main__":
    text = "저희는![*&자필원고지 인식을 하고 이후의 마춤뻡 검사를 하는 프로그램을 작성하고 있습니다. 원고지는 인쇄술이 발달하면서 글의 분량을 확인하기 위해 고안된 용지 입니다. 글씨체는 사람 마다 다르 지만, 원고지에 글을 쓰면 글자 크기에 관계업이 원고의 양을 가늠할쑤 있기 때문입니다."
    print(f"\nRaw Data : {text}\n")
    text = clear_special_mark(text)
    print(f"clear_special_mark : {text}\n")
    text = kor_manuscript_spacer(text)
    print(f"spaing : {text}\n")
    text = spell_corrector(text)
    print(f"\nspell check : {text}\n")
