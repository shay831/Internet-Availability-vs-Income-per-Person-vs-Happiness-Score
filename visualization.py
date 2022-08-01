import matplotlib.pyplot as plt
import csv

income = []
internet = []


def format_coord(x, y):
    try:
        return "x: {}, y: {}, z: {}".format(x, y)

    except:
        return "x: {}, y: {}".format(x, y)


with open('internetusage_income.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        if row[0] != "country" and row[1] != "" and row[2] != "":
            income.append(int(float(row[1])))
            internet.append(int(float(row[2])))


fig, ax = plt.subplots()
ax.format_coord = format_coord

plt.scatter(income, internet, color='g', s=100)
plt.xticks(rotation=25)
plt.xlabel('Income per person')
plt.ylabel('Internet use rate')
plt.title('income per person vs intenet use rate', fontsize=20)

plt.show()
