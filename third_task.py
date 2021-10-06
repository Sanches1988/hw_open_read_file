import os


def new_file(file_one=None, file_two=None):
    if file_one or file_two is None:
        file_one = '1.txt'
        file_two = '2.txt'
        os.chdir('sort')
        outout_file = "3.txt"
        f_one_path = os.path.join(os.getcwd(), file_one)
        f_two_path = os.path.join(os.getcwd(), file_two)
        with open(f_one_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(f_two_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(outout_file, 'w', encoding='utf-8') as f_result:

            if len(file1) < len(file2):
                f_result.write(file_one + '\n')
                f_result.write(str(len(file1)) + '\n')
                f_result.writelines(file1)
                f_result.write('\n')
            elif len(file2) < len(file1):
                f_result.write(file_two + '\n')
                f_result.write(str(len(file2)) + '\n')
                f_result.writelines(file2)
                f_result.write('\n')
            if len(file2) > len(file1) or len(file2) < len(file1):
                f_result.write(file_one + '\n')
                f_result.write(str(len(file1)) + '\n')
                f_result.writelines(file1)
                f_result.write('\n')
            elif len(file1) > len(file2) or len(file2) > len(file1) and len(file2):
                f_result.write(file_two + '\n')
                f_result.write(str(len(file2)) + '\n')
                f_result.writelines(file2)
                f_result.write('\n')
    else:
        print('------------------------------------')
    return

new_file()