#!/usr/bin/env python2

import nltk
import sys

assert len(sys.argv) == 2

with open(sys.argv[1]) as f:
  print(map(nltk.tokenize.word_tokenize,
            nltk.tokenize.sent_tokenize(f.read())))
