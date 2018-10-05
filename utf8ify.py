#!/usr/bin/env python3
import codecs
import chardet
import sys

if len(sys.argv) < 2:
    print('Usage: utf8ify FILE', file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    cont = f.read()

enc = chardet.detect(cont)['encoding']
if enc is None:
    print('Failed to detect encoding', file=sys.stderr)
    sys.exit(1)

cont = codecs.decode(cont, enc)
with open(sys.argv[1], 'w') as f:
    f.write(cont)
