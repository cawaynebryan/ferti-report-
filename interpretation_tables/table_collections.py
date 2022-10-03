almd = {           # TODO: add valency electron to the following for more accurate calculation
    'limits': {
        'EC': {'unit': 'mmhos/cm', 'max': 4},  # TODO: modify to range
        'Na': {'unit': 'mmhos/cm', 'max': 1}
    },
    'range': {
        'pH': {'unit': 'pH', 'min': 5.5, 'max': 7.3},
        'OC': {'unit': '%', 'min': 2, 'max': 5},
        'CEC': {'unit': 'Meg/100g soil', 'min': 15, 'max': 25},
        'OM': {'unit': '%', 'min': 4, 'max': 8}
    },
    'elements': {
        'N':  {'unit': 'ppm', 'mass': 14, 'min': 2, 'max': 5, 'es': 1},
        'P':  {'unit': 'ppm', 'mass': 31, 'min': 60, 'max': 100, 'es': 3},
        'K':  {'unit': 'ppm', 'mass': 39, 'min': 0.5, 'max': 1.5, 'es': 1},
        'Ca': {'unit': 'Meg/100g soil', 'mass': 40, 'min': 10, 'max': 10, 'es': 2},  # TODO: check value
        'Mg': {'unit': 'Meg/100g soil', 'mass': 24, 'min': 0.5, 'max': 1.5, 'es': 2},
        'Cu': {'unit': 'ppm', 'mass': 63, 'min': 2.0, 'max': 5.0, 'es': 2},
        'Mn': {'unit': 'ppm', 'mass': 54, 'min': 50, 'max': 100, 'es': 1},
        'Fe': {'unit': 'ppm', 'mass': 55, 'min': 60, 'max': 120, 'es': 2}
    }

}
