import sys, getopt

#-e 1 -i /Users/rajesh.chandra/netwise-july-2018/netwise_july_2018.psv -o /Users/rajesh.chandra/netwise-july-2018/tmpremove.psv
#Remove the given line from the file.
def read_file_and_remove_line(input_file_path, output_file_path, line_number_to_remove):
    with open(output_file_path, 'w') as out_file:
        with open(input_file_path) as input_file:
            line_ptr = 0
            line_number_to_remove_idx = 0
            line_to_remove = line_number_to_remove[line_number_to_remove_idx]
            for line in input_file:
                line_ptr = line_ptr + 1 # 1- based
                if line_ptr != line_to_remove:
                    out_file.write(line)
                else:
                    line_number_to_remove_idx = line_number_to_remove_idx + 1
                    if line_number_to_remove_idx >= len(line_number_to_remove):
                        line_to_remove = -1
                    else :
                        line_to_remove = line_number_to_remove[line_number_to_remove_idx]

            input_file.close()
            out_file.close()

def main(argv):
    line_number_to_remove = 0
    input_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "h:e:i:o:")
        if len(opts) != 3:
            raise getopt.GetoptError("Insufficient Parameters")
    except getopt.GetoptError:
        print 'RemoveLineFromFile.py -e <line number to remove 1-based> -i <input file path> -o <output file path>'
        sys.exit(2)
    for opt, arg in opts:
        if opts == '-h':
            print 'RemoveLineFromFile.py -e <line number to remove 1-based> -i <input file path> -o <output file path>'
            sys.exit(1)
        elif opt in ("-e"):
            line_number_to_remove = [int(i) for i in arg.split(',')]
            if any(line_number <= 0 for line_number in line_number_to_remove):
                print 'Please provide line numbers >= 1'
                sys.exit(1)
        elif opt in ("-i"):
            input_file = arg
        elif opt in ("-o"):
            output_file = arg

    if(line_number_to_remove <= 0):
        print 'RemoveLineFromFile.py -e <line number to remove 1-based> -i <input file path> -o <output file path>'
        sys.exit(1)

    read_file_and_remove_line(input_file, output_file, line_number_to_remove)

if __name__ == "__main__":
   main(sys.argv[1:])