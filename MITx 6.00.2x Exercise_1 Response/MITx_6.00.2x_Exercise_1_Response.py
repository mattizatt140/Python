import itertools

def powerset(iterable):
    return list(itertools.chain.from_iterable(itertools.combinations(iterable, r) for r in range(len(iterable)+1)))