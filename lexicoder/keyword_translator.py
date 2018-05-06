# -*- coding: utf-8 -*-
from .lexer import Lexer, LexerEOF


class KeywordTranslator:
    _KEYWORDS = {
        'for': 'for_replaced',
        'in': 'in_replaced',
        'print': 'print_replaced'
    }
    _SPECIALS = ['\n', '[', ']', '(', ')', '{', '}']

    def __init__(self, text: str):
        self.text = text
        self.output_stream = []
        self.lexer = Lexer(self.text)

    def translate(self):
        try:
            while True:
                token = self.lexer.get()
                transformed = token
                if token in KeywordTranslator._KEYWORDS:
                    transformed = KeywordTranslator._KEYWORDS[token]
                self.output_stream.append(transformed)
        except LexerEOF:
            pass

    def flush_to_path(self, output_path: str):
        with open(output_path, 'w+') as output_file:
            output_file.write(''.join(self.output_stream))
