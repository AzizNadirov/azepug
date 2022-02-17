const BASE_URL = "http://127.0.0.1:8000/"

btn_like = document.getElementsByClassName('btn-like')[0]

btn_save = document.getElementsByClassName("btn-save")[0]
console.log(btn_save)



btn_like.addEventListener('click',
   function (e) {
      e.preventDefault();
      $.ajax({
        type: 'POST',
        url: BASE_URL + `posts/${e.target.id}/like/`,
        data: {
          postid: e.target.id,
          value: e.target.value,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          action: $('#btn-like').val()
        },
        success: function (json) {
          console.log(e.target.value)
          if(e.target.value === "like"){
            $(btn_like).html('Unlike')
            e.target.value = 'unlike'
          }
          else{
            $(btn_like).html('like')
            e.target.value = 'like'
          }
        },
        error: function (xhr, errmsg, err) {
    
        }
      });
    })

