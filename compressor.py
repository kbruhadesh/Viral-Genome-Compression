import os
import time
import gzip
from utils import read_fasta, write_fasta, get_stats
from fcm import FiniteContextModel
from arithmetic import ArithmeticCoder
from huffman import huffman_encode, huffman_decode, build_huffman_tree

# FCM + Arithmetic Coding

def compress(input_file, output_dir, context_length):
    seq = read_fasta(input_file)
    fcm = FiniteContextModel(context_length)
    fcm.train(seq)
    coder = ArithmeticCoder()
    start = time.time()
    code = coder.encode(seq, fcm)
    end = time.time()
    out_path = os.path.join(output_dir, 'compressed.fcmac')
    with open(out_path, 'w') as f:
        f.write(f"{code}\n{context_length}\n{seq[:context_length]}\n{len(seq)}\n")
    stats = get_stats(len(seq), os.path.getsize(out_path), start, end)
    print('FCM+Arithmetic Compression:', stats)


def decompress(input_file, output_dir, context_length):
    with open(input_file, 'r') as f:
        code = float(f.readline().strip())
        context_length = int(f.readline().strip())
        context_seed = f.readline().strip()
        length = int(f.readline().strip())
    fcm = FiniteContextModel(context_length)
    coder = ArithmeticCoder()
    start = time.time()
    seq = coder.decode(code, fcm, length, context_seed)
    end = time.time()
    out_path = os.path.join(output_dir, 'decompressed.fasta')
    write_fasta(seq, out_path)
    stats = get_stats(length, os.path.getsize(out_path), start, end)
    print('FCM+Arithmetic Decompression:', stats)

# Huffman comparison

def compare_with_huffman(input_file, output_dir, compress=True):
    seq = read_fasta(input_file)
    if compress:
        start = time.time()
        encoded, tree = huffman_encode(seq)
        end = time.time()
        out_path = os.path.join(output_dir, 'compressed.huff')
        with open(out_path, 'w') as f:
            f.write(encoded)
        stats = get_stats(len(seq), len(encoded)//8, start, end)
        print('Huffman Compression:', stats)
    else:
        with open(input_file, 'r') as f:
            encoded = f.read().strip()
        tree = build_huffman_tree(seq)  # In practice, tree should be stored/transmitted
        start = time.time()
        decoded = huffman_decode(encoded, tree)
        end = time.time()
        out_path = os.path.join(output_dir, 'decompressed_huff.fasta')
        write_fasta(decoded, out_path)
        stats = get_stats(len(decoded), os.path.getsize(out_path), start, end)
        print('Huffman Decompression:', stats)

# Gzip comparison

def compare_with_gzip(input_file, output_dir):
    seq = read_fasta(input_file)
    out_path = os.path.join(output_dir, 'compressed.gz')
    start = time.time()
    with gzip.open(out_path, 'wt') as f:
        f.write(seq)
    end = time.time()
    stats = get_stats(len(seq), os.path.getsize(out_path), start, end)
    print('Gzip Compression:', stats)
