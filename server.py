from flask import Flask, render_template 
app = Flask(__name__)                     
    
@app.route('/play')                           
def play_one():
    return render_template("index.html",num=3, color="blue")  

@app.route('/play/<int:num>')
def play_two(num):
    return render_template("index.html",num=num, color="blue")

@app.route('/play/<int:num>/<string:color>')
def play_three(num,color):
    return render_template("index.html",num=num, color=color)
    
if __name__=="__main__":
    app.run(debug=True)


#     Create a new Flask project

# Have the /play route render a template with 3 blue boxes

# Have the /play/<x> route render a template with x number of blue boxes

# Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value

# NINJA BONUS: Use only one template for the whole project