with open("input.txt", "w") as f:
    f.write("Line 1: Python File Handling\n")
    f.write("Line 2: Reading and Writing Files\n")
    f.write("Line 3: Counting total lines\n")

with open("input.txt", "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))

extracted_lines = lines[:2]
with open("output.txt", "w") as f:
    f.writelines(extracted_lines)

print("Extracted lines saved to output.txt")