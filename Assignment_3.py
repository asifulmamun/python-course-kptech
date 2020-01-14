"""
    @Assignment-3
    @Victory Day Cooding Compettition(16th December 2019)
"""


# # 1. Input an Integer n and perform these tasks:
# n = int(input("Enter any integert Number for check Even or Odd: "))

# # Check Even or Odd, Queation-1.(i and ii)
# if n % 2 == 0:
#     print("Even\n")
# else:
#     print("Odd\n")

# # check Between 1-5 or not, Queation-1.(iii and iv)
# if n in range (1,5):
#     print("Firts Five\n")
# else:
#     print("Not in Five\n")


# 2. Make a list of Motorcycle with at least 4 data and perform these tasks:
motorCycleList = ["Honda", "Suzuki", "R15", "Pulsar", "Apache"]

motorCycleListAppended = motorCycleList
motorCycleListAppended.append("Harley-Davidson") # Adding Value
for motorCycleLists in motorCycleListAppended:
    print('\n', motorCycleLists)

# motorCycleListRemoved = motorCycleList
# motorCycleListRemoved.pop(-1) # remove last
# print(motorCycleListRemoved)

# motorCycleListReverse = motorCycleList
# motorCycleListReverse.reverse() # Reverse
# print(motorCycleListReverse)

# honda = motorCycleList[0:3]
# print(honda) # Why printed reverse 3