"""Word check: every paragraph of each act's latest version must occur, word for word, in an independent text
extraction (poppler's pdftotext, not PyMuPDF) of the same official PDF. Also checks the first version of each act.

    python -X utf8 scripts/palau-law/verify.py        -> writes verification.json, prints a summary
Normalisation on both sides: quotes, dashes, whitespace and line-wrap hyphenation only.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch  # noqa: E402

DRIVE_FILE = 'https://drive.google.com/uc?export=download&id={}'


def norm(s: str) -> str:
    s = s.replace('‘', "'").replace('’', "'").replace('“', '"').replace('”', '"')
    s = s.replace('–', '-').replace('—', '-').replace(' ', ' ').replace('­', '')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def pdftext(file_id: str) -> str:
    p = fetch.path(DRIVE_FILE.format(file_id))
    r = subprocess.run(['pdftotext', '-enc', 'UTF-8', str(p), '-'], capture_output=True)
    t = r.stdout.decode('utf-8', 'replace')
    t = re.sub(r'(\w)-\n(\w)', r'\1-\2', t)  # keep hyphen, drop the wrap
    return norm(t)


def main() -> None:
    corpus = json.loads((HERE / 'corpus.json').read_text(encoding='utf-8'))
    report = {}
    total_bad = 0
    for act in corpus['acts']:
        for which in ('first', 'last'):
            v = act['versions'][0] if which == 'first' else act['versions'][-1]
            fid = re.search(r'/d/([\w-]+)/', v['source_url']).group(1)
            hay = pdftext(fid)
            hay_ns = hay.replace(' ', '')
            paras = bad = 0
            misses = []
            for k, u in sorted(v['units'].items()):
                for line in u['text'].rstrip('\n').split('\n'):
                    if line.startswith('# Article') or line.startswith('# Preamble') or line.startswith('# ') and 'Amendment' in line:
                        continue  # headings composed by parse.py from the article/amendment heading
                    line = line[2:] if line.startswith('# ') else line
                    paras += 1
                    n = norm(line)
                    # pdftotext may split words differently around line ends: compare without spaces as the fallback
                    if n not in hay and n.replace(' ', '') not in hay_ns:
                        bad += 1
                        misses.append(f'{k}: {n[:160]}')
            report[f'{act["slug"]}@{v["from"]}'] = {'paragraphs': paras, 'not_found': bad, 'examples': misses[:15]}
            total_bad += bad
            print(f'{act["slug"]:32} {v["from"]} paragraphs {paras:5}  not found {bad}')
    (HERE / 'verification.json').write_text(json.dumps(report, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    print('total not found', total_bad)


if __name__ == '__main__':
    main()
