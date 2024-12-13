import http.server
import socketserver
import os

PORT = 8000

# HTML, CSS, and JavaScript for the calculator interface
calculator_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            text-align: center;
            padding: 50px;
        }
        .calculator {
            display: inline-block;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .display {
            width: 100%;
            padding: 10px;
            font-size: 1.5em;
            text-align: right;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
        }
        button {
            padding: 15px;
            font-size: 1.2em;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <input type="text" id="display" class="display" disabled>
        <div class="buttons">
            <button onclick="press('7')">7</button>
            <button onclick="press('8')">8</button>
            <button onclick="press('9')">9</button>
            <button onclick="press('/')">/</button>
            <button onclick="press('4')">4</button>
            <button onclick="press('5')">5</button>
            <button onclick="press('6')">6</button>
            <button onclick="press('*')">*</button>
            <button onclick="press('1')">1</button>
            <button onclick="press('2')">2</button>
            <button onclick="press('3')">3</button>
            <button onclick="press('-')">-</button>
            <button onclick="press('0')">0</button>
            <button onclick="press('.')">.</button>
            <button onclick="calculate()">=</button>
            <button onclick="press('+')">+</button>
            <button onclick="clearDisplay()" style="grid-column: span 4; background-color: #dc3545;">Clear</button>
        </div>
    </div>
    <script>
        let display = document.getElementById('display');

        function press(value) {
            display.value += value;
        }

        function calculate() {
            try {
                display.value = eval(display.value);
            } catch (e) {
                alert('Invalid Expression');
                clearDisplay();
            }
        }

        function clearDisplay() {
            display.value = '';
        }
    </script>
</body>
</html>
"""

class CalculatorHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(calculator_html.encode("utf-8"))
        else:
            self.send_error(404, "File Not Found")

# Run the server
with socketserver.TCPServer(("", PORT), CalculatorHandler) as httpd:
    print(f"Serving on port {PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()
