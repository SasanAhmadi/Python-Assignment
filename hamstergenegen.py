"""hamstergenegen.py

This file generates fictional gene data for Assignment 1 and writes it to a
file in the specified directory.

Arguments
-------------
dir : str
    Directory to place gene data in
"""
import os
import argparse
import itertools
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('dir', help='directory to place gene data in', type=str)
args = parser.parse_args()

output_dir = args.dir

output_folder = os.path.basename(output_dir)
output_dir_int = int(output_folder)
rnd_gen = np.random.RandomState(seed=output_dir_int)

character_set = np.array(list("acgtn") + list("acgtn".upper()) + ['-', '_'])
annotation_set = list("hamsters") + list("hamsters".upper())
annotation_set = np.array([''.join(t) for t in itertools.combinations(annotation_set, r=3)]
                          + [''.join(t) for t in itertools.combinations(annotation_set, r=2)]
                          + list(annotation_set))

gene_length = 500
n_hamsters = 10
n_days = 200

gene_seq = rnd_gen.choice(character_set, size=(n_hamsters, gene_length))
gene_qs = rnd_gen.uniform(size=(n_hamsters, n_days, gene_length))
gene_annotations = rnd_gen.choice(annotation_set, size=(n_hamsters, n_days, gene_length))
post_data_end = rnd_gen.uniform(size=(n_hamsters, n_days))
random_whitespace = rnd_gen.uniform(size=(n_hamsters, n_days, gene_length))

for day in range(n_days):
    mutations = rnd_gen.randint(low=0, high=gene_length, size=(int(gene_length/100),))
    gene_seq[:, mutations] = 'A'
    
    for hamster in range(n_hamsters):
        header = """
# SeqHeadStart
# ID: {}
# Date: {}
# Columns: info;base;quality
# SeqHeadEnd""".format(hamster, day)
        with open(os.path.join(output_dir, f'data_{hamster:02}-{day:03}.seq.raw'), 'w') as hf:
            print(header, file=hf)
            for l in range(len(gene_seq[hamster])):
                print(f"{gene_annotations[hamster, day, l]};"
                      f"{gene_seq[hamster, l]};"
                      f"{gene_qs[hamster, day, l]}", file=hf)
                if random_whitespace[hamster, day, l] < 0.01:
                    print(f"# Additional; annotation; here", file=hf)
            print("# Data end", file=hf)
            for l in range(1, int(post_data_end[hamster, day]*100 + 1) * (post_data_end[hamster, day] < 0.1)):
                print(f"{gene_annotations[hamster, day, l]};"
                      f"{gene_annotations[hamster, day, -l]};"
                      f"{gene_annotations[hamster, day, -2*l]}", file=hf)
