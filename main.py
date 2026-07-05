from counter import count_words, count_characters, count_lines

print("Enter your text (press Enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

print("\nAnalysis")
print(f"Words      : {count_words(text)}")
print(f"Characters : {count_characters(text)}")
print(f"Lines      : {count_lines(text)}")
