
function supportSave(app_name){
    const BASE_URL = "http://127.0.0.1:8000/"
    btn_support = document.getElementsByClassName('btn-support')[0]
    btn_save = document.getElementsByClassName('btn-save')[0]

    btn_support.addEventListener('click',
      function (e) {
          e.preventDefault();  
          $.ajax({
            type: 'POST',
            url: BASE_URL + "support",
            data: {
              postid: e.target.id,
              value: `${app_name}|` + e.target.value,
              csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (json) {
              if(e.target.value === "support"){
                $(btn_support).html('Unsupport')
                e.target.value = 'unsupport'
              }
              else{
                $(btn_support).html('Support')
                e.target.value = 'support'
              }
            },
            error: function (xhr, errmsg, err) {
        
            }
          });
        });
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
  }