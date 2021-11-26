from flask import Flask, request

app = Flask(__name__)

@app.route('/query-example')
def query_example():
    #args is a dictonary. get() is a dict method.
    #The get() method returns the value of the item with the specified key.
    language = request.args.get('language')
    framework = request.args.get('framework') #request.args['framework'] not advised. might fail.
    return '<h1> The language value is: {} and the framework is {} </h1>.'.format(language, framework)

@app.route('/form-example', methods=["GET", "POST"])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1> The language value is {} </h1>
                  <h1> The framework value is {}</h1>'''.format(language, framework)
    
    return '''
              <form method="POST" style="text-align:center;">
                  <div><label>Language:<input type="text" name="language"></label> </div>
                  <br>
                  <div><label>Framework:<input type="text" name="framework"></label> </div>
                  <br>
                  <div><input type="submit" value="submit"></div>
              </form>'''

@app.route('/Json-example')
def json_example():
    return 'JSON Object Example'

if __name__ == "__main__":
    app.run(debug='True', port=5000)
