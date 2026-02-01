import pandas as pd
import os

def criar_pastas():
    # Pastas limpas, sem números
    for pasta in ['data/bronze', 'data/silver', 'data/gold']:
        if not os.path.exists(pasta):
            os.makedirs(pasta)

def processar_dados():
    # Caminho direto para a pasta bronze
    caminho_bronze = 'data/bronze/remedios_brutos.csv'
    
    if not os.path.exists(caminho_bronze):
        print(f"ERRO: O arquivo não está em: {caminho_bronze}")
        return

    df = pd.read_csv(caminho_bronze)
    df['medicamento'] = df['medicamento'].str.upper().str.strip()
    
    # Salvando nas pastas simples
    df.to_csv('data/silver/remedios_limpos.csv', index=False)
    df.to_csv('data/gold/base_consulta.csv', index=False)
    print("Sucesso! Tudo organizado em bronze, silver e gold.")

if __name__ == "__main__":
    criar_pastas()
    processar_dados()