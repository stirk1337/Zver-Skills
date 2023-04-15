function request(type, url, data){
    let returnData = ''
    $.ajax({
        type: type,
        url: url,
        data: data,
        success: function(data) { 
            if(type == 'GET'){
                returnData = data
            }
        },
        async: false
    })
    return returnData
}

getTasks()

function getTasks() {
    let data = request('GET', '/test/get_tasks')
    let taskBlock = $('.tasks-list')
    data.forEach(element => {
        let task = $("<div class='task'></div>")
        task.append($("<p class='task-name'></p>").text(element.name))
        task.append($("<p class='task-module'></p>").text(element.skill))
        if(element.difficulty == 'Легкая'){
            task.append($("<p class='task-difficulty easy'></p>").text(element.difficulty))
        }
        else if(element.difficulty == 'Средняя'){
            task.append($("<p class='task-difficulty normal'></p>").text(element.difficulty))
        }
        else{
            task.append($("<p class='task-difficulty hard'></p>").text(element.difficulty))
        }
        if(element.result == 'false'){
            task.append($("<p class='task-is-done undone'></p>").text('Не решено'))
        }
        else{
            task.append($("<p class='task-is-done done'></p>").text('Решено'))
        }
        taskBlock.append(task) 
    });
}