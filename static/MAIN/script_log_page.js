window.onload = function(){
    console.log("hello");

    document.getElementById("carousel").innerHTML = "Se connecter en tant qu\'élève";

    document.getElementById("Go_etu").addEventListener("click", function(){
        document.getElementById("carousel").innerHTML = "Se connecter en tant qu\'élève";
    });

    document.getElementById("Go_ens").addEventListener("click", function(){
        document.getElementById("carousel").innerHTML = "Se connecter en tant qu\'enseignant";
    });
}

docuement