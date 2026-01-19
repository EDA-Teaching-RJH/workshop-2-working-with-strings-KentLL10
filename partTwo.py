import math  

def main():
    A = int(input("Input side A as an integer: "))
    B = int(input("input side B as an integer: ")) #TO DO 
    C = pythag(A, B)
    print(C)

def pythag(A,B):
    C2 = (A ** 2) + (B ** 2)
    C = math.sqrt(C2)
    return C
main()
