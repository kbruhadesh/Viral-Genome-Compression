import time
import psutil

def read_fasta(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    seq = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return seq

def write_fasta(seq, filepath):
    with open(filepath, 'w') as f:
        f.write('>reconstructed\n')
        for i in range(0, len(seq), 60):
            f.write(seq[i:i+60] + '\n')

def get_stats(input_size, output_size, start_time, end_time):
    process = psutil.Process()
    mem = process.memory_info().rss / (1024 * 1024)
    ratio = output_size / input_size if input_size else 0
    return {
        'compression_ratio': ratio,
        'time_taken': end_time - start_time,
        'memory_mb': mem
    }
