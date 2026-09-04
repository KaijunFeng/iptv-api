#!/usr/bin/env python3
import re
from pathlib import Path

INPUT_PATH = Path('output/result.txt')
OUTPUT_PATH = Path('output/result_filtered.txt')

CATEGORY_KEYWORDS = ["央视频道", "港·澳·台"]
LINE_KEYWORDS = ["CCTV", "香港", "澳门", "台湾"]

def main():
    if not INPUT_PATH.exists():
        print(f"Input file {INPUT_PATH} not found")
        return
    with INPUT_PATH.open('r', encoding='utf-8') as f_in, OUTPUT_PATH.open('w', encoding='utf-8') as f_out:
        lines = f_in.readlines()
        if lines and '#genre#' in lines[0]:
            # keep update time header
            f_out.write(lines[0])
            if len(lines) > 1:
                f_out.write(lines[1])
        keep = False
        for line in lines[2:]:
            stripped = line.strip()
            if '#genre#' in stripped:
                keep = any(keyword in stripped for keyword in CATEGORY_KEYWORDS)
                if keep:
                    f_out.write(line)
                continue
            if keep or any(keyword in stripped for keyword in LINE_KEYWORDS):
                f_out.write(line)

if __name__ == '__main__':
    main()
