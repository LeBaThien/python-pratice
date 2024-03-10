

def cat(*items, delim: str):
    return delim.join(items)


if __name__ == '__main__':
    print(cat("thien", "Le", delim="/"))