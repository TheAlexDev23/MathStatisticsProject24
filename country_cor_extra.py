import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
country = sheet["Where are you from? (country)"]
extracurricular = sheet["If you participate in extracurricular activities, what is the average time you spend doing so weekly. (In hours)"]

res = {}
for i in range(len(country)):
    try:
        float(extracurricular[i])
    except:
        continue

    val = float(extracurricular[i])

    key = country[i]
    if key == "Russia":
        key = "RU"
    if key == "USA" or key == "America" or key == "America ":
        key = "US"
    if key == "Spain" or key == "Spain " or key == "spain" or key == "Catalonia":
        key = "ES"
    if key == "India":
        key = "IN"
    if key == "Latvia":
        key = "LV"
    if key == "Ukraine":
        key = "UA"
    if key == "China":
        key = "CH"
    if key == "Mexico":
        key = "MX"
    if key == "Argentina" or key == "Argentina ":
        key = "AR"
    if key == "Japan":
        key = "JP"

    if key not in res:
        res[key] = {
            "total": 0,
            "amnt": 0,
        }

    res[key]["total"] +=val
    res[key]["amnt"] += 1

res_x = []
res_y = []
for key in res:
    res_x.append(str(key))
    res_y.append(res[key]["total"]/res[key]["amnt"])

plt.bar(res_x, res_y)
plt.savefig("output/country_cor_extra.png")