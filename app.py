from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# This matches your filenames: 1.png, 2.png, etc.
FRUITS = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
credits = 100 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin', methods=['POST'])
def spin():
    global credits
    if credits < 10:
        return jsonify({'error': 'Not enough credits!'}), 400

    credits -= 10
    result = [random.choice(FRUITS) for _ in range(3)]
    won = len(set(result)) == 1
    
    if won:
        credits += 50
        
    return jsonify({
        'result': result, 
        'won': won,
        'current_credits': credits
    })

if __name__ == '__main__':
    app.run(debug=True)