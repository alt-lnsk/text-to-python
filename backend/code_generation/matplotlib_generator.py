def generate_matplotlib_code(parsed_intent, df):
    """
    Génère du code matplotlib basé sur l'intention analysée de l'utilisateur.
    
    Args:
    parsed_intent (dict): L'intention analysée de l'utilisateur.
    df (pd.DataFrame): Le DataFrame pandas contenant les données.
    
    Returns:
    str: Le code matplotlib généré.
    """
    code = "import matplotlib.pyplot as plt\n\n"
    
    if not parsed_intent['columns']:
        return "# Veuillez spécifier au moins une colonne pour le graphique\n"
    
    x_column = parsed_intent['columns'][0]
    y_column = parsed_intent['columns'][1] if len(parsed_intent['columns']) > 1 else parsed_intent['columns'][0]
    
    code += f"x = df['{x_column}']\n"
    code += f"y = df['{y_column}']\n\n"
    
    if parsed_intent['graph_type'] == 'line':
        code += "plt.figure(figsize=(10, 6))\n"
        code += "plt.plot(x, y)\n"
        code += f"plt.xlabel('{x_column}')\n"
        code += f"plt.ylabel('{y_column}')\n"
        code += f"plt.title('Graphique en ligne de {y_column} en fonction de {x_column}')\n"
    elif parsed_intent['graph_type'] == 'bar':
        code += "plt.figure(figsize=(10, 6))\n"
        code += "plt.bar(x, y)\n"
        code += f"plt.xlabel('{x_column}')\n"
        code += f"plt.ylabel('{y_column}')\n"
        code += f"plt.title('Graphique en barres de {y_column} en fonction de {x_column}')\n"
    elif parsed_intent['graph_type'] == 'scatter':
        code += "plt.figure(figsize=(10, 6))\n"
        code += "plt.scatter(x, y)\n"
        code += f"plt.xlabel('{x_column}')\n"
        code += f"plt.ylabel('{y_column}')\n"
        code += f"plt.title('Nuage de points de {y_column} en fonction de {x_column}')\n"
    elif parsed_intent['graph_type'] == 'pie':
        code += "plt.figure(figsize=(10, 6))\n"
        code += "plt.pie(y, labels=x, autopct='%1.1f%%')\n"
        code += f"plt.title('Diagramme circulaire de {y_column}')\n"
    else:
        code += "# Type de graphique non reconnu\n"
    
    code += "plt.grid(True)\n"
    code += "plt.tight_layout()\n"
    code += "plt.show()\n"
    
    return code