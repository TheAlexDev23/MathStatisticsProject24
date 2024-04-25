import matplotlib.pyplot as plt
import pandas as pd

sheet = pd.ExcelFile("./Copy of MTH_24.C_FormResponses.xlsx").parse(0)
country = sheet["Where are you from? (country)"]

grade_science = sheet["What grade do you usually get in science related subjects? "]
science_study = sheet["Time spent studying before science related exams (total hours)(write the answer as a number, no letters)"]

res = {}
for i in range(len(country)):
    study = 0
    try:
        study = float(science_study[i])
    except:
        continue

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

    if study == 0:
        study = 0.2

    res[key]["total"] += grade_science[i]/study
    res[key]["amnt"] += 1

res_x = []
res_y = []
for key in res:
    res_x.append(str(key))
    res_y.append(res[key]["total"]/res[key]["amnt"])

plt.bar(res_x, res_y)
plt.savefig("output/country_cor_stdgradescirate.png")
