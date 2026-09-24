import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("data/students.csv")

# Clean the data
data = data.dropna()
data["grade"] = pd.to_numeric(data["grade"], errors="coerce")
data = data.dropna()

# Calculate statistics
average = data["grade"].mean()
highest = data["grade"].max()
lowest = data["grade"].min()
students = len(data)

# Add pass/fail column
data["result"] = data["grade"].apply(
    lambda grade: "Pass" if grade >= 50 else "Fail"
)

# Display results
print("STUDENT GRADE REPORT")
print("--------------------")
print(f"Number of students: {students}")
print(f"Average grade: {average:.2f}")
print(f"Highest grade: {highest}")
print(f"Lowest grade: {lowest}")

print("\nStudent Results:")
print(data[["name", "grade", "result"]])

# Create a chart
plt.bar(data["name"], data["grade"])
plt.title("Student Grades")
plt.xlabel("Student")
plt.ylabel("Grade")
plt.ylim(0, 100)
plt.tight_layout()

# Save chart
plt.savefig("reports/student_grades.png")
plt.close()

# Create text report
with open("reports/summary.txt", "w") as file:
    file.write("STUDENT GRADE REPORT\n")
    file.write("--------------------\n")
    file.write(f"Number of students: {students}\n")
    file.write(f"Average grade: {average:.2f}\n")
    file.write(f"Highest grade: {highest}\n")
    file.write(f"Lowest grade: {lowest}\n")

print("\nReports created successfully!")
