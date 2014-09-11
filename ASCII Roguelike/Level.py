class Level(object):
    """Do Level stuff, create a level file, read the file, change things about level, etc"""
    def __init__(self):
        #TODO use inputs to create a level of a certain size.
        #TODO use inputs alternately load or create a level.
        pass

    def createLevel(self, level):
        level = level
        levelFileName = 'level' + str(level) + '.txt'
        # using 'w' to erase anything that might still be in a file
        levelFile = open(levelFileName, 'w')
        # for now just create an empty level with walls all around
        for i in range(24):
            for j in range(80):
                if i == 0 or i == 23:
                    line = '#' * 80 + '\n'
                else:
                    line = '#' + ('.' * 78) + '#' + '\n'
            levelFile.write(line)
        levelFile.close()

    def readLevel(self, level):
        level = level
        levelFileName = 'level' + str(level) + '.txt'
        levelFile = open(levelFileName)



    def printLevel(self, level):
        level = level
        levelFileName = 'level' + str(level) + '.txt'
        levelFile = open(levelFileName)
        for line in levelFile:
            print(line)
        levelFile.close()



if __name__ == '__main__':
    level = Level()
    print(level)
