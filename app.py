from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Rinay's Flask App!"

# Example route with query parameter
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'failed'
    })

# Health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

