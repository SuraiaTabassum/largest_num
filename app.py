from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Find N-th Largest Number</h2>
        <form action="/nth-largest" method="post">
            Numbers (comma-separated): <input type="text" name="numbers"><br>
            N: <input type="number" name="n"><br>
            <input type="submit" value="Find">
        </form>
    '''

@app.route('/nth-largest', methods=['POST'])
def nth_largest():
    try:
        numbers_str = request.form['numbers']
        n = int(request.form['n'])
        numbers = [int(x.strip()) for x in numbers_str.split(',')]
        numbers.sort(reverse=True)

        if n <= 0 or n > len(numbers):
            return f"<p>Error: N must be between 1 and {len(numbers)}</p>"

        return f"<h3>The {n}-th largest number is: {numbers[n-1]}</h3>"
    except Exception as e:
        return f"<p>Error: {str(e)}</p>"

if __name__ == '__main__':
    app.run(debug=True)
