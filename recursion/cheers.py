# cheers(n) prints 'Hip' for n-1 times followed but 'Hurrah', one message one line.
# cheers(3)
# Hip
# Hip
# Hurrah

def cheers(n):
    if n == 1:
        print('Hurrah')
    else:
        print('Hip')
        cheers(n - 1)
