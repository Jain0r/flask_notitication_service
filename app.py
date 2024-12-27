from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/notify', methods=['POST'])
def notify():
    try:
        data = request.get_json()
        
        # Validar que estén todos los campos requeridos
        if not all(key in data for key in ['email', 'message']):
            return jsonify({
                'error': 'Campos requeridos faltantes. Se necesita email y message'
            }), 400
            
        # Simular el envío de correo imprimiendo en consola
        print("\n=== Nuevo Email Enviado ===")
        print(f"Timestamp: {datetime.now().isoformat()}")
        print(f"Para: {data['email']}")
        print(f"Mensaje: {data['message']}")
        print("========================\n")
        
        return jsonify({
            'status': 'success',
            'message': 'Notificación enviada exitosamente',
            'timestamp': datetime.now().isoformat(),
            'details': {
                'email': data['email'],
                'message': data['message']
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Error al procesar la solicitud',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    # Usar un puerto diferente al de la API principal
    app.run(port=5001, debug=True)