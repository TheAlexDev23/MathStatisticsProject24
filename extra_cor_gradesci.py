import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
extracurricular = sheet["If you participate in extracurricular activities, what is the average time you spend doing so weekly. (In hours)"]
grade_sci = sheet["What grade do you usually get in science related subjects? "]

res = {}
for i in range(len(extracurricular)):
    try:
        float(extracurricular[i])
    except:
        continue

    key = float(extracurricular[i])

    try:
        float(grade_sci[i])
    except:
        continue

    val_sci = float(grade_sci[i])

    if key not in res:
        res[key] = {
            "total": 0,
            "amnt": 0,
        }

    res[key]["total"] += val_sci
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
plt.savefig("output/extra_cor_gradesci.png", bbox_inches="tight")
