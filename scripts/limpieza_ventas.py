import pandas as pd

# -------------------------------
# 1. Cargar el archivo CSV
# -------------------------------
df = pd.read_csv("ventas.csv")

# -------------------------------
# 2. Eliminar duplicados
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# 3. Manejo de valores nulos
# -------------------------------

# Rellenar con 0 en columnas numéricas
numericas = ['Cantidad', 'Precio']
for col in numericas:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# Eliminar filas vacías en columnas clave
clave = ['Fecha', 'Producto']
df = df.dropna(subset=clave)

# -------------------------------
# 4. Convertir columna "Fecha" al tipo datetime
# -------------------------------
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')  # convierte errores a NaT
df = df.dropna(subset=['Fecha'])  # elimina filas donde la fecha no pudo convertirse

# -------------------------------
# 5. Normalizar texto en columnas de producto y categoría
# -------------------------------
texto_cols = ['Producto', 'Categoría']
for col in texto_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.lower()  # elimina espacios y pasa a minúsculas

# -------------------------------
# 6. Crear columna "Total_Venta"
# -------------------------------
df['Total_Venta'] = df['Cantidad'] * df['Precio']

# -------------------------------
# 7. Guardar el resultado limpio
# -------------------------------
df.to_csv("ventas_limpias.csv", index=False)  # listo para Power BI
print("Archivo 'ventas_limpias.csv' generado correctamente.")
