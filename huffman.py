import heapq
from collections import Counter, defaultdict

class HuffmanNode:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(sequence):
    freq = Counter(sequence)
    heap = [HuffmanNode(sym, freq[sym]) for sym in freq]
    heapq.heapify(heap)
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        parent = HuffmanNode(freq=n1.freq + n2.freq)
        parent.left = n1
        parent.right = n2
        heapq.heappush(heap, parent)
    return heap[0]

def build_codes(node, prefix='', codebook=None):
    if codebook is None:
        codebook = {}
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encode(sequence):
    tree = build_huffman_tree(sequence)
    codebook = build_codes(tree)
    encoded = ''.join(codebook[s] for s in sequence)
    return encoded, tree

def huffman_decode(encoded, tree):
    node = tree
    decoded = ''
    for bit in encoded:
        node = node.left if bit == '0' else node.right
        if node.symbol is not None:
            decoded += node.symbol
            node = tree
    return decoded
