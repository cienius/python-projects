import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="put type of question", choices=['annuity', 'diff'], type=str)
parser.add_argument("--principal", help="put amount of money", type=int)
parser.add_argument("--payment", help=" is the monthly payment amount.", type=int)
parser.add_argument("--periods", help="denotes the number of months needed to repay the loan.", type=int)
parser.add_argument("--interest", help="is specified without a percent sign.", type=float)
#creditcalc.py --type=diff --principal=1000 --interest=10 --periods=10 --payment=10
lol = []
trol =[]
m = 0
args = parser.parse_args()

def checker():
    lol.clear()
    if args.type is None or args.interest is None:
        print('Incorrect parameters')
        return
    elif args.type =='diff' and args.payment:
        print('Incorrect parameters')
        return
    elif args.interest is not None:
        lol.append(args.type)
        lol.append(args.interest)
        if args.interest <0:
            print('Incorrect parameters')
            return
    if args.principal is not None:
        lol.append(args.principal)
        if args.principal <0:
            print('Incorrect parameters')
            return
    if args.periods is not None:
        
        lol.append(args.periods)
        if args.periods <0:
            print('Incorrect parameters')
            return


    if args.payment is not None:
        lol.append(args.payment)
        if args.payment <0:
            print('Incorrect parameters')
            return
    if len(lol) <4:
        print('Incorrect parameters')
        return
    #print(lol)
    #print(len(lol))

checker()

if args.type =='diff' and args.periods is not None and args.interest is not None:
   for lolo in range(args.periods):
       i = (args.interest * 0.01)/12
       m+=1
       d = (args.principal/args.periods)+ i*(args.principal-(args.principal*(m-1)/args.periods))
       trol.append(math.ceil(d))
       print(f'Month {int(m)}: payment is {int(math.ceil(d))}')
       if m==args.periods:
           print()
           print('Overpayment =', sum(trol)-args.principal)
       
if args.type =='annuity' and args.periods is not None and args.payment is None: 
    i = (args.interest * 0.01)/12
    kolo =(1+i)**args.periods
    a=int(math.ceil(args.principal*((i*kolo)/(kolo-1))))
    print(f'Your annuity payment = {int(math.ceil(a))}!')
    print('Overpayment =', (args.periods*a)-args.principal)


if args.type =='annuity' and args.periods is not None and args.payment is not None:
    i = (args.interest * 0.01)/12
    kolo =(1+i)**args.periods
    p = int(math.floor(args.payment/((i*kolo)/(kolo-1))))
    print(f'Your loan principal = {int(math.floor(p))}!')
    print('Overpayment =', (args.payment*args.periods)-p)

if args.type =='annuity' and args.periods is None and args.interest is not None:
    i = (args.interest * 0.01)/12
    lolek = float((args.payment/(args.payment - i*args.principal)))
    n = math.ceil(math.log(lolek, 1+i))
    print(n)
    if int(n%12) ==0:
        print('It will take', int(n/12),'years', 'to repay the loan!')
    if n <=12: 
        print('It will take', int(n), 'months to repay the loan!')
    if n>12 and int(n%12) !=0: print('It will take', int(n/12),'years', 'and',(n%12), 'months to repay the loan!')
    print('Overpayment =', (args.payment*n)-args.principal)