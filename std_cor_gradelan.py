import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
study_time = sheet["Time spent studying before language related exams (total hours)"]
grade = sheet["What grade do you usually get in language related subjects?"]

res = {}
for i in range(len(study_time)):
    if study_time[i] not in res:
        res[study_time[i]] = {
            "total": 0,
            "amnt": 0,
        }

    res[study_time[i]]["total"] += grade[i]
    res[study_time[i]]["amnt"] += 1

res_x = []
res_y = []
for key in sorted(res.keys()):
    res_x.append(str(key))
    res_y.append(res[key]["total"]/res[key]["amnt"])

print(res_x)
print(res_y)

plt.bar(res_x, res_y)
# plt.show()
plt.savefig("output/std_cor_gradelan.png", bbox_inches="tight")
