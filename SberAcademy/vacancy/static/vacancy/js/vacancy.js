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

GetVacancies()

function GetVacancies(){
    let vacancies = request('GET', '/vacancy/get_vacancies')
    console.log(vacancies)
    let vacblock = $('.vacancy-blok')
    vacancies.forEach(element => {
        let vacancy = $("<div class='vacancy'></div>")
        let header = $("<div class='vacancy-name'></div>")
        header.append($("<p></p>").text(element.name))
        header.append($("<img class='vacancy-logo' src='/static/img/vacancy-logo.svg'>"))
        vacancy.append(header)
        let body = $("<div class='vacancy-body'></div>")
        let description = $("<div class='vacancy-description'></div>")
        let flex = $("<div class='vacancy-flex'></div>")
        let place = $("<div class='vacancy-place'></div>")
        place.append($("<p class='company'></p>").text(element.company))
        place.append($("<p class='city'></p>").text(element.city))
        flex.append(place)
        let owner = $("<div class='vacancy-owner'></div>")
        owner.append($("<p></p>").text("Работодатель:"))
        owner.append($("<p></p>").text(element.employeer))
        flex.append(owner)
        description.append(flex)
        description.append($("<p class='description'></p>").text(element.description))
        body.append(description)
        let skills = $("<div class='skills'></div>")
        skills.append($("<p></p>").text('Навыки:'))
        element.skills.forEach(skill => {
            skills.append($("<p></p>").text(skill))
        });
        let img = $("<img class='more' src='/static/img/vacancy-test.svg'>")
        img.attr('id', element.id)
        skills.append(img)
        body.append(skills)
        vacancy.append(body)
        vacblock.append(vacancy)
    });
}

$(document).on('click', '.more', function(e){
    window.location.replace('/vacancy/test/' + e.currentTarget.id)
})