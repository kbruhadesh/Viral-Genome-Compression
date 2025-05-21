from collections import defaultdict, Counter

class FiniteContextModel:
    def __init__(self, context_length=6):
        self.context_length = context_length
        self.model = defaultdict(Counter)
        self.alphabet = ['A', 'C', 'G', 'T']

    def update(self, context, symbol):
        self.model[context][symbol] += 1

    def predict(self, context):
        counts = self.model[context]
        total = sum(counts.values())
        if total == 0:
            # Uniform probability if unseen context
            return {a: 1/4 for a in self.alphabet}
        return {a: counts[a]/total if a in counts else 0 for a in self.alphabet}

    def train(self, sequence):
        for i in range(len(sequence) - self.context_length):
            context = sequence[i:i+self.context_length]
            symbol = sequence[i+self.context_length]
            self.update(context, symbol)
