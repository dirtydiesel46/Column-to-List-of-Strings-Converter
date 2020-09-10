def convert(list):
    return tuple(list)

print("This program takes out the first row, which is usually the header rows, and strings up the subsequent rows")
cont = 'y'
while cont == 'y':
    MultiLine = []
    print("Enter rows to stringify: ")
    while True:
        line = input()
        if line:
            MultiLine.append(line)
        else:
            break
    finalText = '\n'.join(MultiLine)

    strings = finalText
    string = strings.split("\n")
    string.pop(0)

    print("Copy below line: ")
    print(convert(string))
    cont = str(input("Do you want to continue? (y/n):   ")).lower()
