import filecmp
import os
import itertools

# only compare files in the provided directory at the current level

def find_duplicates(directory):
    file_names = []
    for root, files in os.walk(directory, topdown=False):
        for name in files:
            file_names.append(os.path.join(root,name))
    duplicates = []
    # generate tuples with itertools of all pairings
    for f1, f2 in itertools.combinations(file_names, 2):
        if filecmp.cmp(f1,f2):
            duplicates.append((f1,f2))
    return duplicates

if __name__ == '__main__':
    print(find_duplicates('top'))
    
    
    