#Points for "for loop"

# 1. for loop start with keyword "for"
# 2. always includes a variable 
# always use "in" keywaord.
# 4. in for loop we use "range" function to find out sequence of numbers.
# 5.to use block of codes repeatedly we use "for loop".
 

employees = ["saad","raheel","insha","Ali","zaid"]

employeeName = "Raheel wali"

# for emp in employees:
#     print("Employee Name is:",emp)


# for e in employeeName:
#     print("Employee Name is:",e)


# Break

for emp in employees:
    if emp == "saad":
        break
    print("Employee Name is: break",emp)


for emp in employees:
    print("Employee Name is: break",emp)
    if emp == "saad":
        break
    

# continue


for emp in employees:
    if emp == "raheel":
        continue
    print("Continue:",emp)


# for emp in employees:
#     print("Continue:",emp)
#     if emp == "raheel":
#         continue
    

# while loop

ab = 0

while ab < len(employees):
    if(employees[ab] == "raheel" or employees[ab] == "saad"):
        ab = ab + 1
        continue
    else:
        print("while emp Name:",employees[ab], "index", ab)
        ab = ab + 1


while True:
    print("Hello While loop")
    break


 


