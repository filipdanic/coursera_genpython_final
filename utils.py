def readGenome(filename):
    cur = ''
    seq = []
    total_records = 0
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                cur += line.rstrip()
            else:
                total_records += 1
                seq.append(cur)
                cur = ''
    seq.append(cur)
    return seq[1:], total_records

def find_orf(sequence, position):
    start_indexes = []
    start_codon = "ATG"
    stop_indexes = []
    stop_codons =["TAA", "TGA", "TAG"]

    for i in range(position, len(sequence) - 2, 3):
        if sequence[i:i+3] == start_codon:
            start_indexes.append(i)

    for i in range(position, len(sequence), 3):
        if sequence[i:i+3] in stop_codons:
            stop_indexes.append(i)

    orf = []
    mark = 0
    for i in range(0,len(start_indexes)):
        for j in range(0, len(stop_indexes)):
            if start_indexes[i] < stop_indexes[j] and start_indexes[i] > mark:
                orf.append(sequence[start_indexes[i]:stop_indexes[j]+3])
                mark = stop_indexes[j]+3
                break
    return orf


def get_all_repeats(sequence, k):
    length = len(sequence)
    repeats = []
    for i in range(0,length-k+1):
        repeats.append(sequence[i:i+k])
    return repeats


def most_common(lst):
    return max(set(lst), key=lst.count)
