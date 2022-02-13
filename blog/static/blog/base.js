// like-save
const BASE_URL = "http://127.0.0.1:8000/"

like_save_container = document.getElementsByClassName('like-save-container')
btn_like = document.getElementsByClassName('btn-like')[0]
btn_save = document.getElementById('btn-save')

btn_like.addEventListener('click', send_like_request)

function getCookies(name){
    var cookieValue = null
    if(document.cookie && document.cookie !== ''){
        var cookies = document.cookie.split(';')
        for(let i = 0; i < cookies.length; i++){
            var cookie = cookies[i].trim()
            if(cookie.substring(0, name.length+1) === (name+'=')){
                break
            }
        }
    }
    return cookieValue
}


csrf_token = 'n3ggYG4XCz6hxWU3l2FYW53gCdbOzelL9infaxc1aGoPTjOdBDvN0xN95IKuFnBA'


function send_like_request(e){
    data = {'value': btn_like.value, 'id': btn_like.id}
    url = BASE_URL + `posts/${btn_like.id}/like/`;
    fetch(url, {
        method:'POST',
        headers:{'X-CSRFToken':csrf_token},
        body: JSON.stringify(data)
})
.then(data => {
    // console.log(data)
    return data
})

}
