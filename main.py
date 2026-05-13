import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Neha", "Ankit"],
    "Math": [78, 92, 45, 60, 30],
    "Science": [85, 88, 50, 65, 40],
    "English": [80, 95, 40, 70, 35]
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
      df[["Math", "Science", "English"]].mean())

# Student Average
avg = df[["Math", "Science", "English"]].mean(axis=1)
print("Student Average:\n", avg)

# Topper
topper = avg.idxmax()

print("Topper index:", topper)
print("Topper marks:\n", df.loc[topper])

# Fail students
fail = (df[["Math", "Science", "English"]] < 50).any(axis=1)

print("Fail students:\n", df[fail])

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/PC/Desktop/student.csv")

# Subject averages
subject_avg = df[["Math", "Science", "English"]].mean()

# Graph
subject_avg.plot(kind='bar')

plt.title("Subject Average")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()
avg = df[["Math", "Science", "English"]].mean(axis=1)

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