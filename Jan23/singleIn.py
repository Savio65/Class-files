class A:
    def show(self):
        print("I am in A method")
class B(A):
    def show(self):
        A.show(self)
        print("I am in B method")
b=B()
b.show()