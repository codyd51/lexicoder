# -*- coding: utf-8 -*-
import os
import argparse
from lexicoder import KeywordTranslator


parser = argparse.ArgumentParser(
    description='Translate source-code keywords from foreign to host language. '
                'Translated source code is written to <input file>_translated.<extension>'
)
parser.add_argument(
    'input_files', metavar='input_files', type=str, nargs='+', help=
    'One or more files to translate'
)
args = parser.parse_args()

for input_file in args.input_files:
    with open(input_file, 'r') as code_file:
        translator = KeywordTranslator(code_file.read())

    translator.translate()

    filename, extension = os.path.basename(input_file).split('.')
    output_filename = f'{filename}_translated.{extension}'
    output_path = os.path.join(os.path.dirname(input_file), output_filename)
    translator.flush_to_path(output_path)
