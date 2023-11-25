import mymath
import mykeyboard

if __name__ == "__main__":
    a=int(input('Enter a number: '))
    b=mymath.generate_number()

    
    if a==b:
        print('You won the game!!')
