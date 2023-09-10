#Points for "for loop"

# 1. for loop start with keyword "for"
# 2. always includes a variable 
# always use "in" keywaord.
# 4. in for loop we use "range" function to find out sequence of numbers.
# 5.to use block of codes repeatedly we use "for loop".
# we use varible and variable always take 1 value at a time thats why it takes  

#employees = ["saad","raheel","insha","Ali","zaid"]

# employeeName = "Raheel wali"



#for emp in employees:
       # print("emp")

#if we need to go out from loop in any point we use command break.
 
# for e in employeeName:
#     print("Employee Name is:",e)



# Break

# for emp in employees:
#     if emp == "zaid":
#       break
#       print("Employee Name is:",emp)


# for emp in employees:
#     print("Employee Name is:",emp)
#     if emp == "saad":
#         break
    

# continue


# for emp in employees:
#     if emp == "saad":
#         continue
#     print("Continue:",emp)


# for emp in employees:
#     print("Continue:",emp)
#     if emp == "raheel":
#      continue
    

# while loop
# while loop always work on true condition.
# while value intialize inside the loop.
# while loop start with keyword "while"
# in while loop we use break command to stope the loop other wise 
# true statement will run infinite never stop.
# in while loop we use continue command it will skip the specific 
# name remaining will show up 

class_1 = ["saad","raheel","insha","Ali","zaid"]

ab = 0

while ab < 10:
    #if(employees[ab] == "raheel" or employees[ab] == "saad"):
     #   ab = ab + 1
    #     continue
    # else:
    if ab > len(class_1) -1:
      break

    print("while 10 :",class_1[ab], "index", ab)
    ab = ab + 1


# while True:
#     print("Hello While loop")
#     break


 


