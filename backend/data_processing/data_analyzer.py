import pandas as pd
import numpy as np

def analyze_data(df):
    """
    Effectue une analyse de base sur les données du DataFrame.
    
    Args:
    df (pd.DataFrame): Le DataFrame à analyser.
    
    Returns:
    dict: Un dictionnaire contenant les résultats de l'analyse.
    """
    analysis = {}
    
    # Informations générales
    analysis['shape'] = df.shape
    analysis['columns'] = df.columns.tolist()
    
    # Statistiques descriptives
    analysis['description'] = df.describe().to_dict()
    
    # Types de données
    analysis['dtypes'] = df.dtypes.to_dict()
    
    # Valeurs manquantes
    analysis['missing_values'] = df.isnull().sum().to_dict()
    
    # Corrélations (pour les colonnes numériques)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        analysis['correlations'] = df[numeric_cols].corr().to_dict()
    
    return analysis