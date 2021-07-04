def readFileAndPrintContent():
    with open('fillerlist.txt') as f:
        lines = f.readlines()
        print(lines)
        f.close()

readFileAndPrintContent()