import pulp

# Створення проблеми лінійного програмування
prob = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Функція цілі: максимізувати загальну кількість вироблених продуктів
prob += x1 + x2, "Total_Products"

# Обмеження ресурсів
prob += 2 * x1 + 1 * x2 <= 100, "Water_Limit"
prob += 1 * x1 <= 50, "Sugar_Limit"
prob += 1 * x1 <= 30, "LemonJuice_Limit"
prob += 2 * x2 <= 40, "FruitPuree_Limit"

# Розв'язання задачі
prob.solve()

# Вивід результатів
print("Статус розв'язку:", pulp.LpStatus[prob.status])

print("Оптимальна кількість виробленого Лимонаду:", pulp.value(x1))
print("Оптимальна кількість виробленого Фруктового соку:", pulp.value(x2))
print("Максимальна загальна кількість продуктів:", pulp.value(prob.objective))
