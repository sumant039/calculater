class calc :
    def Add ( self, A, B ):
        print (A + B)
    def Sub (self, A, B ):
        print (A - B)
    def Mul (self, A, B ):
        print (A * B)
    def Div (self, A, B ):
        print (A / B)
C = calc()
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

Input = int (input ("Enter the choice:"))
A = int (input ("Enter A:"))
B = int (input ("Enter B:"))
if Input == 1:
    C.Add (A,B)
elif Input == 2:
    C.Sub (A,B)
elif Input == 3:
    C.Mul (A,B)
elif Input == 4:
    C.Div (A,B)
else:
    print ("Its not avaliable try again")

