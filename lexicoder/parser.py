# -*- coding: utf-8 -*-
import os

from .lexer import Lexer


class ParseError(Exception):
    pass


class Parser(object):
    def __init__(self, text):
        self.lexer = Lexer(text)

    def match(self, expected: str):
        """Consume the next token, and verify it matches an expected value
        This method will throw a ParseError if the next token did not match the expected value
        """
        real_tok = self._get_tok()
        if real_tok != expected:
            raise ParseError('Expected token {}, got {}'.format(repr(expected), repr(real_tok)))

