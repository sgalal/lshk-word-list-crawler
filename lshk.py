#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import requests

pattern = re.compile(r'<tr>\s*<td>(?P<honzi>.*?)<\/td>\s*<td>(?P<jyutping>.*?)<\/td>\s*<td class=\"hidden-xs\">(?P<loijyun>.*?)<\/td>[\s\S]*?<\/tr>')

i = 1

with open('result.txt', 'w') as f:
	while True:
		r = requests.post('http://corpus.eduhk.hk/JPwordlist/page.php', data={'num': i})
		xs = [(match['honzi'], match['jyutping'], match['loijyun']) for match in pattern.finditer(r.text)]
		if not xs:
			break
		for x in xs:
			print(*x, file=f)
		i += 1
