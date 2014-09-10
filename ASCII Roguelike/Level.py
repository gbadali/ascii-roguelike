class Level(object):
    """Do Level stuff, create a level file, read the file, change things about level, etc"""
    
    def CreateLevel():
        level = 1
        levelFileName = 'level' + level + '.txt'
        levelFile = open(levelFileName, a)
        # for now just create an empty level with walls all around
        for i in range(24):
            for j in range(80):
                if i == 1 or i == 24:
                    line = '#' * 80
                else:
                    line = '#' + ('.' * 78) + '#'
            levelFile.write(line)


if '__name__' == __main__:
    level = Level()
    print(level)
