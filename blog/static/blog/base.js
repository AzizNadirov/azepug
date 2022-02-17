// like-save
const BASE_URL = "http://127.0.0.1:8000/"

like_save_container = document.getElementsByClassName('like-save-container')
btn_like = document.getElementsByClassName('btn-like')[0]
btn_save = document.getElementById('btn-save')

// btn_like.addEventListener('click', send_like_request)


function getCookie(name) {
    if (!document.cookie) {
      return null;
    }
  
    const xsrfCookies = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith(name + '='));
  
    if (xsrfCookies.length === 0) {
      return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
  }
  csrf_token = getCookie('csrftoken')
// csrf_token = 'n3ggYG4XCz6hxWU3l2FYW53gCdbOzelL9infaxc1aGoPTjOdBDvN0xN95IKuFnBA'


// function send_like_request(e){
//     data = {'value': btn_like.value, 'id': btn_like.id}
//     url = BASE_URL + `posts/${btn_like.id}/like/`;
//     fetch(url, {
//         method:'POST',
//         headers:{'Content-Type': 'application/json',
//                     "Accept": "application/json",
//                     'X-CSRFToken':csrf_token},
//         body: JSON.stringify(data)
// })
// .then(data => {
//     console.log(data)
//     return data
// })

// }




