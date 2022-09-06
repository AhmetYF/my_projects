from flask import Flask

app = Flask(__name__) 

@app.route('/')
def hello ():
    return "Hello World!"

@app.route('/second')
def second():
    return "This is the second page"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"
        
#Create a dynamic url which takes id number dynamically and return with a massage which show id of page. 
@app.route('/<id>')
def dynamic_url(id):
    return ("This is the {} page".format(id))


if __name__ == '__main__':
    app.run(debug=True, port=4000)