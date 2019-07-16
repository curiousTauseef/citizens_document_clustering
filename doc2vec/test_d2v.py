from gensim.models.doc2vec import Doc2Vec
from random import sample
from shutil import get_terminal_size
import glob
import os

all_files = glob.glob('txts/*lmms')
model = Doc2Vec.load('lemmas.model')

# This prints _ of equal length to your terminal size
# Works as a separator between printed files
term_line = '_' * (get_terminal_size().columns)


# Picks a random file and prints the n_files that are most similar to it
def print_similar(n_files):
    test_file = sample(all_files, 1)[0]
    most_similar = (model.docvecs.most_similar([test_file], topn = n_files))
    os.system(f'cat {test_file}')
    for file,l in most_similar:
        os.system(f'cat {file}')
        print('\n', term_line)


# print_similar(10)

# Returns a dict
# Format: {file: similarity_to_all_other_files}
def get_similarity(n_files):
    for file in all_files:
        most_similar = (model.docvecs.most_similar([file], topn = n_files))
        yield {file: most_similar}


similarity = [w for w in get_similarity(len(all_files))]
