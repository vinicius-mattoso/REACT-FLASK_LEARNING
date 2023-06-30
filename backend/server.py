# Import flask and datetime module for showing date and time
from flask import Flask, render_template
import datetime
 
x = datetime.datetime.now()

print(x)
 
# Initializing flask app
app = Flask(__name__)
 
# Route Base
@app.route('/')
def index():
    return render_template('index.html')
 
# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek",
        "Age":"22",
        "Date":x,
        "programming":"python"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run(debug=True)