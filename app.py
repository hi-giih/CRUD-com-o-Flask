from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

#Post
@app.route('/tasks', methods=["POST"])

def create_tasks():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ""))
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso"})

#GET
#Todas as tarefas
@app.route('/tasks', methods=["GET"])

def get_tasks():
    task_lists = [ task.to_dict() for task in tasks]
    
    output = {
            "tasks": task_lists,
            "total_tasks":len(task_lists)
            }
    return jsonify(output)

#Apenas uma atividade
@app.route('/tasks/<int:id>', methods=["GET"])

def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possivel encontrar a tarefa"}), 404

#PUT
@app.route('/tasks/<int:id>', methods=["PUT"])

def update_task(id):
    task = None
    print(task)
    for t in tasks:
        if t.id == id:
            task=t
            break

    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a tarefa"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    return jsonify({"message": "Tarefa atualizada com sucesso"})
        
    print(task)

#DELETE
@app.route('/tasks/<int:id>', methods=["DELETE"])

def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
        
    if not task:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__=='__main__':
    app.run()