# Usando lista por comprensión
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

# Usando generador
for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()
