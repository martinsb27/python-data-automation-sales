import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

productos = [
    ("Laptop", "Electrónica"),
    ("Mouse", "Electrónica"),
    ("Camiseta", "Ropa"),
    ("Zapatos", "Ropa"),
    ("Manzana", "Alimentos"),
    ("Banana", "Alimentos")
]

fechas = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(10)]

data = []
for _ in range(15):
    fecha = random.choice(fechas)
    producto, categoria = random.choice(productos)
    cantidad = random.randint(1, 20) if random.random() > 0.1 else None
    precio = round(random.uniform(0.5, 1500), 2) if random.random() > 0.1 else None
    producto = f" {producto.upper() if random.random() < 0.5 else producto.lower()} "
    categoria = f"{categoria.lower() if random.random() < 0.5 else categoria.upper()} "
    if random.random() < 0.1:
        fecha = None
    data.append([fecha, producto, categoria, cantidad, precio])

df = pd.DataFrame(data, columns=["Fecha", "Producto", "Categoría", "Cantidad", "Precio"])
df = pd.concat([df, df.sample(2, random_state=42)], ignore_index=True)

df.to_csv("ventas.csv", index=False)
print("Archivo 'ventas.csv' generado correctamente.")
