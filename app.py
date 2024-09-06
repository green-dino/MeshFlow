from flask import Flask

app = Flask(__name__)

# Step 3: Define Routes
@app.route('/')
def home():
    return "Welcome to MeshFlow!"

@app.route('/about')
def about():
    return "About MeshFlow"

# Step 4: Run the App
if __name__ == "__main__":
    app.run(debug=True)