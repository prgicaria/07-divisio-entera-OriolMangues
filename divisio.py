print('aquest programa realitza una divisió')
a=float(input('divisor'))
b=float(input('dividend'))
D=b//a
r=b%a
if a==0:
    print('no es por realitzar una divisió entre 0')
else: 
    print('divisio:',b,'/',a)
    print('quocient:',D)
    print('residu:',r)