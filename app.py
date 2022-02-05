from flask import Flask, jsonify,request
app=Flask(__name__)
tasks=[{
    'id': 1, 'title': u'Buy groceries', 'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': False

}, { 'id': 2, 'title': u'Learn Python', 'description': u'Need to find a good Python tutorial on the web', 'done': False }]
@app.route("/")
def helloworld():
    return "hello world"
@app.route("/get-data")
def get_data():
    return jsonify({
        "data":tasks
    })
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":
            "please provide the data"
        })
    
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":
            "task added successfully"
        })
if(__name__=="__main__"):
    app.run()