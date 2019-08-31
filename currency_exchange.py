from flask import Flask, render_template, request
import requests

# App configuration
DEBUG = True
app = Flask(__name__, template_folder='templates')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # Not working here -- these form requests return 'NONETYPE' 
        # initial_value = float(request.form['initial_value'])
        initial_value = (request.values.get('initial_value'))
        print(initial_value) 
        # currency_base = request.form['currency_base']
        currency_base = (request.values.get('currency_base'))
        # currency_convert = request.form['currency_convert']
        currency_convert = (request.values.get('currency_convert'))

        r = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(currency_base))
        
        data = r.json() 
        
        conversion = (initial_value) * data['rates'][currency_convert]

        return render_template('conversion.html', conversion=conversion)
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run()