
def mult_file(INFILE='numbers.txt', OUTFILE='numbers-mult.txt'):
    """Reads file numbers.txt and outputs where each number in numbers.txt is multiplied by its line number."""

    try:
        with open(INFILE, 'r') as infile, open(OUTFILE, 'w') as outfile:
            for count, line in enumerate(infile, 1):
                line.strip()
                if line:
                    out = count * int(line)
                    outfile.write("%d\n" % out)
    except IOError as e:
        print("Can't open files %s" % e)