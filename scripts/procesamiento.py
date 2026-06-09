import pandas as pd

print("🔵 INICIO DEL PROCESO")

df = pd.read_csv('data/dataset.csv')

print("\n📌 Dataset original:")
print(df)

df = df.fillna(0)

print("\n🧹 Dataset limpio:")
print(df)

df.to_csv('output/dataset_limpio.csv', index=False)

print("\n✅ Archivo exportado correctamente")
print("🔵 FIN DEL PROCESO")