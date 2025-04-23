def minmax(depth, nodeIndex, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        return max(
            minmax(depth + 1, nodeIndex * 2, False, scores, h),
            minmax(depth + 1, nodeIndex * 2 + 1, False, scores, h)
        )
    else:
        return min(
            minmax(depth + 1, nodeIndex * 2, True, scores, h),
            minmax(depth + 1, nodeIndex * 2 + 1, True, scores, h)
        )

scores = [3, 5, 6, 9, 1, 2, 0, -1]
h = 3
print("\nOptimal value (Min-Max):", minmax(0, 0, True, scores, h))
