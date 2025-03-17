data = np.array([(1, 'Alice', 50000), (2, 'Bob', 60000)],
                dtype=[('ID', 'i4'), ('Name', 'U10'), ('Salary', 'f4')])
print(data['Name'])  # Sirf names extract karega
