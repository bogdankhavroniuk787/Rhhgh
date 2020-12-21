from factorial.factorial import fac
from exp_root.exponentiation import exp2,exp3
from exp_root.root import root2,root3
from logarithm.logarithm import log , ln , lg

def main():
    while True :
        try:

           needed_function = int(input("яку функцію ви хочете запустити? якщо факторіал 1 , квадрат натисніть 2, куб натисніть 3, квадратний корінь 4,"+"\n"+"кубічний корінь 5 ,логарифм 6, натуральний логарифм 7 ,десятковий логарифм 8. "))
           if needed_function in range(1,9):
               break
        except ValueError :
            print("ви ввели не ціле число")
    while True:
        try:
            n = float(input("введіть аргумент"))
            break
        except ValueError :
            print("ви ввели не дробове число")
    if needed_function ==1 :
        print(fac(n))
    if needed_function == 2:
        exp2(n)
    if needed_function == 3:
        exp3(n)
    if needed_function == 4:
        root2(n)
    if needed_function == 5:
        root3(n)
    if needed_function == 6:
        while True:
            try:
                base = float(input("введіть базу логарифму"))
                if base>0 and base!=1 :
                   break
                else:
                    print("ви ввели не правильну базу")
            except ValueError:
                print("ви ввели не дробове число")
        if n > 0:
                log(base,n)
        else:
                print("не можливо знайти логарифм для даного числа")
    if needed_function == 7:
        if n > 0:
            ln(n)
        else:
            print("не можливо знайти логарифм для даного числа")
    if needed_function == 8:
        if n > 0:
            lg(n)
        else:
            print("не можливо знайти логарифм для даного числа")
if __name__ == '__main__':
    main()


