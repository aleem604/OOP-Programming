from prettytable import PrettyTable
from prettytable.prettytable import HRuleStyle, VRuleStyle


table = PrettyTable()

table.field_names = [
    "ID",
    "Employee",
    "Department",
    "Country",
    "Experience",
    "Salary",
    "Rating",
]

table.add_rows([
    [101, "Muhammad Aleem", "Engineering", "Pakistan", 10, 8500, 4.85],
    [102, "John Smith", "Architecture", "USA", 12, 12000, 4.91],
    [103, "Sarah Johnson", "Backend", "Canada", 8, 7500, 4.72],
    [104, "David Brown", "DevOps", "UK", 7, 7000, 4.60],
    [105, "Lisa Adams", "Frontend", "Germany", 6, 6500, 4.50],
])

# Title
table.title = "EMPLOYEE MANAGEMENT REPORT"

# Alignment
table.align["Employee"] = "l"
table.align["Department"] = "l"
table.align["Country"] = "c"
table.align["Experience"] = "r"
table.align["Salary"] = "r"
table.align["Rating"] = "r"

# Padding
table.left_padding_width = 1
table.right_padding_width = 1

# Column width
table.max_width["Department"] = 15
table.max_width["Employee"] = 20

# Header
table.header = True
table.header_style = "upper"

# Borders / rules - latest PrettyTable style
table.border = True
table.hrules = HRuleStyle.ALL
table.vrules = VRuleStyle.FRAME

# Sorting
table.sortby = "Salary"
table.reversesort = True

# Correct numeric formatting
table.float_format = ".2"

# For comma/currency formatting, use custom_format
table.custom_format["Salary"] = lambda field, value: f"${value:,.0f}"
table.custom_format["Experience"] = lambda field, value: f"{value} yrs"

print(table)

print("\nSelected Columns:\n")
print(table.get_string(fields=["Employee", "Department", "Salary"]))

print("\nTop 3 Records:\n")
print(table.get_string(start=0, end=3))

with open("employees_report.txt", "w", encoding="utf-8") as file:
    file.write(table.get_string())

print("\nReport exported successfully.")