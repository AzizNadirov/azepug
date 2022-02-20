btn_add_emp = document.getElementById('add_emp_btn')
const BASE_URL = "http://127.0.0.1:8000/"



btn_add_emp.addEventListener('click', function (e) {
    document.querySelector('.popup').style.display = "flex"
  })
document.querySelector('.close').addEventListener('click', function(e){
    document.querySelector('.popup').style.display = "none"
})


btnCreateEmp = document.getElementById("btn-create-emp");

var emp_name = document.getElementById("input-emp-name")
var emp_founded = document.getElementById("input-emp_founded") 
var EmpSelectBox = document.getElementById('id_employer')

// validate date and name

function validate(){
    var date_regex = /^(0[1-9]|1[0-2])\/(0[1-9]|1\d|2\d|3[01])\/(0[1-9]|1[1-9]|2[1-9])$/;
    today = new Date()
    entered_date = new Date(emp_founded.value)
    if(emp_name.value.length < 2 && 
            (!date_regex.test(emp_founded.value) || emp_founded.value.length != 0)
            || entered_date.getTime() >= today.getTime() )
     {
        btnCreateEmp.disabled = true
    }
    else{
        btnCreateEmp.disabled = false
    }
}
btnCreateEmp.disabled = true // disable button initially
emp_founded.onchange = validate;
emp_name.onchange = validate;

btnCreateEmp.addEventListener('click',
   function (e) {
      e.preventDefault();
      $.ajax({
        type: 'POST',
        url: BASE_URL + "vacancies/new/emp",
        data: {
          name: emp_name.value,
          founded_at: emp_founded.value,
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
          // action: $('#btn-like').val()
        },
        success: function (json) {
            document.querySelector('.popup').style.display = "none"
            try{
                newOption = document.createElement('option');
                newOption.value = `${json.emp_id}`;
                newOption.text = emp_name.value;
                EmpSelectBox.appendChild(newOption)
                EmpSelectBox.value = newOption.value}
            catch(e){
                if(e instanceof TypeError){
                    EmpSelectBox = document.getElementById('id_organiser')
                    newOption = document.createElement('option');
                    newOption.value = `${json.emp_id}`;
                    newOption.text = emp_name.value;
                    EmpSelectBox.appendChild(newOption);
                    EmpSelectBox.value = newOption.value
                }
                else{
                    console.log("uppss")
                }
            }
            
        },
        error: function (xhr, errmsg, err) {
    
        }
      });
    })