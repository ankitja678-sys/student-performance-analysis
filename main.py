import pandas as pd

data = {
    "Name": ["ankit", "Riya", "shivani", "shaloni", 'amit', 'avinash'],
    "Math": [93, 22, 34, 60, 33, 78],
    "Science": [66, 78, 88, 65, 78, 68],
    "English": [91, 52, 73, 70, 23, 80],
    'Hindi': [67, 78, 89, 23, 34, 45]
}

df = pd.DataFrame(data)

# Save CSV
df.to_csv("C:/Users/PC/Desktop/student.csv", index=False)

print("CSV file created successfully!")

# Read CSV
df = pd.read_csv("C:/Users/PC/Desktop/student.csv")

print("Data:\n", df)

# Shape
print("Shape:", df.shape)

# Subject Average
print("Subject Average:\n",
      df[["Math", "Science", "English", 'Hindi']].mean())

# Student Average
avg = df[["Math", "Science", "English", 'Hindi']].mean(axis=1)
print("Student Average:\n", avg)

# Topper
topper = avg.idxmax()

print("Topper index:", topper)
print("Topper marks:\n", df.loc[topper])

# Fail students
fail = (df[["Math", "Science", "English", 'Hindi']] < 50).any(axis=1)

print("Fail students:\n", df[fail])

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/PC/Desktop/student.csv")

# Subject averages
subject_avg = df[["Math", "Science", "English", 'Hindi']].mean()

# Graph
subject_avg.plot(kind='bar')

plt.title("Subject Average")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()
avg = df[["Math", "Science", "English", 'Hindi']].mean(axis=1)

plt.bar(df["Name"], avg)

plt.title("Student Average")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.show()

subject_avg.plot(kind='pie', autopct='%1.1f%%')

plt.title("Subject Contribution")

plt.ylabel("")

plt.show()
plt.plot(df["Name"], df["Math"], marker='o')

plt.title("Math Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()