import re


class FuncionsCounter:
    def countFunctions(file):
        functionsCount = 0
        fileContent = iter(file.readlines())

        for line in fileContent:
            stringContainsFunction = re.match(r"\S+(?:\s\S+)*\(", line)
            if stringContainsFunction:
                print(line)
                if re.match("\{$", line):
                    functionsCount += 1
                else:
                    nextLine = next(fileContent)
                    blockOpening = re.match("^\{", nextLine)
                    if blockOpening:
                        functionsCount += 1

        print("Counted functions in you file:" + str(functionsCount))
        print()
