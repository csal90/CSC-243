# countdown(n) prints numbers from n to 1 followed by 'Blast off!'
# countdown(5)
# 5
# 4
# 3
# 2
# 1
# Blast off!

def countdown(n):
    if n == 0:
        print('Blast off!')  # dont make a recursive call if the number is 0.
    else:
        print(n)
        countdown(n - 1)  # keep doing n - 1 until n is 0.
