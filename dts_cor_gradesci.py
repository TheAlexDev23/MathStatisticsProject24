import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
days_to_study = sheet["How many days before the exam do you start studying? -1 if you don’t study. 0 if you study the same day. 1 if you study the day before, etc."]
grade_language = sheet["What grade do you usually get in science related subjects? "]

res = {}
for i in range(len(days_to_study)):
    if days_to_study[i] not in res:
        res[days_to_study[i]] = {
            "total": 0,
            "amnt": 0,
        }

    res[days_to_study[i]]["total"] += grade_language[i]
    res[days_to_study[i]]["amnt"] += 1

res_x = []
res_y = []
for key in sorted(res.keys()):
    res_x.append(str(key))
    res_y.append(res[key]["total"]/res[key]["amnt"])

print(res_x)
print(res_y)

plt.bar(res_x, res_y)
# plt.show()
plt.savefig("output/dts_cor_gradesci.png", bbox_inches="tight")
