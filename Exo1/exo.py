import sys

with open("input1.txt", "r") as file:
	lines = file.read().split("\n")

lines.pop(0)
scores = []
score = 0
for line in lines:
	if line == "B":
		score += 1
	if line == "X":
		scores.append(score)
		score = 0
scores.append(score)
max = max(scores)
print(max)