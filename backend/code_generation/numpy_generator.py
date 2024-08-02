def generate_numpy_code(parsed_intent, df):
    """
    Génère du code numpy basé sur l'intention analysée de l'utilisateur.
    
    Args:
    parsed_intent (dict): L'intention analysée de l'utilisateur.
    df (pd.DataFrame): Le DataFrame pandas contenant les données.
    
    Returns:
    str: Le code numpy généré.
    """
    code = "import numpy as np\n\n"
    
    if not parsed_intent['columns']:
        return "# Veuillez spécifier au moins une colonne pour l'opération\n"
    
    column = parsed_intent['columns'][0]
    
    code += f"# Conversion de la colonne en array NumPy\n"
    code += f"arr = df['{column}'].to_numpy()\n\n"
    
    if parsed_intent['operation'] == 'mean':
        code += f"result = np.mean(arr)\n"
        code += f"print(f'La moyenne de {column} est: {{result}}')\n"
    elif parsed_intent['operation'] == 'sum':
        code += f"result = np.sum(arr)\n"
        code += f"print(f'La somme de {column} est: {{result}}')\n"
    elif parsed_intent['operation'] == 'max':
        code += f"result = np.max(arr)\n"
        code += f"print(f'Le maximum de {column} est: {{result}}')\n"
    elif parsed_intent['operation'] == 'min':
        code += f"result = np.min(arr)\n"
        code += f"print(f'Le minimum de {column} est: {{result}}')\n"
    else:
        code += "# Opération non reconnue\n"
    
    return code