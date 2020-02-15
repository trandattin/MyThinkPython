class Kangaroo:
    def __init__(self, name, contents = None):
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        t = [ self.name + ' has pouch contents:']
        for i in self.pouch_contents:
            s = '   ' + object.__str__(i)
            t.append(s)
        return '\n'.join(t)

    def put_incleaer_pouch(self, item):
        self.pouch_contents.append(item)


def main():
    kanga = Kangaroo("Kanga")
    kanga.put_incleaer_pouch("tin")
    roo = Kangaroo("Roo")
    roo.put_incleaer_pouch("nhi")

    print(kanga)
    print(roo)



if __name__ == "__main__":
    main()