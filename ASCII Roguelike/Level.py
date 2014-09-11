class Level(object):
    """Do Level stuff, create a level file, read the file, change things about level, etc"""
    def __init__(self):
        #TODO use inputs to create a level of a certain size.
        #TODO use inputs alternately load or create a level.
        pass

    def createLevel(self):
        level = 1
        levelFileName = 'level' + str(level) + '.txt'
        # using 'w' to erase anything that might still be in a file
        levelFile = open(levelFileName, 'w')
        # for now just create an empty level with walls all around
        for i in range(24):
            for j in range(80):
                if i == 1 or i == 24:
                    line = '#' * 80 + '\n'
                else:
                    line = '#' + ('.' * 78) + '#' + '\n'
            levelFile.write(line)
        levelFile.close()


    def printLevel(self):
        pass



if __name__ == '__main__':
    level = Level()
    print(level)
