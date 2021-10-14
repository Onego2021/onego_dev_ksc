import re


def clear_special_mark(text):
    return_text = re.sub(
        "[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]", "", text)
    return return_text.replace(" ", "")


if __name__ == "__main__":
    text = clear_special_mark("이 문장은 & *(""특수문자를 제거하기 위한''''테스트 케이스입니다.")
    print(f"remove_special_mark :  {text}")
