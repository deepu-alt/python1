#trapping rain water(1D version, no function)

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

l = 0
r = len(height) - 1

leftMax = height[l]
rightMax = height[r]

water = 0

while l < r:
    if leftMax < rightMax:
        l += 1
        leftMax = max(leftMax, height[l])
        water += leftMax - height[l]
    else:
        r -= 1
        rightMax = max(rightMax, height[r])
        water += rightMax - height[r]

print(water)

#time complexity : O(n)
# space complexity : O(1)
#instead of checking both side every time :
# you trust smaller boundary
# if left side is smaller -> process left
# if right side is smaller -> process right
# this avoids O(n**2) brute force.


# N-Queens (Single Script)

n = 4

board = [["."] * n for _ in range(n)]

col = set()
posDiag = set()
negDiag = set()

res = []

stack = [(0, col.copy(), posDiag.copy(), negDiag.copy(), board)]

while stack:
    r, col, posDiag, negDiag, board = stack.pop()

    if r == n:
        res.append(["".join(row) for row in board])
        continue

    for c in range(n-1, -1, -1):
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue

        new_board = [row[:] for row in board]
        new_board[r][c] = "Q"

        new_col = col.copy()
        new_pos = posDiag.copy()
        new_neg = negDiag.copy()

        new_col.add(c)
        new_pos.add(r+c)
        new_neg.add(r-c)

        stack.append((r+1, new_col, new_pos, new_neg, new_board))

print(res)