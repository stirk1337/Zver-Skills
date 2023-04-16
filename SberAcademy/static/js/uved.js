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

$(document).on('click', '.header-user p', function(e){
    let name = $('.header-user p').text()
    let data = ''
    $('.uved-container').removeClass('hidden')
    if(name == 'rabota'){
        data = request('GET', '/user/get_surveys')
        let uvedContainer = $('.uved-container')
        data.forEach(element => {
            let uved = $("<div class='uved'></div>")
            uved.attr('id', element.id)
            uved.append($("<p class='uved-name'></p>").text(element.name))
            let decision = $("<div class='decision'></div>")
            decision.append($("<p class='easy'></p>").text('Принять'))
            decision.append($("<p class='hard'></p>").text('Отклонить'))
            uved.append(decision)
            if(name == 'rabota'){
                uved.append($("<p class='normal'></p>").text('Посоветовать ментора'))
            }
            uvedContainer.append(uved)
        });
    }
    else{
        data = request('GET', '/user/get_notifications')
        data.forEach(element => {
            let uvedContainer = $('.uved-container')
            let uved = $("<div class='uved'></div>")
            let hyper = $("<a class='message'></a>").text(element.message)
            hyper.attr('href', '/user/profile/' + element.second_user_id)
            uved.append(hyper)
            uvedContainer.append(uved)
        });
    }
    console.log(data)
})

$(document).on('click', '.uved .easy', function(e){
    let id = e.currentTarget.parentElement.parentElement.id
    request('GET', '/user/accept_survey', {survey_id: id})
    e.currentTarget.parentElement.parentElement.remove()
})

$(document).on('click', '.uved .hard', function(e){
    let id = e.currentTarget.parentElement.parentElement.id
    request('GET', '/user/delete_survey', {survey_id: id})
    e.currentTarget.parentElement.parentElement.remove()
})

$(document).on('click', '.uved .normal', function(e){
    let id = e.currentTarget.parentElement.id
    request('GET', '/user/mentor_survey', {survey_id: id})
    e.currentTarget.parentElement.remove()
})