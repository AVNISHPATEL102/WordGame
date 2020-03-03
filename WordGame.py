import random

wordList = ['CODE', 'ERROR', 'EXECUTE', 'JAVA', 'FORTRAN','BLOOD','POTATOES','PANIC','STOMACH','CRAMP','PAIN']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

wordList.sort(key=len)

def biggestWord(wL):
    maxLength = 0
    for i in wL:
        if (len(i) > maxLength):
            maxLength = len(i)
    return maxLength


def totalLengthOfWords(wL):
    sentence=''
    for i in wL:
        sentence= sentence + i
    le = len(sentence)
    return le


lensentence = totalLengthOfWords(wordList)
longestword = biggestWord(wordList)
totalwords=len(wordList)

grid = None
temp = wordList.copy()
if totalwords > longestword:
    grid = [[None for _ in range(totalwords+6)] for _ in range(totalwords+6)]
else:
    grid = [[None for _ in range(longestword+6)] for _ in range(longestword+6)]

def spacerigthrow(gr, st, r, c):
    for x in range(len(st)):
        if gr[r][c] != None:
            return False
        else:
            c = c + 1
    return True


def spaceleftrow(gr,st,r,c):
    for x in range(len(st)):
        if gr[r][c] != None:
            return False
        else:
            c=c-1
    return True

def spacedowncolumn(gr,st,r,c):
    for x in range(len(st)):
        if gr[r][c] != None:
            return False
        else:
            r=r+1
    return True

def spaceupcolumn(gr,st,r,c):
    for x in range(len(st)):
        if gr[r][c] != None:
            return False
        else:
            r=r-1
    return True

def settingGrid(wl,gr):

    count=1
    r=None
    c=None
    for x in range(len(wl)):
        word = wl[-1]

        if count==1:
            a=True
            while a:
                r = random.randint(0,(len(gr)-1))
                c = random.randint(0,(len(gr)-len(word)))
                if spacerigthrow(gr,word,r,c):
                    for i in range(len(word)):
                        gr[r][c]=word[i]
                        c+=1
                    a=False
        elif count ==2:
            b=True
            while b:
                r = random.randint(0, (len(gr) - 1))
                c = random.randint(len(word), (len(gr) - 1))
                if spaceleftrow(gr, word, r, c):
                    for i in range(len(word)):
                        gr[r][c] = word[i]
                        c -= 1
                    b=False
        elif count ==3:
            c=True
            while c:
                r = random.randint(0, (len(gr) - len(word)))
                c = random.randint(0, (len(gr) - 1))
                if spacedowncolumn(gr, word, r, c):
                    for i in range(len(word)):
                        gr[r][c] = word[i]
                        r += 1
                    c=False
        elif count==4:
            d=True
            while d:
                r = random.randint(len(word), (len(gr) - 1))
                c = random.randint(0, (len(gr) - 1))
                if spaceupcolumn(gr, word, r, c):
                    for i in range(len(word)):
                        gr[r][c] = word[i]
                        r -= 1
                    d=False
        if(count >= 4):
            count=1
        else:
            count+=1
        wl.pop(-1)



settingGrid(wordList,grid)


for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == None:
            tempo = random.randint(0,(len(letters)-1))
            grid[i][j] = letters[tempo]


for i in range(len(grid)):
    for j in range(len(grid)):
        print("{}".format(grid[i][j]),end='\t')
    print(" ")











