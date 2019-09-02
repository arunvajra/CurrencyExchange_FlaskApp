from flask import Flask, render_template, request
import requests

# App configuration
DEBUG = True
app = Flask(__name__, template_folder='templates')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
       
        initial_value = int(request.values.get('initial_value'))
        print(initial_value) 
        
        currency_base = (request.values.get('currency_base')).upper()
        print(currency_base)
        
        currency_convert = (request.values.get('currency_convert')).upper()
        print(currency_convert)

        r = requests.get('https://api.exchangeratesapi.io/latest?base={}'.format(currency_base))
     
        data = r.json() 
        print(initial_value)
        print(data['rates'][currency_convert])
        
        
        conversion = (initial_value) * data['rates'][currency_convert]

        return render_template('conversion.html', initial_value=initial_value, currency_base=currency_base, conversion=conversion, currency_convert=currency_convert)
    
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()