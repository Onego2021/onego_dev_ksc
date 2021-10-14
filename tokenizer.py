from pykospacing import Spacing
import kss


def kor_manuscript_spacer(kor_manuscript_text):
    spacing = Spacing()
    return spacing(kor_manuscript_text)


def kor_sentence_separater(kor_manuscript_text):
    return kss.split_sentences(kor_manuscript_text)


if __name__ == "__main__":
    text = kor_manuscript_spacer("띄어쓰기안하니까화나지?하지만난띄어쓰기안해줄껀데요.약오르지그렇지만어쩔수없는걸.")
    print(f"kor_manuscript_spacer : {text}")
    text = kor_sentence_separater(text)
    print(f"kor_sentence_separater : {text}")
