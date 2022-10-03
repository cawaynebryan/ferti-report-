from interpretation_tables import table_collections
import math


extracted = {'N': 1, 'P': 3, 'K': 141, 'Mg': 2.5, 'Cu': 3, 'EC': 23}


# #########################  Calculation of Limits  ####################################################################

def base_saturation_sar_cec(Al):  # Todo: check formulas
    sum_of_base = extracted['Ca'] + extracted['Mg'] + extracted['K'] + extracted['Na']
    sar = extracted['Na'] / (math.sqrt((1 / 2 * (extracted['Ca'] + extracted['Mg']))))
    cec = sum_of_base + Al
    base_saturation = ((extracted['Ca'] + extracted['Mg'] + extracted['K'] + extracted['Na']) / cec)
    return base_saturation


def electrical_conductivity(ec):
    return ec <= table_collections.almd['limits']['EC']['Max']


def sodium(na):
    return na <= table_collections.almd['limits']['Na']['Max']


# #########################  Calculation of Range  ####################################################################

def ph(pH):
    return pH <= table_collections.almd['range']['pH']['Max']


def organic_carbon(oc):
    return table_collections.almd['range']['OH']['min'] <= \
           oc <= table_collections.almd['range']['OH']['max']


def cation_exchange_capacity(cec):
    return table_collections.almd['range']['CEC']['min'] <= \
           cec <= table_collections.almd['range']['CEC']['max']


def organic_matter(om):
    return table_collections.almd['range']['OH']['min'] <= \
            om <= table_collections.almd['range']['OH']['max']



