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
            return None

        tok = self._tokens[self._token_index]

        # the lexer will automatically skip over comments
        if tok == '/':
            # is this the start of a line comment? //
            if self._tokens[self._token_index+1] == '/' or self._tokens[self._token_index - 1] == '/':
                # skip comment tokens
                next_idx = self._token_index + 1
                while self._tokens[next_idx] != '\n':
                    if next_idx + 1 >= len(self._tokens):
                        return None
                    next_idx += 1
                # now, skip the newline
                self._token_index = next_idx + 1

            # is this the start of a block comment? /*
            # check if this is the start of a block comment
            elif self._tokens[self._token_index+1] == '*':
                # first, ensure that we're not parsing this construct:
                # // * comment here
                # the lexer throws away spaces, so the above and a real block comment token would look the same
                # to check if this is the case or not, we must check the indexes of the '/' and '*' within
                # the source and see if they're right next to each other

                # skip block comment
                # tokens[token_index+0] = '/'
                # tokens[token_index+1] = '*'
                # tokens[token_index+2] = contents of block content
                next_idx = self._token_index+2
                while True:
                    while '*' not in self._tokens[next_idx]:
                        # keep eating block comment
                        next_idx += 1
                    if self._tokens[next_idx+1] == '/':
                        # end of block comment
                        # set next_idx to the next token after the end of the block comment
                        next_idx += 2
                        break
                    else:
                        # keep eating
                        next_idx += 1

                self._token_index = next_idx

        if self._token_index >= len(self._tokens):
            return None
        return self._tokens[self._token_index]

    def get(self) -> str:
        """Return and consume the next token in the parse stream
        """
        tok = self.peek()
        self._token_index += 1
        return tok

    @staticmethod
    def _split_stream(stream: str) -> List[str]:
        return re.findall(r"[\w']+|[*+@.,!#?;():/\-\[\]\n\"\\]", stream)

