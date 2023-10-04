n, m = int(input('n=')), int(input('m='))
res = f"{'*' * n}\n" + f"*{' ' * (n - 2)}*\n" * (m - 2) + f"{'*' * n}\n"
print(res)

