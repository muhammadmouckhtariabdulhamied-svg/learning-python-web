from flask import Flask, request, jsonify
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)
guess_count = 4
guess_limit = 4

@app.route('/guess', methods=['POST'])
def guess_number():
    global guess_count, secret_number
    data = request.get_json()
    guess = int(data['guess'])
    guess_count += 1

    if guess == secret_number:
        return jsonify({"result": "🎉 You won!"})
    elif guess_count >= guess_limit:
        return jsonify({"result": f"❌ Sorry, you failed! The number was {secret_number}"})
    elif guess < secret_number:
        return jsonify({"result": "Too low! Try again."})
    else:
        return jsonify({"result": "Too high! Try again."})

if __name__ == '__main__':
    app.run(debug=True)
