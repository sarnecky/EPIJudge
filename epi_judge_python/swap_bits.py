from test_framework import generic_test

# xorowanie z bit_mask zadziala dlatego ze:
# w masce beda 2 bity w miejscach i oraz j
# w liczbie x beda bity na miejscach i oraz j, a ich wartosci sa rozne
# jezeli mamy maske i xorujemy ja z liczba x, efekt bedzie nastepujacy
# tam gdzie w x bedzie 1, wynik xor 1 XOR 1 daje 0, czy wartosc przeciwna
# tam gdzue w x bedzie 0, wynik xor 1 xor 0 daje 1, czyli wartosc przecina
# bity sa zamienione
def swap_bits(x, i, j):
    if (x >> i) & 1 != ( x >> j) & 1:
        bit_mask = (1 << i) | (1 << j) 
        x ^= bit_mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
