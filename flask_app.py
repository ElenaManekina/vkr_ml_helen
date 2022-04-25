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
        predicted_value = predict_matrix([[
            float(request.form['density_kg/m3']),
            float(request.form['elasticity_modulus_GPa']),
            float(request.form['hardener_quantity_m%']),
            float(request.form['epoxy_group_amount_%']),
            float(request.form['flash_T_С_2']),
            float(request.form['surface_density_g/m2']),
            float(request.form['mod_of_elast_under_tension_GPa']),
            float(request.form['strength_under_tension_MPa']),
            float(request.form['resin_consumption_g/m2']),
            float(request.form['patch_angle_degree']),
            float(request.form['patch_step']),
            float(request.form['patch_density'])
        ]])
        return render_template('predict_result.html', result=predicted_value[0][0])

    else:
        # Соотношение матрица-наполнитель - выходной параметер, пропускаем
        if 'Соотношение матрица-наполнитель' in parameter_names:
            parameter_names.pop('Соотношение матрица-наполнитель')

        parameters = []

        for key, value in parameter_names.items():
            parameters.append({
                'id': value,
                'title': key,
                'default_value': 0.0,
            })
        return render_template('predict_form.html', parameters=parameters)


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
