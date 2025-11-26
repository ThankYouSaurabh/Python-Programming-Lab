try:
    with open("input.txt") as f:
        words = f.read().lower().split()

    words.sort()

    with open("output.txt", "w") as f:
        f.write(" ".join(words))

    print("Words sorted and written to output.txt")
except Exception as e:
    print("Error:", e)
