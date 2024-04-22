import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
study_time = sheet["Time spent studying before science related exams (total hours)(write the answer as a number, no letters)"]
grade = sheet["What grade do you usually get in science related subjects? "]

res = {}
for i in range(len(study_time)):
    try:
        float(study_time[i])
    except:
        continue

    key = float(study_time[i])
    if key not in res:
        res[key] = {
            "total": 0,
            "amnt": 0,
        }

    res[key]["total"] += grade[i]
    res[key]["amnt"] += 1

res_x = []
res_y = []
for key in sorted(res.keys()):
    res_x.append(str(key))
    res_y.append(res[key]["total"]/res[key]["amnt"])

print(res_x)
print(res_y)

plt.bar(res_x, res_y)
# plt.show()
plt.savefig("output/std_cor_gradesci.png", bbox_inches="tight")
