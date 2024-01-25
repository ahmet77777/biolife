
function Check_2(el){
    var username = el.username.value;
    var email = el.email.value;
    var pass = el.password1.value;
    var repass = el.password2.value;

    
    var fail = '';

    if(username == '' || email == "" || pass == "" || repass == "")
        fail = 'Аill in all fields';
    else if(pass != repass)
        fail = "Passwords must match";
    else if(pass > 8 || repass > 8)
        fail = "Password must be 8 digits";
    else if(username.length < 2 || username.length > 50){
        fail = 'Enter correctly username';
    }




    if(fail != '')
        document.getElementById('error').innerHTML = fail;
    else{
        return true
    }
    


   
    
    return false
    
}