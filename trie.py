class trienode:
    def __init__(self):
        self.child = {}
        self.end = False


class trie:
    def __init__(self):
        self.root = self.getroot()

    def getroot(self):
        return trienode()

    def insert(self, key):
        pc = self.root
        for elem in key:
            if not pc.child.get(elem):
                #print('eleme', elem)
                pc.child[elem] = self.getroot()
                pc = pc.child[elem]
            else:

                pc = pc.child[elem]
                #print('elems', pc)
                if pc.end:
                    pc.end = False

        pc.end = True

    def search(self, key):
        pc = self.root
        for elem in key:
            if not pc.child.get(elem):
                #print('elemsdd', elem)
                return False
            else:
                pc = pc.child[elem]

        return True

