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

getTests()

function getTests() {
    let data = request('GET', '/test/get_tests')
    console.log(data)
    let testContainer = $('.test-cards')
    let threeContainer = ''
    for (let index = 0; index < data.length; index++) {
        let test = $("<div class='test'></div>")
        test.attr('id', data[index].id)
        test.attr('href', '/test/' + data[index].id)
        test.append($("<p class='test-name'></p>").text(data[index].name))
        test.append($("<p class='test-description'></p>").text(data[index].description))
        if(index % 3 == 0){
            threeContainer = $("<div class='container-three'></div>")
            threeContainer.append(test)
            testContainer.append(threeContainer)
        }
        else{
            threeContainer.append(test)
        }
        if(index + 1 == data.length && index + 1 % 3 != 0){
            testContainer.append(threeContainer)
        }
    }
}

$(document).on('click', '.test', function(e){
    window.location.replace('test/' + e.currentTarget.id)
})