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

let id = window.location.href.split('/')[5]

GetProfile()

function GetProfile(){
    let data = request('GET', '/user/get_user_profile', {user_id: id})
    console.log(data)
    $('.group').text(data.group)
    $('.login').text(data.login)
    $('.fio').text(data.name)
    $('.number').text(data.contacts)
    $('.description').text(data.description)
}