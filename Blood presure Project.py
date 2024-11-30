import matplotlib.pyplot as plt

blood_pressure_men = [80, 95, 98, 90, 123, 135, 162, 199]
blood_pressure_women = [132, 142, 127, 193, 176, 90, 85, 87]

type = [blood_pressure_men, blood_pressure_women]
colors = ['Chartreuse', 'Turquoise']
label = ['men', 'women']
bins = [80, 100, 125, 150]
plt.xlabel("Blood Pressure Range")
plt.ylabel("Total no. of patients")

plt.hist(type, bins=bins, rwidth=0.95, color=colors,
         label=label, orientation='vertical')
plt.title("Blood Pressure Level Chart")
plt.legend()
plt.show()