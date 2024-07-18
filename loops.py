def power (n , p):
    if p == 0: return 1 
    return (n*power(n, p-1))
if __name__ == '__main__':
    n =float(input('enter the number'))
    p = int(input('enter the power'))
print (power(n , p)) 