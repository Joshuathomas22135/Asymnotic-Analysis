# A Python program that performs three different operations on a game leaderboard — direct index access, linear search, and 
# nested pair comparison — counts the exact steps for each, and classifies every operation with its formal asymptotic 
# notation: Theta(1), Omega(1), O(n), and O(n²). The program ends with an asymptotic summary showing all four notations 
# side by side and the dominant-term simplification rule.

scores = [10,6,8,8,12,11,6]

print("O(1)")
print(scores[0])

print("\n")
print("O(n)")

index = int(input("Enter the number of the element you want to view: "))

flag = False
pos = 0
for i in range(len(scores)):
    if scores[i]==index:
        flag = True
        pos = i

if flag == True:
    print("Found at pos:", pos)
else:
    print("Not found")

print("\n")

print("O(n²)")

steps = 0

for i in range(len(scores)):
    for j in range(i+1, len(scores)):
        steps += 1
        if scores[i] == scores[j]:
            print(f"Pair found: {scores[i]} at positions {i} and {j}")

print("Nested comparison steps:", steps)

print("\n")
print("Asymptotic Summary")
print("-------------------")
print("Direct index access:       Θ(1)")
print("Best-case search:          Ω(1)")
print("Linear search:             O(n)")
print("Nested pair comparison:    O(n²)")