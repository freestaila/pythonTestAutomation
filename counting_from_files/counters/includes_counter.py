import re


class IncludesCounter:
    def listOfIncludesInFile(file):
        includesList = []
        fileContent = iter(file.readlines())
        for line in fileContent:
            lineContainsInclude = re.match("#include", line)
            if lineContainsInclude:
                includesList.append(line)
        return includesList
