#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

d1s = []
d2s = []

with open('result.txt') as r:
	for i, line in enumerate(r.readlines()):
		line_strip = line.rstrip()
		try:
			xs = line_strip.split()
			assert len(xs) == 3, 'Malformed data row'
			honzis, jyutpings, _ = xs

			honzi_list = list(honzis)
			jyutpings_lower = jyutpings.lower()
			jyutping_list = re.split(r'(?<=[1-6])(?!$)', jyutpings_lower)
			assert len(honzi_list) == len(jyutping_list), 'Lengths do not match'

			for honzi in honzi_list:
				# https://stackoverflow.com/a/2718268
				assert re.match(r'[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]', honzi), 'Not a Chinese character'

			for jyutping in jyutping_list:
				assert re.match(r'[a-z]+[1-6]', jyutping), 'Malformed Jyutping'

			(d1s if len(honzi_list) == 1 else d2s).append((honzis, ' '.join(jyutping_list)))

		except AssertionError as e:
			print(f'Line {i + 1}: "{line_strip}", {" ".join(e.args)}', file=sys.stderr)

with open('sanitized.txt', 'w') as f:
	for a, b in d1s:
		print(f'{a}\t{b}', file=f)
	for a, b in d2s:
		print(f'{a}\t{b}', file=f)
