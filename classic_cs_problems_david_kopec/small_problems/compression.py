from collections import deque
from typing import Deque


class CompressedGene:
    NUCLEOTIDE_MAPPING = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
    NUCLEOTIDES = ['A', 'C', 'G', 'T']

    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:

        self.bit_string: int = 1

        for nucleotide in gene.upper():
            self.bit_string <<= 2  # shift left two bits
            if nucleotide in self.NUCLEOTIDE_MAPPING:
                self.bit_string |= self.NUCLEOTIDE_MAPPING[nucleotide]  # change last two bits
            else:
                raise ValueError('Invalid Nucleotide: {}'.format(nucleotide))

    def decompress(self) -> str:
        gene: Deque[str] = deque()
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits < 4:
                gene.appendleft(self.NUCLEOTIDES[bits])
            else:
                raise ValueError("Invalid bits: {}".format(bits))

        return ''.join(gene)

    def __str__(self):
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTT" * 100
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compres
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))
