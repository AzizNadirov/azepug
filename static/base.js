function likeSave(app_name){
  var what_done = null 
  const BASE_URL = "http://127.0.0.1:8000/"
  btn_like = document.getElementsByClassName('btn-like')[0]
  btn_save = document.getElementsByClassName('btn-save')[0]

  btn_like.addEventListener('click',
    function (e) {
        e.preventDefault();
        $.ajax({
          type: 'POST',
          url: BASE_URL + "like",
          data: {
            postid: e.target.id,
            value: `${app_name}|` + e.target.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function (json) {
            if(e.target.value === "like"){
              $(btn_like).html('Unlike')
              e.target.value = 'unlike'
              what_done = 1
            }
            else{
              $(btn_like).html('like')
              e.target.value = 'like'
              what_done = -1
            }
          },
          error: function (xhr, errmsg, err) {
      
          }
        });
      })
      btn_save.addEventListener('click',
      function (e) {
        e.preventDefault();
        $.ajax({
          type: 'POST',
          url: BASE_URL + 'save',
          data: {
            postid: e.target.id,
            value: `${app_name}|` + e.target.value,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            //  action: $('#btn-like').val()
          },
          success: function (json) {
            if(e.target.value === "save"){
              $(btn_save).html('unsave')
              e.target.value = 'unsave'
            }
            else{
              $(btn_save).html('save')
              e.target.value = 'save'
            }
          },
          error: function (xhr, errmsg, err) {
      
          }
        });
      })
    return what_done
}
