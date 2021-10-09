if __name__ == "__main__":
    ids, words = [], []
    with open("./mapping.csv", "r") as f:
        for line in f:
            id, word = line.strip().split(",")
            if (word != "NA"):
                ids.append(id)
                words.append(word)
    print(f"# of valid word: {len(words)}")
    with open("./frontend/src/data.js", "w") as f:
        f.write("const word2idx = {\n")
        for word, idx in zip(words, ids):
            f.write(f'\t"{word}" : {idx},\n')
        f.write("}\n")
        f.write("export { word2idx };\n")