def plural_or_single(word, amount):
    if amount == 0:
        return ""
    elif amount == 1:
        return f"{amount} {word}"
    else:
        return f"{amount} {word}s"

if __name__ == "__main__":
    print("please run main.py")
