import sys, getopt
from random import randint

random_numbers = []

#generate random numbers
def generate_random_ints(number_of_random_numbers, total_number_of_lines_in_file):
    tmp_list = []
    for i in range(0,number_of_random_numbers):
        random_number = randint(10,total_number_of_lines_in_file)
        tmp_list.append(random_number)

    #sort the list
    return sorted(tmp_list)


#Using the random numbers get that line from the file
def read_file_and_get_lines(input_file_path, output_file_path, random_line_numbers):
    current_line_index = 0
    with open(output_file_path, 'w') as out_file:
        with open(input_file_path) as input_file:
            line_ptr = 0
            line_number_to_store = random_line_numbers[current_line_index]
            for line in input_file:
                line_ptr = line_ptr + 1 # 1- based
                if line_ptr == line_number_to_store:
                    out_file.write(line)
                    current_line_index = current_line_index + 1
                    if current_line_index >= len(random_line_numbers):
                        break
                    else:
                        line_number_to_store = random_line_numbers[current_line_index]
            input_file.close()
            out_file.close()

def main(argv):
    number_of_lines_to_extract = 0
    number_of_lines_in_input_file = 0
    input_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "h:e:t:i:o:")
        if len(opts) != 4:
            raise getopt.GetoptError("Insufficient Parameters")
    except getopt.GetoptError:
        print 'RandomLinesFromLargeFile.py -e <number of lines to extract> -t  <total number of lines in input file -i <input file path> -o <output file path>'
        sys.exit(2)
    for opt, arg in opts:
        if opts == '-h':
            print 'RandomLinesFromLargeFile.py -e <number of lines to extract> -t  <total number of lines in input file -i <input file path> -o <output file path>'
            sys.exit(1)
        elif opt in ("-e"):
            number_of_lines_to_extract = int(arg)
        elif opt in ("-t"):
            number_of_lines_in_input_file = int(arg)
        elif opt in ("-i"):
            input_file = arg
        elif opt in ("-o"):
            output_file = arg


    random_numbers = generate_random_ints(number_of_lines_to_extract, number_of_lines_in_input_file)
    print(random_numbers)
    read_file_and_get_lines(input_file, output_file, random_numbers)

if __name__ == "__main__":
   main(sys.argv[1:])