import numpy as np
from keras.models import load_model


class BadDataInstance(Exception):
    pass


class BadDataShape(Exception):
    pass


parameter_names = {
    'Соотношение матрица-наполнитель': 'matrix_litter_ratio',
    'Плотность, кг/м3': 'density_kg/m3',
    'модуль упругости, ГПа': 'elasticity_modulus_GPa',
    'Количество отвердителя, м.%': 'hardener_quantity_m%',
    'Содержание эпоксидных групп,%_2': 'epoxy_group_amount_%',
    'Температура вспышки, С_2': 'flash_T_С_2',
    'Поверхностная плотность, г/м2': 'surface_density_g/m2',
    'Модуль упругости при растяжении, ГПа': 'mod_of_elast_under_tension_GPa',
    'Прочность при растяжении, МПа': 'strength_under_tension_MPa',
    'Потребление смолы, г/м2': 'resin_consumption_g/m2',
    'Угол нашивки, град': 'patch_angle_degree',
    'Шаг нашивки': 'patch_step',
    'Плотность нашивки': 'patch_density'
}


def predict_matrix(data_to_predict):
    if not isinstance(data_to_predict, list):
        raise BadDataInstance('Data must be a list!')

    if np.shape(data_to_predict) != (1, 12):
        raise BadDataShape('Data must contain 12 parameters in list!')

    model = load_model('keras_models/analyse_composite')
    return model.predict(data_to_predict)
