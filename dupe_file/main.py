import filecmp
import os
import itertools

# only compare directories nested within the current location

file_names = []

if __name__ == '__main__':
    top = 'top'
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            file_names.append(os.path.join(root,name))
    print(file_names)

    duplicates = []
    
    # generate tuples with itertools of all pairings
    for f1, f2 in itertools.combinations(file_names, 2):
        if filecmp.cmp(f1,f2):
            duplicates.append((f1,f2))
    print(duplicates)