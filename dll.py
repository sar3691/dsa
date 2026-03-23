class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
        self.pre=None

class DLL:
    def __init__(self):
        self.head=None

    def add_f(self,data):
        new=Node(data)
        if self.head != None:
            self.head.pre=new
            new.link=self.head

        self.head=new

    def add_l(self,data):
        new=Node(data)
        if self.head == None:
            self.head=new
            return

        temp=self.head
        while temp.link:
            temp=temp.link

        temp.link=new
        new.pre=temp

    def display(self):
        temp=self.head

        while temp.link:
            print(temp.data)
            temp=temp.link

        print(temp.data)




    def dl_f(self):
        if self.head==None:
            print("empty")
            return
        self.head=self.head.link

        if self.head:
            self.head.pre=None

    def dl_l(self):

        if self.head==None:
            print("empty")
            return
        temp=self.head
        while temp.link:
            temp=temp.link
        if temp.pre:
            temp.pre.link=None
        else:
            self.head=None


dll=DLL()
dll.add_f(10)
dll.add_f(20)
dll.add_l(30)
dll.add_l(25)
dll.display()

dll.dl_f()
dll.dl_l()
dll.display()





