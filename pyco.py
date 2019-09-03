import re

class Pyco():

    boxes = 'cfb' # class, function, block

    def __init__(self, fileType='unix',spnum=4):
        self.code = list()
        self.indentLevel = 0
        self.setFileType(fileType)
        self.setIndent2space(spnum)

    def setFileType(self,fileType):
        self.fileType = fileType if fileType in ['unix','windows','mac'] else 'unix'
        self.eol = '\n' if fileType == 'unix' else '\r\n' if fileType == 'windows' else '\r'

    def setIndent2space(self,spnum):
        spnum = int(spnum)
        if spnum:
            self.indent2space = spnum

    def dent(self):
        self.indentLevel = self.indentLevel - 1

    def indent(self):
        self.indentLevel = self.indentLevel + 1

    def add(self, strline):
        '''
        add one string line to code
        '''
        strline = strline.strip()
        self.code.append((strline, self.indentLevel))
        box = self.getBoxTypeByStrLine(strline)
        if box is not None:
            if box in self.boxes:
                self.indentLevel = self.indentLevel + 1

    def addline(self):
        '''
        add a blank line to code
        '''
        self.code.append(('',0));

    def getBoxTypeByStrLine(self,strline):
        if strline[0:4] == 'class ':
            return 'c'
        elif strline[0:4] == 'def ':
            return 'f'
        elif strline[-1:] in ':{([':
            return 'b'
        else:
            return None

    def escape(self,boxtype='b',closer=None):

        '''
        escape from box such as class (c), function (f), or block (b)
        '''

        if boxtype in self.boxes:
            p = re.compile('[\}\)\]]\s?,?')

            for strline, indentLevel in reversed(self.code):
                strline = strline.strip()
                if strline:
                    if (boxtype == self.getBoxTypeByStrLine(strline)) and (self.indentLevel > indentLevel):
                        self.indentLevel = indentLevel
                        if closer is not None:
                            if closer == p.match(closer).group():
                                self.add(closer)
                        if boxtype == 'c':
                            self.addline()
                            self.addline()
                        elif boxtype == 'f':
                            self.addline()
                        break

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
