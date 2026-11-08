import matplotlib.pyplot as plt

Girls_marks= [90, 95, 80, 75, 69, 88, 92, 71, 89, 79, 12, 89, 100]
Boys_marks = [67, 98, 89, 79, 87, 81, 84, 69, 89, 79, 80, 89, 100]

type = [Girls_marks, Boys_marks]
colors = ["blue", "orange"]
label = ['boys', 'girls']
bins = [80, 100, 125, 150]
plt.xlabel("Marks of Boys and Girls in PTM")
plt.ylabel("Total marks of Boys and Girls")

plt.hist(type, bins=bins, rwidth=0.95, color=colors,
            label=label, orientation="vertical")
plt.title("Marks Distribution of Boys and Girls ")
plt.legend()
plt.show()