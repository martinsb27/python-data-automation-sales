import pandas as pd
import random
from datetime import datetime, timedelta

# -------------------------------
# Configuración inicial
# -------------------------------
random.seed(42)

# Productos y categorías
productos = [
    ("Laptop", "Electrónica"),
    ("Mouse", "Electrónica"),
    ("Teclado", "Electrónica"),
    ("Camiseta", "Ropa"),
    ("Zapatos", "Ropa"),
    ("Chaqueta", "Ropa"),
    ("Manzana", "Alimentos"),
    ("Banana", "Alimentos"),
    ("Leche", "Alimentos")
]

# Fechas: todo enero 2026
fechas = [datetime(2026, 1, 1) + timedelta(days=i) for i in range(31)]

# -------------------------------
# 1. Generar 100 filas de ventas
# -------------------------------
data = []
for _ in range(100):
    fecha = random.choice(fechas)
    producto, categoria = random.choice(productos)
    
    # Introducir errores nulos aleatorios
    cantidad = random.randint(1, 20) if random.random() > 0.05 else None
    precio = round(random.uniform(0.5, 1500), 2) if random.random() > 0.05 else None
    
    # Espacios extra y mayúsculas/minúsculas inconsistentes
    producto = f" {producto.upper() if random.random() < 0.5 else producto.lower()} "
    categoria = f"{categoria.lower() if random.random() < 0.5 else categoria.upper()} "
    
    # Fecha nula aleatoria
    if random.random() < 0.05:
        fecha = None
    
    data.append([fecha, producto, categoria, cantidad, precio])

# Crear DataFrame y agregar duplicados intencionales
df = pd.DataFrame(data, columns=["Fecha", "Producto", "Categoría", "Cantidad", "Precio"])
df = pd.concat([df, df.sample(5, random_state=42)], ignore_index=True)  # 5 duplicados

# Guardar dataset original profesional
df.to_csv("ventas.csv", index=False)
print("Archivo 'ventas.csv' generado con 100 filas de ventas profesionales.")

# -------------------------------
# 2. Limpieza de dataset
# -------------------------------
# 2a. Eliminar duplicados
df = df.drop_duplicates()

# 2b. Manejar valores nulos
numericas = ['Cantidad', 'Precio']
for col in numericas:
    if col in df.columns:
        df[col] = df[col].fillna(0)

clave = ['Fecha', 'Producto']
df = df.dropna(subset=clave)

# 2c. Convertir columna "Fecha" a datetime
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df = df.dropna(subset=['Fecha'])

# 2d. Normalizar texto
texto_cols = ['Producto', 'Categoría']
for col in texto_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.lower()

# 2e. Crear columna Total_Venta
df['Total_Venta'] = df['Cantidad'] * df['Precio']

# -------------------------------
# 3. Guardar dataset limpio listo para Power BI
# -------------------------------
df.to_csv("ventas_limpias.csv", index=False)
print("Archivo 'ventas_limpias.csv' generado correctamente y listo para Power BI.")

# -------------------------------
# 4. Mostrar un vistazo al dataset limpio
# -------------------------------
print("\n--- Primeras 10 filas del dataset limpio ---")
print(df.head(10))
