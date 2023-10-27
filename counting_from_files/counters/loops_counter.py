class CountLoops:
    def countLoops(file):
        forCount = 0
        whileCount = 0
        doWhileCount = 0
        for line in file.readlines():
            if "for" in line:
                forCount += 1
            elif "while" in line:
                whileCount += 1
            elif "do /{" in line:
                doWhileCount += 1

        print("Counted loops in you file:\n")
        print("1. For: " + str(forCount))
        print("2. While: " + str(whileCount))
        print("3. DoWhile: " + str(doWhileCount))
        print()
