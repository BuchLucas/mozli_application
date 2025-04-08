document.getElementById("textoMain").innerHTML ="Caro estudante!, acabou a preocupacao esse biblioteca Online com Livros para os seus estudos, Acabou adescupa de nao ser inteligente!";
document.getElementById("ch1").innerHTML = "O Futuro E Seu, Naisceste para Brilhar!";


function open_pop_menu(){

    var menu = document.getElementById("pop_menu");
    menu.style.display = "block";
}

function close_pop_menu(){

    var menu = document.getElementById("pop_menu");
    menu.style.display = "none";
}

function open_form(){

    var form = document.getElementById("form1");
    form.style.display = "block";
}

function open_form_suj(){

    var form = document.getElementById("form2");
    form.style.display = "block";
}

function seleted_vm(){

    var vm = document.getElementById("img_vm");
    var mv = document.getElementById("img_mv");
    vm.style.border = "solid yellow 5px"
    mv.style.border = "0px"

}

function seleted_mv(){
    var vm = document.getElementById("img_vm");
    var mv = document.getElementById("img_mv");
    vm.style.border = "0px";
    mv.style.border = "solid yellow 5px";

}

function open_8(){

    var c8 = document.getElementById("drop_8");
    var bknn = c8.style.display;
    var img = document.getElementById("img_baisim8");

    if (bknn == "none"){
        c8.style.display = "block";
        img.src = "../image/sim.png";
        alert("Estudante Siga as Nossas Redes Sociais!");
        var ca9 = document.getElementById("caixa_9");
        var ca10 = document.getElementById("caixa_10");
        ca9.style.display = "none";
        ca10.style.display = "none";

    }else{

        img.src = "../image/bai.png";
        c8.style.display = "none";
        alert("Estudante Siga as Nossas Redes Sociais!");
        var ca9 = document.getElementById("caixa_9");
        var ca10 = document.getElementById("caixa_10");
        ca9.style.display = "block";
        ca10.style.display = "block";

    }
    
    
}
function open_9(){

    var c9 = document.getElementById("drop_9");
    var bknn = c9.style.display;
    var img = document.getElementById("img_baisim9");

    if (bknn == "none"){
        c9.style.display = "block";
        img.src = "../image/sim.png";
        alert("Estudante Siga as Nossas Redes Sociais!");
        var ca8 = document.getElementById("caixa_8");
        var ca10 = document.getElementById("caixa_10");
        ca8.style.display = "none";
        ca10.style.display = "none";

    }else{

        c9.style.display = "none";
        img.src = "../image/bai.png";
        alert("Estudante Siga as Nossas Redes Sociais!");
        var ca8 = document.getElementById("caixa_8");
        var ca10 = document.getElementById("caixa_10");
        ca8.style.display = "block";
        ca10.style.display = "block";

    }
    
    
}function open_10(){

    var c10 = document.getElementById("drop_10");
    var bknn = c10.style.display;
    var img = document.getElementById("img_baisim10");

    if (bknn == "none"){
        c10.style.display = "block";
        img.src = "../image/sim.png";
        alert("Estudante Siga as Nossas Redes Sociais!");
        var ca9 = document.getElementById("caixa_9");
        var ca8 = document.getElementById("caixa_8");
        ca9.style.display = "none";
        ca8.style.display = "none";

    }else{

        c10.style.display = "none";
        img.src = "../image/bai.png";
        alert("Estudante Siga as Nossas Redes Sociais!");
        var ca9 = document.getElementById("caixa_9");
        var ca8 = document.getElementById("caixa_8");
        ca9.style.display = "block";
        ca8.style.display = "block";

    }
    
    
}