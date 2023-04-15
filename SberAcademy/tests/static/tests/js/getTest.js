let id = window.location.href.split('/')[5]
let testid = ''
let type = window.location.href.split('/')[3]

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

let test = ''
let answers = []
getTest(id)

function getTest(id){
    console.log(type)
    if(type == 'vacancy'){
        test = request('GET', '/vacancy/test_vac', {vacancy_id: id})
        testid = test.id
    }
    else{
        test = request('GET', '/test/get_test', {test_id: id})
    }
    console.log(test)
    $('.open-test-name').text('Тест на ' + test.name)
    $('.open-test-description').text(test.description)
    $('.open-test-answers p').text(test.questions.length + ' вопросов')
}

function SetAnswers(num){
    let questions = test.questions
    $('.question').text(questions[num].question)
    $('.variants p:nth-child(1)').text(questions[num].opt1)
    $('.variants p:nth-child(2)').text(questions[num].opt2)
    $('.variants p:nth-child(3)').text(questions[num].opt3)
    $('.variants p:nth-child(4)').text(questions[num].opt4)
}

$(document).on('click', '.start-test', function(e){
    console.log(test)
    $('.open-test-container').addClass('hidden')
    $('.test-field').removeClass('hidden')
    $('.submit-test').removeClass('hidden')
    let questions = test.questions
    SetAnswers(0)
    let select = $('.question-select')
    for (let index = 0; index < questions.length; index++) {
        let num = $("<div></div>").text(index + 1)
        if(index + 1 == 1){
            num.attr('class', 'active')
        }
        answers.push(['0', '0'])
        select.append(num)
    }
})

$(document).on('click', '.question-select div', function(e){
    let number = e.currentTarget.innerText
    if(e.currentTarget.classList.contains('task-choiced')){
        $('.choiced').removeClass('choiced')
        let answer = answers[parseInt(number) - 1]
        $('.variants #' + answer[0]).addClass('choiced')
    }
    else{
        $('.choiced').removeClass('choiced')
    }
    SetAnswers(number - 1)
    $('.active').removeClass('active')
    $('.question-select div:nth-child(' + number + ')').addClass('active')
})

$(document).on('click', '.variants p', function(e){

    let answer = e.currentTarget.innerText

    answers[parseInt($('.active').text()) - 1] = [e.currentTarget.id, answer]
    $('.choiced').removeClass('choiced')
    console.log(e)
    e.currentTarget.classList.add('choiced')
    $('.active').addClass('task-choiced')
    console.log(answers)
})

$(document).on('click', '.submit-test', function(e){
    let sendArray = []
    answers.forEach(element => {
        sendArray.push(element[1])
    });
    console.log(sendArray)
    let mark = ''
    if(type == 'vacancy'){
        mark = request('GET', '/vacancy/complete_test', {test_id: testid, vacancy_id: id, answers: sendArray.join(',')})
        for(var key in mark){
            $('.mark').append($("<p></p>").text('Ваш балл ' + key + ': ' + mark[key]))
        }
        $('.mark').append($("<p></p>").text('Ваша анкета была отправлена'))
    }
    else{
        mark = request('GET', '/test/complete_test', {test_id: id, answers: sendArray.join(',')})
        $('.mark').text('Ваш балл: ' + mark)
    }
    $('.test-field').addClass('hidden')
    $('.submit-test').addClass('hidden')
})




