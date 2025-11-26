def round_robin(*seqs):
    seqs = [iter(s) for s in seqs]
    while seqs:
        for it in list(seqs):
            try:
                yield next(it)
            except StopIteration:
                seqs.remove(it)

print(list(round_robin([1,2,3], (4,5))))
