def cat(a: str, b: str, /, *, delim: str):
    return delim.join([a, b])


if __name__ == "__main__":
    print(cat("John", "Doe", delim=" "))
