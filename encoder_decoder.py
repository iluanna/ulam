import random
import re
from typing import List


class EnDec:
    """
    Encoder and Decoder. For each original word in the original text, leaves the first and last character of it in that
    position, but shuffles (permutate) all the characters in the middle of the word. Encoder output contains encoded text (with shuffled words) and a sorted list of original words (only words that got shuffled).
    """
    def __init__(self):
        self.separator = '\n-weird-\n'
    
    def encode_text(self, original_text: str) -> str:
        encoded_list = []
        changed_strings_list = []

        tokens = self.isolate_tokens(original_text)

        for t in tokens:
            shuffled = self.shuffle_string(t)
            encoded_list.append(shuffled)
            if shuffled != t:
                changed_strings_list.append(t)

        encoded_text = ''.join(encoded_list)
        changed_strings = ' '.join((sorted(set(changed_strings_list))))

        final = f"{self.separator}{encoded_text}{self.separator}{changed_strings}"
        return final
    
    def decode_text(self, encoded_text: str) -> str:
        reg = re.compile(rf"{self.separator}\s*.*?\s*{self.separator}\s*.*?", re.DOTALL)
        if not bool(reg.fullmatch(encoded_text)):
            raise Exception(
                "Encoded text doesn't have a correct format (separator)")

        _, text, original_words = encoded_text.split(self.separator)

        tokens = self.isolate_tokens(text)

        decoded_list = []

        for t in tokens:
            decoded = self.decode_string(t, original_words.split())
            decoded_list.append(decoded)

        decoded_text = ''.join(decoded_list)
        return decoded_text

    def decode_string(self, shuffled: str, original_words: List[str]) -> str:
        if len(shuffled) <= 3 or len(set(shuffled[1:-1])) == 1:
            # If the string is too short to shuffle or there is only one type of letter in the middle, leave it as is
            return shuffled
        
        for word in original_words:
            if word[0] == shuffled[0] and word[-1] == shuffled[-1] and sorted(shuffled[1:-1]) == sorted(word[1:-1]) and word != shuffled:
                return word
        raise Exception(f"No matching word in original words for: {shuffled}")

    def shuffle_string(self, s: str) -> str:
        if len(s) <= 3 or len(set(s[1:-1])) == 1:
            # If the string is too short to shuffle or there is only one type of letter in the middle, leave it as is
            return s
        
        middle = list(s[1:-1])
        middle_original = middle[:]  # not the same object
        random.shuffle(middle)

        # If possible, the resulting “encoded” word MUST NOT be the same as the original word
        while True:
            random.shuffle(middle)
            if middle != middle_original:
                break
        
        shuffled_string = s[0] + ''.join(middle) + s[-1]
        return shuffled_string
    
    def isolate_tokens(self, text: str) -> List[str]:
        # Isolates every word, punctuation sings, spaces and other non-letter chars, exept the ' sign
        # I assume that a word with the ' sign is one word (e.g. "You've" or "I'm")
        tokenize_re = re.compile(r"(\w+('\w+)?|[^\w\s]|\s+)", re.U)
        tokens = tokenize_re.findall(text)
        tokens = [match[0] for match in tokens]
        return tokens
