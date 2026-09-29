try:
    # Open input.txt in read mode
    with open("input.txt", "r") as file:
        lines = file.readlines()

    # Count total number of lines
    total_lines = len(lines)

    # Extract first two lines
    first_two_lines = lines[:2]

    # Open output.txt in write mode
    with open("output.txt", "w") as file:
        file.write("Total number of lines: " + str(total_lines) + "\n")
        file.write("First two lines:\n")

        for line in first_two_lines:
            file.write(line)

    print("Result saved in output.txt")

except FileNotFoundError:
    print("input.txt file not found")

except Exception as e:
    print("Error:", e)
