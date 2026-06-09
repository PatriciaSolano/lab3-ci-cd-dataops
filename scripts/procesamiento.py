import pandas as pd

print("INICIO DEL PROCESO")

df = pd.read_csv('data/dataset.csv')

print("\nDataset original:")
print(df)

df = df.fillna(0)

print("\nDataset limpio:")
print(df)

df.to_csv('output/dataset_limpio.csv', index=False)

print("\nArchivo exportado correctamente")
print("FIN DEL PROCESO")