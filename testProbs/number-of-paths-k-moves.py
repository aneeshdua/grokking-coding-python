"""
In a distant land, nestled among rolling hills and ancient forests, lies the Enchanted Kingdom, a realm of magic and wonder. Within this mystical land, there is a square grid with dimensions n by m, where each square is denoted by (x, y), representing the x-th row from the top and y-th column from the left. In this grid, a special character known as the Seeker, with its extraordinary ability move through the grid, starts at position (x1,y1) and must find its way to a distant square at position (x2, y2) after K moves, where each move involves the Seeker being placed in a square that shares either the same row or the same column as its current position. The Seeker must not remain in the same square throughout the moves. Can you determine the number of valid sequences of moves the Seeker can make to reach the target position? Please provide the answer modulo 998244353.

Constraints:
The dimensions of the grid satisfy ≤ 10^9.
The number of moves K satisfies ≤ 10^6.
1 ≤ x1, x2 ≤ n and 1 ≤ y1, y2 ≤ m.

Example -

Input:
n: 3
m: 4
k: 3
startingPosition: [1, 2]
endingPosition: [2, 3]

Output: 9

Explanation
There are 9 possible sequence of reaching [2,3] from [1,2]

[1,2] -> [1,4] -> [2,4] -> [2,3]
[1,2] -> [1,3] -> [3,3] -> [2,3]
[1,2] -> [1,4] -> [1,3] -> [2,3]
[1,2] -> [1,1] -> [1,3] -> [2,3]
[1,2] -> [1,1] -> [2,1] -> [2,3]
[1,2] -> [2,2] -> [2,1] -> [2,3]
[1,2] -> [3,2] -> [3,3] -> [2,3]
[1,2] -> [2,2] -> [2,4] -> [2,3]
[1,2] -> [3,2] -> [2,2] -> [2,3]
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_sequences(n, m, x1, y1, x2, y2, K):
    MOD = 998244353
    
    # Calculate the number of right moves (R) and downward moves (D)
    R = y2 - y1
    D = x2 - x1
    
    # Calculate the number of permutations
    permutations = factorial(K) // (factorial(R) * factorial(D))
    
    return permutations % MOD

# Input
n, m = 3, 4
x1, y1 = 1, 2
x2, y2 = 2, 3
K = 3

# Output
print(count_sequences(n, m, x1, y1, x2, y2, K))

