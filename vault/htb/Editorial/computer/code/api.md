```python
# API (in development).
# * To retrieve info about editorial

import json
from flask import Flask, jsonify

# -------------------------------
# App configuration
# -------------------------------
app = Flask(__name__)

# -------------------------------
# Global Variables
# -------------------------------
api_route = "/api/latest/metadata"
api_editorial_name = "Editorial Tiempo Arriba"
api_editorial_email = "info@tiempoarriba.htb"

# -------------------------------
# API routes
# -------------------------------
# -- : home
@app.route('/api', methods=['GET'])
def index():
    data_editorial = {
        'version': [{
            '1': {
                'editorial': 'Editorial El Tiempo Por Arriba', 
                'contact_email_1': 'soporte@tiempoarriba.oc',
                'contact_email_2': 'info@tiempoarriba.oc',
                'api_route': '/api/v1/metadata/'
            }},
            {
            '1.1': {
                'editorial': 'Ed Tiempo Arriba', 
                'contact_email_1': 'soporte@tiempoarriba.oc',
                'contact_email_2': 'info@tiempoarriba.oc',
                'api_route': '/api/v1.1/metadata/'
            }},
            {
            '1.2': {
                'editorial': api_editorial_name, 
                'contact_email_1': 'soporte@tiempoarriba.oc',
                'contact_email_2': 'info@tiempoarriba.oc',
                'api_route': f'/api/v1.2/metadata/'
            }},
            {
            '2': {
                'editorial': api_editorial_name, 
                'contact_email': 'info@tiempoarriba.moc.oc',
                'api_route': f'/api/v2/metadata/'
            }},
            {
            '2.3': {
                'editorial': api_editorial_name, 
                'contact_email': api_editorial_email,
                'api_route': f'{api_route}/'
            }
        }]
    }
    return jsonify(data_editorial)

# -- : (development) mail message to new authors
@app.route(api_route + '/authors/message', methods=['GET'])
def api_mail_new_authors():
    return jsonify({
        'template_mail_message': "Welcome to the team! We are thrilled to have you on board and can't wait to see the incredible content you'll bring to the table.\n\nYour login credentials for our internal forum and authors site are:\nUsername: dev\nPassword: dev080217_devAPI!@\nPlease be sure to change your password as soon as possible for security purposes.\n\nDon't hesitate to reach out if you have any questions or ideas - we're always here to support you.\n\nBest regards, " + api_editorial_name + " Team."
    }) # TODO: replace dev credentials when checks pass

# -------------------------------
# Start program
# -------------------------------
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)

```

Nothing that we do not know already