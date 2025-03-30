def knapsack(weights, values, W):
    n = len(weights)
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 1: Solve the knapsack problem using dynamic programming
    def knapsack_dp(i, w):
        # Base case
        if i == 0 or w == 0:
            return 0

        # Return from memo if already calculated
        if memo[i][w] != -1:
            return memo[i][w]

        # Case: Item weight is greater than capacity
        if weights[i - 1] > w:
            memo[i][w] = knapsack_dp(i - 1, w)
        else:
            # Max of including or excluding the current item
            memo[i][w] = max(
                values[i - 1] + knapsack_dp(i - 1, w - weights[i - 1]),
                knapsack_dp(i - 1, w)
            )

        return memo[i][w]

    # Step 2: Backtrack to find selected items
    def find_selected_items():
        selected = []
        i, w = n, W

        while i > 0 and w > 0:
            # If the value is different, the item was included
            if memo[i][w] != memo[i - 1][w]:
                selected.append(i - 1)
                w -= weights[i - 1]
            i -= 1

        return selected

    # Step 3: Get results
    max_value = knapsack_dp(n, W)
    selected_items = find_selected_items()

    return max_value, selected_items

# Test case
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

max_value, selected_items = knapsack(weights, values, W)
print("Maximum Value:", max_value)
print("Selected Items (indices):", selected_items)
