# Genome Compressor: FCM + Arithmetic Coding

A Python tool for compressing viral DNA sequences using Finite Context Models (FCM) and Arithmetic Coding.

## Features
- Compress/decompress FASTA genome files
- Adaptive FCM with configurable context length
- Arithmetic coding for efficient compression
- Huffman and gzip comparison
- CLI options for input, output, context, and method
- Compression statistics (ratio, time, memory)
- Modular and extensible design

## Usage
```sh
python -m genome_compressor --input <input.fasta> --output <outdir> --context 6 --mode compress --method fcm
python -m genome_compressor --input <input.fasta> --output <outdir> --context 6 --mode decompress --method fcm
python -m genome_compressor --input <input.fasta> --output <outdir> --mode compress --method huffman
python -m genome_compressor --input <input.fasta> --output <outdir> --mode compress --method gzip
```

## Requirements
- Python 3.8+
- See `requirements.txt`

## Installation

Install dependencies with:
```sh
pip install -r requirements.txt
```

## Input/Output

- **Input:** Standard FASTA file (single sequence, DNA alphabet: A, C, G, T).
- **Output:** 
  - FCM+Arithmetic: `compressed.fcmac` and `decompressed.fasta`
  - Huffman: `compressed.huff` and `decompressed_huff.fasta`
  - Gzip: `compressed.gz`

## Decompression

- FCM+Arithmetic: Use `--mode decompress --method fcm`
- Huffman: Decompression is supported, but the tree is not saved to file, so only works for demonstration.
- Gzip: Decompress using standard gzip tools.

## Limitations

- The FCM+Arithmetic implementation is for demonstration and may not scale to very large genomes.
- Huffman decompression requires the same session or code modification to save/load the tree.
