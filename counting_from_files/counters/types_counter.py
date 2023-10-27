import re

types_in_c = {
    "char",
    "unsigned char",
    "signed char",
    "int",
    "unsigned int",
    "short",
    "long",
    "unsigned long",
    "float",
    "double",
    "long double",
    "void",
}


class TypesCounter:
    # Check if it's not a function
    def countIntTypes(file):
        intCount = 0
        fileContent = iter(file.readlines())
        for line in fileContent:
            lineContainsInt = re.match(r"\s+(int)(?:\s\S+)*(\=|\;)", line)
            if lineContainsInt:
                intCount += 1
        print("File contains: " + str(intCount) + " int declarations\n")

    def countVoidTypes(file):
        floatCount = 0
        fileContent = iter(file.readlines())
        for line in fileContent:
            lineContainsVoid = re.match(r"(?:\s\S+)*(void)(?:\s\S+)*\(", line)
            if lineContainsVoid:
                floatCount += 1
        print("File contains: " + str(floatCount) + " voids declarations\n")

    def countFloatTypes(file):
        floatCount = 0
        fileContent = iter(file.readlines())
        for line in fileContent:
            lineContainsFloat = re.match(r"\s+(float)(?:\s\S+)*(\=|\;)", line)
            if lineContainsFloat:
                floatCount += 1
        print("File contains: " + str(floatCount) + " floats declarations\n")
