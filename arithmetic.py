import math

class ArithmeticCoder:
    def __init__(self, alphabet=['A', 'C', 'G', 'T']):
        self.alphabet = alphabet

    def encode(self, sequence, fcm):
        low, high = 0.0, 1.0
        context_length = fcm.context_length
        for i in range(len(sequence) - context_length):
            context = sequence[i:i+context_length]
            symbol = sequence[i+context_length]
            probs = fcm.predict(context)
            cum = 0.0
            ranges = {}
            for a in self.alphabet:
                ranges[a] = (cum, cum + probs[a])
                cum += probs[a]
            s_low, s_high = ranges[symbol]
            width = high - low
            high = low + width * s_high
            low = low + width * s_low
            fcm.update(context, symbol)
        return (low + high) / 2

    def decode(self, code, fcm, length, context_seed):
        context_length = fcm.context_length
        sequence = context_seed
        value = code
        for _ in range(length - context_length):
            context = sequence[-context_length:]
            probs = fcm.predict(context)
            cum = 0.0
            ranges = {}
            for a in self.alphabet:
                ranges[a] = (cum, cum + probs[a])
                cum += probs[a]
            for symbol in self.alphabet:
                s_low, s_high = ranges[symbol]
                if s_low <= value < s_high:
                    sequence += symbol
                    value = (value - s_low) / (s_high - s_low)
                    fcm.update(context, symbol)
                    break
        return sequence
