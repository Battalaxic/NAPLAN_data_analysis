import json

with open("static/Student NAPLAN data csv.csv.json") as f:
    for line in f:
        students_NAPLAN_results_d = json.loads(line)
print(students_NAPLAN_results_d)