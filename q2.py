import sys

def q2(inp, inp_type='filenames'):
    result_dict = {}
    if inp_type == 'filenames':
        for f_name in inp:
            f = open(f_name)
            for lines in f.readlines():
                for word in lines.split():
                    if word.lower() in result_dict:
                        if f_name not in result_dict[word.lower()]:
                            result_dict[word.lower()].append(f_name)
                    else:
                        result_dict[word.lower()] = [f_name]
            f.close()
    for word, fname in list(result_dict.items()):
        print(word, fname)

def input_handler():
    '''
    Enter the filename like command line arguments
        e.g. python<version> q2.py "/path/file_nam1" "/path/file_nam2" "/path/file_nam3"
    or, as input
        python<version> q2.py

    
    '''
    inp = []
    if len(sys.argv) == 4:
        q2(sys.argv[1:])
    else:
        print("Enter the 3 filenames below\n")
        for i in range(3):
            inp.append(input("Enter the %s filename with path" %(i+1)))
        q2(inp)