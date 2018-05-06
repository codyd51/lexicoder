# -*- coding: utf-8  -*-
import re
from typing import List, Optional


class Lexer(object):
    """Transform a text stream into a token stream
    """
    def __init__(self, text: str):
        self.text = text
        self._tokens = self._split_stream()
        self._token_index = 0

    def peek(self) -> Optional[str]:
        """Return the next token in the parse stream, without consuming it
        """
        if self._token_index >= len(self._tokens):
            raise LexerEOF()
        return self._tokens[self._token_index]

    def get(self) -> str:
        """Return and consume the next token in the parse stream
        Raises LexerEOF once the token stream is exhausted
        """
        tok = self.peek()
        self._token_index += 1
        return tok

    def _split_stream(self) -> List[str]:
        return re.findall(r"[\w']+|[*+@.,!#?;():/\-\[\]\n\"\\\ ]", self.text)

