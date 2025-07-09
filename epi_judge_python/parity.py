from test_framework import generic_test


# O(n) n number of bits
def parity(x: int) -> int:
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity % 2

# O(k)
def parity_bit_fiddler(x: int) -> int:
    parity = 0
    while x:
        parity ^= 1
        x &=(x - 1)
    return parity % 2


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
