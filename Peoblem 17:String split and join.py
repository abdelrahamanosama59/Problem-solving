def split_and_join(line):
    word = line.split(" ")
    line = "-".join(word)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
