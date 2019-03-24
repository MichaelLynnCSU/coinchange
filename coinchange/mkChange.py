# A program to compute a logically recursive formula, using both
# recursion (divide and conquer) and building up a table of answers
# to subproblems (dynamic programming).
# Which do you think will be faster, for which sizes of input?
# Do you think dynamic programming can be used to make MergeSort
# (another divide and conquer algorithm) faster?
from array import array
import sys

coins = []
calls = 0
reads = 0
# Set recursion limit
sys.setrecursionlimit(1000000000)

# read coin values
def readCoins(fnm):
   global coins
   f = open(fnm)
   for line in f:
      l = line.strip().split(" ")
      for c in l:
        coins.append(int(c))
   if db: print("coins:", coins)

my_mem  = {}

def mkChangeDC(money, numberCoins):
      # """Divide and Conquer. n is the amount to make change for.
  # Should only consider coins with indices [0, c] (inclusive inclusive)."""
    global calls
    calls += 1
    if money == 0:
        return 1
    if money < 0 or numberCoins < 0:
        return 0

    #print(coins)
    #print(tuple(coins))

    mykeys = (money, numberCoins, tuple(coins))

   # print(money, "and", numberCoins, "and", tuple(coins) )
    # MEMOIZATION TOP DOWN ( RECURSIVE )
    if mykeys not in my_mem :
        my_mem [mykeys] =  mkChangeDC(money, numberCoins - 1) + mkChangeDC(money - coins[numberCoins - 1], numberCoins)

    return my_mem [mykeys]


def mkChangeDP(money):
       #"""Dynamic Programming. n is the amount to make change for.
   #Should consider all coins."""
    global reads

    myResults = [0 for _ in range(money + 1)]
   # print(myResults)
    myResults[0] = 1

    # BOTTOM UP ( ITERATIVE )
    for mycoin in coins:
        for i in range(mycoin, money + 1):
           # print(i, "and", mycoin)
            myResults[i] += myResults[i - mycoin]
            reads+=1
    return myResults[money]

if __name__ == "__main__":
   db = len(sys.argv)>3

   money = int(sys.argv[1])

   fnm = sys.argv[2]

   readCoins(fnm)

   numberCoins = len(coins) - 1


  # print("numberCoins", numberCoins)
  # print("money", money)
  # print(mkChangeDC(numberCoins,money))
  # ways = mkChangeDC(money,numberCoins)

   #print("mkChangeDC")

  # print("amount:", money, "coins:", coins, "ways:", ways, "calls:", calls)

   ways = mkChangeDP(money)

   print("mkChangeDP")

   print("amount:", money, "coins:", coins, "ways:", ways, "reads:", reads)
