import json


def recreate_student_name(student_result_list):
    """This function recreates a student's name from split indexes due to splitting on the comma"""
    student_name = student_result_list[0] + student_result_list[1]
    return student_name


def create_students_result_dict(filename):
    d = {}
    with open(f"static/{filename}", encoding="utf-8-sig") as f:
        EOF_flag = False
        f.readline()
        for line in f:
            if ",,,,,,,,,,,," in line:
                EOF_flag = True
            if EOF_flag == False:
                #print(line)
                #print(line.strip().split(',')[:-4])
                student_result_list = line.strip().split(',')[:-4]
                #TODO: deal with empty cells in processing strings to float
                student_total_result = float(student_result_list[-1]) + float(student_result_list[-2]) + \
                                       float(student_result_list[-3]) + float(student_result_list[-4]) + float(student_result_list[-5])
                student_result_list.append(student_total_result)
                student_name = recreate_student_name(student_result_list)
                d[student_name] = student_result_list[2:]

        #print(d)
        return d


def append_dict_to_file(d, filename):
    """This function inserts a python dictionary into a file which is either newly created or rewritten"""
    try:
        with open(f"static/{filename}.json", "x") as outfile:
            json.dump(d, outfile)
    except:
        with open(f"static/{filename}.json", "w") as outfile:
            json.dump(d, outfile)


def student_NAPLAN_results_initialisation_subroutine(filename):
    d = create_students_result_dict(filename)
    append_dict_to_file(d, filename)

if __name__ == '__main__':
    d = create_students_result_dict("Student NAPLAN data csv.csv")
    append_dict_to_file(d, "Student NAPLAN data csv.csv")
