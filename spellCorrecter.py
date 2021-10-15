from hanspell import spell_checker


def spell_corrector(text):
    spellChecker = spell_checker.check(text)
    spellSender = spellChecker.checked

    print(spellChecker)
    print(spellSender)

    return spellSender


if __name__ == "__main__":
    spell_corrector("외 않돼? 이런 말들을 써서 맞춤법검사기의 성능을 검사하고 있습니다.")
