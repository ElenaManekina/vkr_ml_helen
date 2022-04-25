from predict import parameter_names, predict_matrix


def input_parameters(parameter_names):
    result = {}

    # Соотношение матрица-наполнитель - выходной параметер, пропускаем
    parameter_names.pop('Соотношение матрица-наполнитель')

    for key, value in parameter_names.items():
        while True:
            text_value = input(
                f'Введите значение параметра "{key}": '
            )
            try:
                parameter_value = float(text_value)
                if parameter_value < 0.0 or parameter_value > 1.0:
                    raise ValueError('Out of range!')
                result[value] = parameter_value
                break

            except ValueError:
                print(
                    f'\tВведено недопустимое значение "{text_value}"!'
                )
    return result


if __name__ == '__main__':
    try:
        print('\n\n'
              'Выпускная квалификационная работа (Манекина Елена)'
              'Прогнозирование выходного параметра "Соотношение матрица-наполнитель"\n'
              )
        parameters = input_parameters(parameter_names)
        predicted_value = predict_matrix([[
            parameters['density_kg/m3'],
            parameters['elasticity_modulus_GPa'],
            parameters['hardener_quantity_m%'],
            parameters['epoxy_group_amount_%'],
            parameters['flash_T_С_2'],
            parameters['surface_density_g/m2'],
            parameters['mod_of_elast_under_tension_GPa'],
            parameters['strength_under_tension_MPa'],
            parameters['resin_consumption_g/m2'],
            parameters['patch_angle_degree'],
            parameters['patch_step'],
            parameters['patch_density']
        ]])
        print(
            '\n\n'
            f'Соотношение матрица-наполнитель: {predicted_value[0][0]}'
        )

    except KeyboardInterrupt:
        print('\n\n'
              '\tВыполнение программы прeрвано пользователем.\n'
              '\tДо свидания!\n')
