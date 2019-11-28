def estCoincer(lines: list):
	new_lines = lines.copy()
	for i in range(len(lines)):
		for n in range(len(lines[i])):
			if lines[i][n] == "T":
				fillHLine(new_lines, i)
				fillVLine(new_lines, n)
	print(new_lines)


def fillVLine(tab: list, index: int):
	for i in range(len(tab)):
		tab[i][index] = "T"


def fillHLine(tab: list, index: int):
	tab[index] = ["T"] * len(tab[index])
	pass



with open("input1.txt", "r") as file:
	lines = file.read().split("\n")
for n in range(len(lines)):
	lines[n] = lines[n].split()
# print(lines)
estCoincer(lines)


