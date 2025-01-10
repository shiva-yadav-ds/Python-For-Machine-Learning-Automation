row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


position = int(position)  # Convert input to integer
row = position % 10 - 1  # Get row (second digit - 1)
col = position // 10 - 1  # Get column (first digit - 1)

# Place X at the specified position
map[row][col] = "X"

# Print the updated map
print(f"{map[0]}\n{map[1]}\n{map[2]}")