import pandas as pd
def crear_dataframe():
    data = {
        "Nombre": ["Juan", "Ana", "Luis"],
        "Edad": [25, 30, 28]
    }
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    crear_dataframe()
    