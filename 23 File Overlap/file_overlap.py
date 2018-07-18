# Given two .txt files that have lists of numbers in them, find the numbers that are
# overlapping. One .txt file has a list of all prime numbers under 1000, and the other
# .txt file has a list of happy numbers up to 1000.
def main():
    print(overlapping_numbers_txt('primenumbers', 'happynumbers'))

def load_file(file):
    with open(file + '.txt', 'r') as open_file:
        return open_file.read().split()


def overlapping_numbers_txt(file_a, file_b):
    file_a = load_file(file_a)
    file_b = load_file(file_b)
    overlap_list = []
    for linha_a in file_a:
        if linha_a in file_b:
            overlap_list.append(linha_a)
    return overlap_list


if __name__ == '__main__':
    main()
