import pulp as plp

model = plp.LpProblem("Homemade drinks Company", plp.LpMaximize)

Lemonade = plp.LpVariable("Lemonade", lowBound = 0, cat='Integer')
Fruit_juice = plp.LpVariable("Fruit_juice", lowBound = 0, cat='Integer')

model += Lemonade + Fruit_juice, "Profit"

model += 2 * Lemonade + Fruit_juice <= 100, "water"
model += Lemonade <= 30, "lemon_juice"
# model += Lemonade <= 50, "sugar"   
# наявність додаткового обмеження на цукор ніяк не 
# вплииває на задачу, оскількии лімітуючим фактором є  лимонний сік
model += 2 * Fruit_juice <= 40, "fruit_puree"

model.solve()
print(f"Status: {plp.LpStatus[model.status]}")

print(f"Lemonade = {plp.value(Lemonade)}")
print(f"Fruit_juice = {plp.value(Fruit_juice)}")

print(f"Max_Profit = {plp.value(model.objective)}")