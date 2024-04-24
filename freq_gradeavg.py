import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
grade_language = sheet["What grade do you usually get in language related subjects?"]
grade_science = sheet["What grade do you usually get in science related subjects? "]

res = {}
for i in range(len(grade_language)):
    grade_avg = (grade_language[i] + grade_science[i])/2
    if grade_avg not in res:
        res[grade_avg] = 0
    
    res[grade_avg] += 1

res_x = []
res_y = []
for key in sorted(res.keys()):
    res_x.append(str(key))
    res_y.append(res[key])

print(res_x)
print(res_y)

plt.bar(res_x, res_y)
# plt.show()
plt.savefig("output/freq_gradeavg.png", bbox_inches="tight")
