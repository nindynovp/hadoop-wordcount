#!/usr/bin/env python3
import sys

# Membaca input dari stdin
for line in sys.stdin:
    # Menghapus spasi di awal dan akhir
    line = line.strip()

    # Memisahkan baris menjadi kata-kata
    words = line.split()

    # Mengeluarkan tuple (kata, 1) dalam format tab-delimited
    for word in words:
        print(f'{word}	1')
