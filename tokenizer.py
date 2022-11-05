
from typing import List, re


class Tokenizer:

    def tokenize(self, text: str) -> List[str]:
        line = re.sub(r'(\W)', r' \1 ', text.lower())
        adjusted = re.sub(r'(\w) \' (\w)', r"\1'\2", line)
        with_ellipses = re.sub(r'\.\s+\.\s+\.', '...', adjusted)
        split_tokens = with_ellipses.split()
        return split_tokens

