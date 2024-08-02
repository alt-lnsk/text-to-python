import re

def parse_intent(intent):
    """
    Analyse l'intention de l'utilisateur et extrait les informations pertinentes.
    
    Args:
    intent (str): La description en langage naturel de ce que l'utilisateur veut faire.
    
    Returns:
    dict: Un dictionnaire contenant les informations extraites de l'intention.
    """
    intent = intent.lower()
    parsed = {
        'library': None,
        'operation': None,
        'columns': [],
        'graph_type': None
    }
    
    # Déterminer la bibliothèque
    if 'pandas' in intent or 'dataframe' in intent:
        parsed['library'] = 'pandas'
    elif 'matplotlib' in intent or 'plot' in intent or 'graph' in intent:
        parsed['library'] = 'matplotlib'
    elif 'numpy' in intent or 'array' in intent:
        parsed['library'] = 'numpy'
    
    # Extraire les colonnes mentionnées
    columns = re.findall(r'\b(colonne|column)\s+(\w+)', intent)
    parsed['columns'] = [col[1] for col in columns]
    
    # Déterminer l'opération ou le type de graphique
    if parsed['library'] == 'pandas':
        if 'moyenne' in intent or 'mean' in intent:
            parsed['operation'] = 'mean'
        elif 'somme' in intent or 'sum' in intent:
            parsed['operation'] = 'sum'
        elif 'trier' in intent or 'sort' in intent:
            parsed['operation'] = 'sort'
    elif parsed['library'] == 'matplotlib':
        if 'ligne' in intent or 'line' in intent:
            parsed['graph_type'] = 'line'
        elif 'barre' in intent or 'bar' in intent:
            parsed['graph_type'] = 'bar'
        elif 'scatter' in intent or 'dispersion' in intent:
            parsed['graph_type'] = 'scatter'
        elif 'camembert' in intent or 'pie' in intent:
            parsed['graph_type'] = 'pie'
    elif parsed['library'] == 'numpy':
        if 'moyenne' in intent or 'mean' in intent:
            parsed['operation'] = 'mean'
        elif 'somme' in intent or 'sum' in intent:
            parsed['operation'] = 'sum'
        elif 'maximum' in intent or 'max' in intent:
            parsed['operation'] = 'max'
        elif 'minimum' in intent or 'min' in intent:
            parsed['operation'] = 'min'
    
    return parsed