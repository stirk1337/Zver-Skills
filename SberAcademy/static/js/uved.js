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

getUved()

function getUved(){
    let name = $('.header-user p').text()
    data = ''
    if(name == 'rabota'){
        data = request('GET', 'vacancies/get_surveys')
    }
    console.log(data)
}