import pandas as pd

def read_excel_file(file):
    """
    Lit un fichier Excel et retourne un DataFrame pandas.
    
    Args:
    file: Un objet FileStorage de Flask représentant le fichier Excel uploadé.
    
    Returns:
    Un DataFrame pandas contenant les données du fichier Excel.
    """
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Excel: {str(e)}")
        return None