import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
country = sheet["Where are you from? (country)"]
days_to_study = sheet["How many days before the exam do you start studying? -1 if you don’t study. 0 if you study the same day. 1 if you study the day before, etc."]

res = {}
for i in range(len(country)):
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

    res[key]["total"] += days_to_study[i]
    res[key]["amnt"] += 1

res_x = []
res_y = []
for key in res:
    res_x.append(str(key))
    res_y.append(res[key]["total"]/res[key]["amnt"])

plt.bar(res_x, res_y)
plt.savefig("output/country_cor_dts.png")