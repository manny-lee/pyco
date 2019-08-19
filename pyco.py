class Pyco():

    currIndentLevel = 0
    boxes = ['c','f','b'] # class, function, block

    def __init__(self, fileType='unix',spnum=4):
        self.code = list()
        self.setFileType(fileType)
        self.setIndent2space(spnum)

    def setFileType(self,fileType):
        self.fileType = fileType if fileType in ['unix','windows','mac'] else 'unix'
        self.eol = '\n' if fileType == 'unix' else '\r\n' if fileType == 'windows' else '\r'

    def setIndent2space(self,spnum):
        spnum = int(spnum)
        if spnum:
            self.indent2space = spnum

    def add(self, strline):
        '''
        add one string line to code
        '''
        strline = strline.strip()
        self.code.append((strline, self.currIndentLevel))
        box = self.getBoxTypeByFirstLine(strline)
        if box in self.boxes:
            self.currIndentLevel = self.currIndentLevel + 1

    def addline(self):
        '''
        add a blank line to code
        '''
        self.code.append(('',0));

    def getBoxTypeByFirstLine(self,strline):
        if strline[0:4] == 'class ':
            return 'c'
        elif strline[0:4] == 'def ':
            return 'f'
        elif strline[-1:] == ':':
            return 'b'
        else:
            return None

    def escape(self,box='b'):
        '''
        escape from box such as class (c), function (f), or block (b)
        '''
        reversedCode = sorted(self.code, reverse=True)
        if box in self.boxes:
            for strline, indentLevel in reversedCode:
                strline = strline.strip()
                if box == self.getBoxTypeByFirstLine(strline):
                    self.currIndentLevel = indentLevel
                    if box == 'c':
                        self.addline()
                        self.addline()
                    elif box == 'f':
                        self.addline()
                    break

    def escadd(self,box,strline):
        '''
        escape from box and add a string line
        '''
        self.escape(box)
        self.add(strline)

    def get(self):
        '''
        get all the codes to written
        '''
        content = list()

        for strline, indentLevel in self.code:
            strlen = len(strline) + indentLevel * self.indent2space
            content.append(strline.rjust(strlen))

        content.append('')
        return self.eol.join(content)

    def print(self):
        '''
        print all the codes to screen
        '''
        print(self.get())

    def make(self,filePath):
        '''
        make file from the codes
        '''
        with open(filePath,'w') as f:
            f.write(self.get())
