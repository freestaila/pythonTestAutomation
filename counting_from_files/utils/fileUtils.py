class FileUtils:
    def openFile():
        while True:
            try:
                path = str(input("Provide file path:"))
                return open(path, "r")
            except:
                print("File not exists. Please provide correct file path ...")
                continue
            break

    def safeToFile(includesList, fileName):
        open(fileName, "x")
        with open(fileName, "w") as file:
            for item in includesList:
                # write each item on a new line
                file.write("%s\n" % item)
        print("File saved")
