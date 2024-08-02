import pytest
import re
from encoder_decoder import EnDec


@pytest.fixture()
def endec():
    endec = EnDec()
    return endec


def test_encoder_initialization(endec):
    assert endec.separator == "\n-weird-\n"


@pytest.mark.parametrize("original, after_shuffle", (
        ("a", "a"),
        ("że", "że"),
        ("bit", "bit"),
        ("biiiiiiig", "biiiiiiig")
))
def test_encode_not_shuffled_string(endec, original, after_shuffle):
    assert endec.shuffle_string(original) == after_shuffle


@pytest.mark.parametrize("original", (
        "long",
        "loooooong",
        "żółcień",
        "You've"
))
def test_shuffled_string(endec, original):
    shuffled = endec.shuffle_string(original)
    assert shuffled != original
    assert len(shuffled) == len(original)
    assert shuffled[0] == original[0]
    assert shuffled[-1] == original[-1]


@pytest.mark.parametrize("text, isolated", (
        ("1 Tekst bez interpunkcji", ["1", " ", "Tekst", " ", "bez", " ", "interpunkcji"]),
        ("I'm here. (Żółć?)", ["I'm", " ", "here", ".", " ", "(", "Żółć", "?", ")"])
))
def test_isolate_tokens(endec, text, isolated):
    assert endec.isolate_tokens(text) == isolated


def test_encode_text_format(endec):
    original = "To jest oryginalny tekst!"
    encoded = endec.encode_text(original)
    reg = re.compile(rf"{endec.separator}\s*.*?\s*{endec.separator}\s*.*?")
    assert bool(reg.fullmatch(encoded))


@pytest.mark.parametrize("original_text, changed_words", (
        ("To jest ten oryginalny tekst: Żółć. You're welcome. I'm not.",
         ["jest", "oryginalny", "tekst", "Żółć", "You're", "welcome"]),
        ("To jest jedno, to jest drugie", ["jest", "jedno", "drugie"]) # check no duplicates
))
def test_encode_text_changed_words(endec, original_text, changed_words):
    encoded_text = endec.encode_text(original_text)

    _, text, original_shuffled_words = encoded_text.split(endec.separator)

    assert sorted(changed_words) == original_shuffled_words.split()


@pytest.mark.parametrize("shuffled, original_words, decoded", (
        ("book", ["brak", "barman", "hamak"], "book"),
        ("że", ["brak", "barman", "hamak"], "że"),
        (" ", [], " "),
        ("braamn", ["brak", "barman", "hamak"], "barman"),
))
def test_decode_string(endec, shuffled, original_words, decoded):
    assert endec.decode_string(shuffled, original_words) == decoded


@pytest.mark.parametrize("shuffled, original_words, decoded", (
        ("book", ["brak", "barman", "hamak"], "book"),
        ("że", ["brak", "barman", "hamak"], "że"),
        (" ", [], " "),
        ("braamn", ["brak", "barman", "hamak"], "barman"),
))
def test_decode_string(endec, shuffled, original_words, decoded):
    assert endec.decode_string(shuffled, original_words) == decoded


@pytest.mark.parametrize("shuffled, original_words", (
        ("biawk", ["brak", "barman", "hamak"]),
))
def test_decode_string_exception_no_original_word(endec, shuffled, original_words):
    with pytest.raises(Exception):
        endec.decode_string(shuffled, original_words)


def test_decode_text_format_exception(endec):
    encoded = f"Ala ma kota {endec.separator} Tak"
    with pytest.raises(Exception):
        endec.decode_text(encoded)


def test_decode_text(endec):
    encoded = f"{endec.separator}To jset ten tkest: Żłóć. Yur'oe weomcle. I'm not.{endec.separator}jest tekst Żółć You're welcome"
    decoded = endec.decode_text(encoded)
    assert decoded == "To jest ten tekst: Żółć. You're welcome. I'm not."


# allow mistakes in "barek" and "break"
def test_decode_text_allow_mistake(endec):
    encoded = f"{endec.separator}To jset berak, to jset beark.{endec.separator}jest barek break"
    decoded = endec.decode_text(encoded)

    valid_combinations = [
        "To jest barek, to jest barek.",
        "To jest break, to jest break.",
        "To jest break, to jest barek.",
        "To jest barek, to jest break.",
    ]

    assert decoded in valid_combinations










