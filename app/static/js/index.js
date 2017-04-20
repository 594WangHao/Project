$(function() {
    var login_title = $("#login_title");
    var register_title = $("#register_title");
    var loginFrom = $("#login");
    var registerForm = $("#register");

    login_title.click(function(event) {
        console.log(1)
        loginFrom.removeClass('hide');
        registerForm.addClass('hide');
        register_title.removeClass('light-blue-text text-darken-4');
        login_title.addClass('light-blue-text text-darken-4');
    })

    register_title.click(function(event) {
        console.log(2)
        loginFrom.addClass('hide');
        registerForm.removeClass('hide');
        login_title.removeClass('light-blue-text text-darken-4');
        register_title.addClass('light-blue-text text-darken-4');
    })

    loginFrom.submit(function(event) {
        event.preventDefault()
        _this = $(this)
            // formData = new FormData(loginFrom[0])
        $.post('/api/login/', _this.serialize()).then(REST_response).then(function(data) {
            window.location.reload();
        })
    });

    registerForm.submit(function(event) {
        event.preventDefault()
        _this = $(this)
        $.post('/api/register/', _this.serialize()).then(REST_response).then(function(data) {
            window.location.href = '/'
        })
    });
})

function REST_response(response) {

    if (response.code !== 100) {
        alert(response.message)
        throw new Error(response.message)
    } else {
        return response.data
    }
}