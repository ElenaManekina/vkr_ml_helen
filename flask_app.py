import sys
from flask import Flask, request, render_template
from predict import parameter_names, predict_matrix

app = Flask('web application')


@app.get('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        parameters = {}

        for key, value in request.form.items():
            try:
                parameter_value = float(value)
                if parameter_value < 0.0 or parameter_value > 1.0:
                    raise ValueError('Out of range!')
                parameters[key] = parameter_value

            except ValueError:
                return render_template('parameter_error.html', title=key, value=value)

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
        return render_template('predict_result.html', result=predicted_value[0][0])

    else:
        # Соотношение матрица-наполнитель - выходной параметер, пропускаем
        if 'Соотношение матрица-наполнитель' in parameter_names:
            parameter_names.pop('Соотношение матрица-наполнитель')

        template_data = []

        for key, value in parameter_names.items():
            template_data.append({
                'id': value,
                'title': key,
                'default_value': 0.0,
            })
        return render_template('predict_form.html', parameters=template_data)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        host = sys.argv[1]
    else:
        host = 'localhost'

    if len(sys.argv) >= 3:
        port = int(sys.argv[2])
    else:
        port = 5000

    app.run(host=host, port=port)
