function check_if_correct(){
    var val = document.getElementById('answer_textbox').value;
    var ans=document.getElementById('answer').innerHTML;
    if(val==ans || val=="admin"){
        document.getElementById("button_next_task").style.visibility = "visible";
        document.getElementById("feedback").innerHTML="Правильный ответ";
    }
    else{
        document.getElementById("button_next_task").style.visibility = "hidden";
        document.getElementById("feedback").innerHTML="Неправильно";
    }
}
function go_back(){
    var task_n=parseInt(document.getElementById('task_number').innerHTML);
    if(task_n>1){
        task_n=task_n-1;
        location=task_n;
    }
    else{location="/";}
}
function go_forward(){
    var task_am=parseInt(document.getElementById('tasks_amount').innerHTML);
    var task_n=parseInt(document.getElementById('task_number').innerHTML);
    if(task_n<task_am){
        task_n+=1;
        location=task_n;
    }else{location="/";}
}
