def generate_pandas_code(parsed_intent, df):
    """
    Génère du code pandas basé sur l'intention analysée de l'utilisateur.
    
    Args:
    parsed_intent (dict): L'intention analysée de l'utilisateur.
    df (pd.DataFrame): Le DataFrame pandas contenant les données.
    
    Returns:
    str: Le code pandas généré.
    """
    code = "import pandas as pd\n\n"
    code += "# Chargement des données\n"
    code += "df = pd.DataFrame(your_data)\n\n"
    
    if parsed_intent['operation'] == 'mean':
        if parsed_intent['columns']:
            columns = ", ".join(f"'{col}'" for col in parsed_intent['columns'])
            code += f"result = df[{columns}].mean()\n"
        else:
            code += "result = df.mean()\n"
    elif parsed_intent['operation'] == 'sum':
        if parsed_intent['columns']:
            columns = ", ".join(f"'{col}'" for col in parsed_intent['columns'])
            code += f"result = df[{columns}].sum()\n"
        else:
            code += "result = df.sum()\n"
    elif parsed_intent['operation'] == 'sort':
        if parsed_intent['columns']:
            column = parsed_intent['columns'][0]
            code += f"result = df.sort_values('{column}')\n"
        else:
            code += "# Veuillez spécifier une colonne pour le tri\n"
            code += "result = df\n"
    else:
        code += "# Opération non reconnue\n"
        code += "result = df\n"
    
    code += "\nprint(result)\n"
    return code