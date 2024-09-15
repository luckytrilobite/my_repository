function change(a,b)
{
    let hide = document.querySelector(a);
    let show = document.querySelector(b);

    hide.style.display = "none";
    show.style.display = "block";

    return;
}

function login()
{
    let account = document.getElementById("inaccount").value;
    let password = document.getElementById("inpass").value;

    fetch('api/loginout',
    {
        method:'POST',
        headers: {'Content-Type': 'application/json',},
        body:JSON.stringify
        ({
            "account": account,
            "password": password,
            'logch': 'login'
        }),
    })
    .then(response => response.text())
    .then(text => {
        if (text == 'ok') 
        {
            let url = `/profile/${account}`;
            window.location.href = url;
        }
        else
        {
            alert("wrong input");
        }
    })
    .catch((error) => {
        console.log("Error",error);
    })
    return;
}

function logout()
{
    let account = document.getElementById("outacc").value;

    fetch('/api/loginout',
        {
            method:'POST',
            headers: {'Content-Type': 'application/json',},
            body:JSON.stringify
            ({
                "account": account,
                "password": "",
                'logch': 'logout'
            }),
        })
        .then(response => response.text())
        .then(text => {
            if (text == 'ok') 
            {
                window.location.href = '/home';
            }
            else
            {
                console.log("Error");
            }
        })
        .catch((error) => {
            console.log("Error",error);
        })

    return;
}

function getdata()
{
    let account = document.getElementById('outacc').innerText

    fetch('/api/getdata',{
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify
        ({
            "account":account
        }),
    })
    .then(response => response.json())
    .then(data =>{
        console.log(data);
        if (data['statu'] == 'ok') {
            document.getElementById('mail').innerText = data['info'].mail;
            document.getElementById('number').innerText = data['info'].number;
        }
        else
        {
            alert("請先登入")
            document.location.href = '/home'
        }
    })
    .catch(error => {
        console.log("Error",error);
    })

    return
}

function signup()
{
    let data = {
        'account': document.getElementById('upacc').value,
        'password': document.getElementById('uppasw').value,
        'mail': document.getElementById('mail').value,
        'number': document.getElementById('num').value,
    };
    
    fetch('/api/signup',{
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(data),
    })
    .then(response => {
        alert("succes");
        change('#signup','#signin')
    })
    .catch(error => console.log("Error",error))    
}