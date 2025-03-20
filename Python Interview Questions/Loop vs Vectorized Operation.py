arr = np.arange(1000000)

# Loop Method (Slow)
start = time.time()
result = [x ** 2 for x in arr]
print("Loop Time:", time.time() - start)

# NumPy Vectorized (Fast)
start = time.time()
result = arr ** 2
print("NumPy Time:", time.time() - start)
