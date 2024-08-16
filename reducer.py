#!/usr/bin/env python3
import sys

current_word = None
current_count = 0
word = None

# Membaca input dari stdin
for line in sys.stdin:
    # Menghapus spasi di awal dan akhir
    line = line.strip()

    # Memisahkan input dari mapper.py
    word, count = line.split('	', 1)

    # Mengubah count dari string menjadi int
    try:
        count = int(count)
    except ValueError:
        continue

    # Jika word sama dengan current_word, tambahkan count
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Menulis hasil untuk current_word
            print(f'{current_word}	{current_count}')
        current_count = count
        current_word = word

# Jangan lupa untuk menulis kata terakhir jika diperlukan!
if current_word == word:
    print(f'{current_word}	{current_count}')
