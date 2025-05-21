import argparse
import os
import sys
from compressor import compress, decompress, compare_with_gzip, compare_with_huffman

def main():
    parser = argparse.ArgumentParser(description="Genome Compressor: FCM + Arithmetic Coding")
    parser.add_argument('--input', required=True, help='Input FASTA file')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--context', type=int, default=6, help='Context length for FCM (default: 6)')
    parser.add_argument('--mode', choices=['compress', 'decompress'], required=True, help='Mode: compress or decompress')
    parser.add_argument('--method', choices=['fcm', 'huffman', 'gzip'], required=True, help='Compression method')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    if args.method == 'fcm':
        if args.mode == 'compress':
            compress(args.input, args.output, args.context)
        else:
            decompress(args.input, args.output, args.context)
    elif args.method == 'huffman':
        if args.mode == 'compress':
            compare_with_huffman(args.input, args.output, compress=True)
        else:
            compare_with_huffman(args.input, args.output, compress=False)
    elif args.method == 'gzip':
        compare_with_gzip(args.input, args.output)
    else:
        print('Unknown method')
        sys.exit(1)

if __name__ == '__main__':
    main()
