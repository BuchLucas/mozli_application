from flask import Flask,render_template
#from flask_ngrok import run_with_ngrok
from flask import request,redirect
#import webbrowser
import os

app = Flask(__name__)
#run_with_ngrok(app)



def verificarCliente(numero,senha):
	num = numero
	cod = senha
	if os.path.isdir(".logsf"):
		...
	else:
		os.mkdir(".logsf")
		
	
	listaClientes = os.listdir(".logsf")
	
	
	
	if str(num)+".txt" in listaClientes:
		
		
		fileD = open(".logsf/"+str(num)+".txt","r")
		
		dadosD = fileD.read()
		
		
		listaD = dadosD.split("\n")
		
		passw = listaD[-1]
		
		if str(passw) == str(cod):
			print("Senha Valida!")
			return "si014"
		else:
			return "se012"
	return "ne013"
	
	
def criarCliente_c(numero,senha,email,nome):
	num = str(numero)
	cod = str(senha)
	mail = str(email)
	nom = str(nome)
	
	
	
	
	
	if os.path.isdir(".logsf"):
		...
	else:
		mkdir(".logsf")
		
	
	listaClientes = os.listdir(".logsf")
	
	
	
	if str(num)+".txt" in listaClientes:
		return True
	
	clienteN = open(".logsf/"+str(num)+".txt","w")
	
	clienteN.write(nom+"\n"+num+"\n"+mail+"\n"+cod)
	return False
	



def dadofilm():
	listaF = os.listdir("static/class8")
	titulo = "Melhor Serie de 2025 nao perca o lancamento da serie fantasticos"
	TodosD = ""
	for i in range(len(listaF)):
		linkImg = listaF[i-1]
		titulo = linkImg.split(".")[0]
		pathSerie =str("8class8-")+str(linkImg).split(".")[0]
		dadoF = (f"""
		<div class="discipli">

		<br><a href="/showserie/{pathSerie}">

		<span><img class="img_lista_li" src="static/class8/{linkImg}"/>
		</span>

		<h5><b>{titulo}</b></h5>

		</a>
</div>""")
		
		
		TodosD = TodosD + dadoF
	
	
	
	return TodosD


def dadoserie():
	listaF = os.listdir("static/class9")
	titulo = "Melhor Serie de 2025 nao perca o lancamento da serie fantasticos"
	TodosD = ""
	for i in range(len(listaF)):
		linkImg = listaF[i-1]
		titulo = linkImg.split(".")[0]
		pathSerie = str("9class9-")+str(linkImg).split(".")[0]
		dadoF = (f"""
		<div class="discipli">

		<br><a href="/showserie/{pathSerie}">

		<span><img class="img_lista_li" src="static/class9/{linkImg}"/>
		</span>

		<h5><b>{titulo}</b></h5>

		</a>
</div>""")
		
		
		TodosD = TodosD + dadoF
	
	
	
	return TodosD

def dadoanime():
	listaF = os.listdir("static/class10")
	titulo = "Melhor Serie de 2025 nao perca o lancamento da serie fantasticos"
	TodosD = ""
	for i in range(len(listaF)):
		linkImg = listaF[i-1]
		titulo = linkImg.split(".")[0]
		pathSerie = str("10class10-")+str(linkImg).split(".")[0]
		dadoF = (f"""
		<div class="discipli">

		<br><a href="/showserie/{pathSerie}">

		<span><img class="img_lista_li" src="static/class10/{linkImg}"/>
		</span>

		<h5><b>{titulo}</b></h5>

		</a>
</div>""")
		
		
		TodosD = TodosD + dadoF
	
	
	
	return TodosD


        

def loadTemp(spath):
	
	
	nomeP = spath.split("-")
	nomeSPasta = nomeP[0]+"/"+nomeP[1]
	
	pastaTemps = f"static/{nomeSPasta}"
	paginas = os.listdir(pastaTemps)
	
	todasTemp = ""
	lt = len(paginas)
	todosHtmlPages = ""
	for cpag in range(len(paginas)):
		
		
		idTP = str(cpag)
		numpages = len(paginas)
	
		if 1 == 1:
			tmp =str("1")
			page = str(cpag+1)
			cpag1 = str(cpag+1)
			linkv = str(nomeSPasta+"/"+cpag1).replace("/","_")
			lancado = "2025_ plural_editora"
			nomeTitulo = f"{nomeSPasta} |class: {tmp} pagina: {cpag1}".replace("|","xkdz")
			nomeTitulo = nomeTitulo.replace(" ","dfrcz")
			
			nomeTitulo = nomeTitulo.replace(":","uxtak")
			catg = "livroDeEducacao"
			
			
			
			
			classNome = nomeP[0][:-1]
			livroNome = nomeP[1]
			
			titulo= f"{livroNome} | {classNome} paginas: {page}"
			dadoEps= (f"""
		<div class="discipli">

		<br><a href="/assistir/{linkv}/{lancado}/{nomeTitulo}/{catg}">

		<span><img class="img_lista_li" src="/static/{nomeSPasta}/{cpag1}.png"/>
		</span>

		<h5><b>{titulo}</b></h5>

		</a>
</div>""")
			todosHtmlPages = todosHtmlPages + dadoEps
			
		todosepsTemps = """ <div class="caixa_drop_li"  >"""+todosHtmlPages+"""</div>"""
		
	
	
	todoBoxTemp = todosHtmlPages+"""<br><br>"""
		
	return todoBoxTemp




@app.route("/home")
def home():
	
	
	dadoF = dadofilm()
	dadoS = dadoserie()
	dadoA = dadoanime()
	
	
	
	
	mainSite = ("""<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="stylesheet" href="../styles/style.css"/>

    <title>MozLi</title>

    <style>

    

    

    

    body{

        margin: 0px;

    }

    

    

    

    

    

    

#textoMain{

    font-size: 30px;

    text-align: center;

    background-image: url("../image/bg1.jpg");

    background-color: #77bddd;

    background-size: cover;

    color: white;

  }

  

  .caixa{

    width: 100%;

    

    height: 350px;

    background-color: #77bddd;

    margin: 10px;

    display: flex;

   

    

    

  }

  .caixa div{

    width: 98%;

    display:grid;

    grid-template-columns: auto;

    grid-gap: 20px;

    padding:10px;

  }

  

  .caixa div img{

    width:60%;

  }

  #boxCab{

    text-align: left;

    margin:15px;

    

  }

  

  

  .caixinha{

    width: 100%;

    height: 160px;

    background-color: #0ad;

    color: white;

    text-align: center;

    margin-top: -25px;

    background-image: url("{{url_for('static',filename='/series/round6_2.jpg')}}");

    background-repeat: no-repeat;

    background-size: cover;

  }

  #ch1{

    width: 100%;

    font-size: 35px;

    text-align: center;

    margin: 20px;

    

  }

  .subC{

    font-size: 30px;

    padding-top: 30px;

  }

  #nameS{

    color: red;

    float: right;

    padding-top: 1px;

    font-size: 35px;

  }

  #img_menu{

    height: 20px;

    width:25px;

    margin-left:3px;

    

  }

  

  .imgp{



    width:10%;

    height:330px;

    text-align: center;

    align-self: center;



  }



  .btnr{

    background-color:rgb(48, 195, 214);

    width: 150px;

    height: 40px;

    color: #f0eeee;

  }



  .btnr:hover{

    width: 170px;

    height: 50px;

    background-color:tomato;

  }

  .and{

    width: 100%;

    position:absolute;

    background-color: darkcyan;

    color: #aff804;

    



  }

  #caixa_suj{



    width: 90%;

    margin:50px;

    text-align: center;



  }

  #text_suj{





    font-size:30px;



  }



  .caixa_lista_li{



    background-color: #77bddd;

    margin: 5%;

    border-radius:10px;

    padding: 10px;



  }

  #drop_8{

    display: none;

  }

  #drop_9{

    display: none;

  }

  #drop_10{

    display: none;

  }



  .img_lista_li{



    width: 260px;

    height: 150px;

  }

  .img_lista_li_drop{



    width: 100px;

    height: 90px;

    margin-left: 20px;

  }





  .discipli{

    float:left;

    width: 300px;

    text-align: center;

    margin: 7px;

    background-color: #F0F8FF;

    border-radius: 7px;

    border: solid 4px #00005511;

    



  }

  .caixa_drop_li{

    

    

    background:#174580;

    background-color: #aff804;

    background-position: center;

    background-image: url("../image/bg1.jpg");

    color: red;

  }

  #drop_8{

    display: none;

  }

  #drop_9{

    display: none;

  }

  #drop_10{

    display: none;

  }



  #pop_menu{

    width: 250px;

    margin: 10%;

    border: 3px solid #174580;

    text-align: center;

    background: navy;

    color: red;

    border-radius: 20px;

    display: none;

    position: fixed;

    

    

    

  }



  #form1{

    width: 280px;

    margin: 10%;

    

    border: 3px solid #17458055;

    text-align: center;

    background: silver;

    color: #222222;

    border-radius: 20px;

    display: none;

    position: fixed;

    

    

    

    

  }

  

  #form p{

      font-size: 10px;

  }

  #form2{

    width: 50%;

    margin: 10%;

    border: 3px solid #174580;

    text-align: center;

    background: navy;

    color: red;

    border-radius: 20px;

    display: none;

    position: fixed;

    

    

    

  }



  #img_mv{

    height: 40px;

    width:50px;

    

  }

  #img_vm{

    height: 40px;

    width:50px;

    

  }

  .pform{

    text-align: left;

    margin-left: 10px;

    border-radius: 10px;

  }

  

  input{

    width: 80%;

    height: 23px;

    border-radius: 10px;

    border: 2px solid green;

    color: teal;

    font-size: 17px;

    

  }

  

  button{

    width: 150px;

    height: 30px;

    border-radius: 10px;

    margin: 20px;

  }

  

  textarea{

    width: 80%;

    height: 100px;

    border-radius: 15px;

    border: 2px solid green;

    color: teal;

    font-size: 18px;

  }

  #PFF{



font-size: 10px;

  }

  

#mx{

    background-color:#ffffff00;

    color: red;

}

  

  #ddd{

    

    background-color: #0007;

      

  }



.pf{

    font-size: 12px;

    

}



.mai_box_spay{

    width: 100%;

}

.box_spay{

    width: 47%;

    background-color: #0022ad55;

    float: left;

    margin: 2px;

    border-radius: 7px;

}



.box_spay:hover{

    background-color:#88221188;

}

    </style>

</head>

<body>





    <form id="form1">

        <p class="pform">Nome: </p>

        <input id="inNomePay" type="name" required>

        <p class="pform">Numero de Telefone: </p>

        <input id="inTellPay" type="tel" required>

        <p class="pf" id="PFF"><b>OPCOES DE PAGAMENTO: </b></p>

        <img onclick="seleted_mv()" id="img_mv" src="static/image/mvm1.png" alt="movi" >

        <img onclick="seleted_vm()" id="img_vm" src="static/image/vmp1.png" alt="voda" >

        <div mai_box_spay>

            <div class="box_spay">

        <p class="pf">Semanal 50MTS</p><input name="mpay" type="radio"required>

        </div>

        <div class="box_spay">

        <p class="pf">Mensal 150MTS</p><input name="mpay" type="radio"required>

        </div>

        </div>

        <button onclick="paquei()" type="submit">PAGAR SUBSCRICAO</button>

    </form>

    <div class="caixinha" >

        <br>

    <h1 id="ddd"><mark id="mx">Moz</mark>SFilmes</h1>

    <p>se ainda nao tens acesso inscreva se nessa plataforma

        de baixo custo para baixar seus filmes series e animes.

    </p>

    <button onclick="open_form()" class="btnr">Inscreva Se</button>

    </div>

<br><br><br>

    <div class="caixa_lista_li" id="caixa_8">



        <p class="text_lista_li" ><h2>8 class</h2></p>

        <span><img class="img_lista_li" src="/static/class8/Biologia.jpeg"/></span>

        <span><img onclick="open_8()" id="img_baisim8" class="img_lista_li_drop" src="/static/image/bai.png"/></span>



    </div>

    <div class="caixa_drop_li" id="drop_8">

       """+dadoF+"""
       

    </div>



    <div class="caixa_lista_li" id="caixa_9">



        <p class="text_lista_li" ><h1>9 Class</h1></p>

        <span><img class="img_lista_li" src="/static/class9/Fisica.jpeg"/></span>

        <span><img onclick="open_9()" id="img_baisim9" class="img_lista_li_drop" src="/static/image/bai.png"/></span>

    </div>
    <div class="caixa_drop_li" id="drop_9">

        """+dadoS+"""
    </div>

    <div class="caixa_lista_li" id="caixa_10" >



        <p class="text_lista_li" ><h2>10 Class</h2></p>

        <span><img class="img_lista_li" src="/static/class10/Historia.jpg"/></span>

        <span><img onclick="open_10()" id="img_baisim10" class="img_lista_li_drop" src="static/image/bai.png"/></span>

    </div>

    <div class="caixa_drop_li" id="drop_10">

       """+dadoA+"""
    </div>

   

    <script>

        

        

document.getElementById("textoMain").innerHTML ="Caro estudante!, acabou a preocupacao esse biblioteca Online com Livros para os seus estudos, Acabou adescupa de nao ser inteligente!";

document.getElementById("ch1").innerHTML = "O Futuro E Seu, Naisceste para Brilhar!";





function paquei(){
    let nn = document.getElementById("inNomePay").value;
    
    let tt = document.getElementById("inTellPay").value;
    
    lentt = tt.length;
    
    lennn = nn.length;
    if (lentt > 0){
        if (lennn > 0){
        
        alert("Espere alguns segundos para o sistema atualizar!");
        
        }
    	}else{
    	
    
    }

}









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

        img.src = "url_for('static',filename='/image/sim.png')";

        

        var ca9 = document.getElementById("caixa_9");

        var ca10 = document.getElementById("caixa_10");

        ca9.style.display = "none";

        ca10.style.display = "none";



    }else{



        img.src = "url_for('static',filename='/image/bai.png')";

        c8.style.display = "none";

        
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

        img.src = "url_for('static',filename='/image/sim.png')";

        
        var ca8 = document.getElementById("caixa_8");

        var ca10 = document.getElementById("caixa_10");

        ca8.style.display = "none";

        ca10.style.display = "none";



    }else{



        c9.style.display = "none";

        img.src = "url_for('static',filename='/image/bai.png')";

        
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

        img.src = "url_for('static',filename='/image/sim.png')";

        
        var ca9 = document.getElementById("caixa_9");

        var ca8 = document.getElementById("caixa_8");

        ca9.style.display = "none";

        ca8.style.display = "none";



    }else{



        c10.style.display = "none";

        img.src = "url_for('static',filename='/image/bai.png')";

        
        var ca9 = document.getElementById("caixa_9");

        var ca8 = document.getElementById("caixa_8");

        ca9.style.display = "block";

        ca8.style.display = "block";



    }

    

    

}

        

        

    </script>

    

</body>

</html>
	""")
	error = None
	
	"""
	if request.method == "POST":
		
		if valid_login(request.form["name"],
		request.form["password"]):
			numero = request.form["phone"]
			senha = request.form["password"]
	"""
	
	return mainSite

@app.route("/", methods= ["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
	
	
	
	
	return render_template("login.html",atvInfo= "none",infoLog1 = "")


@app.route("/create_login", methods= ["GET","POST"])
def create_login():
	return render_template("create_account.html",atvCLInfo="none",infoCLog1 = "")

@app.route("/assistir/<videourl>/<lancam>/<titulov>/<catego>", methods= ["GET","POST"])
def assistir(videourl,lancam,titulov,catego):
	
	videourl = videourl
	lancam = lancam.replace("_",",")
	titulov = titulov.replace("_"," ")
	titulov = titulov
	catego = catego.replace("_",",")
	
	
	
	ttl = "ola esse é o titulo"
	if "_T" in videourl:
		
		
		titulov = titulov.replace("xkdz","|")
		
		titulov = titulov.replace("dfrcz"," ")
		titulov = titulov.replace("uxtak",":")
		
		videourl = videourl.replace("_","/")
		url = "/static/series8/"+videourl+".mp4"
	else:
		videourl = videourl.replace("_"," ")
		url = "/static/filmes8/"+videourl+".mp4"
	ctg1 = "acacao"
	
	
	return render_template("assistir.html",urlv = url,titulo = titulov,lancamen= lancam, ctg = catego)

@app.route("/showserie/<seriePath>", methods= ["GET","POST"])
def showserie(seriePath):
	"""
	videourl = videourl
	lancam = lancam.replace("_",",")
	titulov = titulov.replace("%"," ")
	catego = catego.replace("%",",")
	
	"""
	
	
	readTemp = loadTemp(seriePath)
	
	ttl = seriePath
	url = "static/filmes8/haven.mp4"
	ctg1 = "acacao"
	
	
	
	serieS = """
	<!DOCTYPE html>

<html>
<head>
 
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  
  <meta http-equiv="CONTENT-TYPE" content="text/html; charset=UTF-8">
  <link rel="stylesheet" href="url_for('static',filename='/static/styles/style.css')"/>
  <title>NetSFilm</title>
  <style>
 
body{
    margin: 0px;
    text-align: center;
  }
  
  
#mx{
    background-color:#ffffff00;
    color: red;
}
  
  #ddd{
    
    background-color: #0007;
      
  }
  .form{
      background-color: #0011;
      padding: 10px;
      margin: 10px;
      border-radius: 20px;
  }
  
  #formI{
      
      display: none;
  }
  #textoMain{
    font-size: 30px;
    text-align: center;
    background-image: url("{{url_for('static',filename='/image/bg1.jpg')}}");
    background-color: #77bddd;
    background-size: cover;
    color: white;
  }
  
  .caixa{
    width: 100%;
    
    height: 350px;
    background-color: #77bddd;
    margin: 10px;
    display: flex;
   
    
    
  }
  .caixa div{
    width: 98%;
    display:grid;
    grid-template-columns: auto;
    grid-gap: 20px;
    padding:10px;
  }
  
  .caixa div img{
    width:60%;
  }
  #boxCab{
    text-align: left;
    margin:15px;
    
  }
  
  
  .caixinha{
    width: 100%;
    height: 160px;
    background-color: #0ad;
    color: white;
    margin-top: -25px;
    background-image: url("{{url_for('static',filename='/series/round6_2.jpg')}}");
    background-repeat: no-repeat;
    background-size: cover;
    
    
    
    
  }
  #ch1{
    width: 100%;
    font-size: 35px;
    text-align: center;
    margin: 20px;
    
  }
  .subC{
    font-size: 30px;
    padding-top: 30px;
  }
  #nameS{
    color: red;
    float: right;
    padding-top: 1px;
    font-size: 35px;
  }
  #img_menu{
    height: 20px;
    width:25px;
    margin-left:3px;
    
  }
  
  .imgp{

    width:10%;
    height:330px;
    text-align: center;
    align-self: center;

  }

  .btnr{
    background-color:rgb(48, 195, 214);
    width: 150px;
    height: 40px;
    color: #f0eeee;
  }

  .btnr:hover{
    width: 170px;
    height: 50px;
    background-color:tomato;
  }
  .and{
    width: 100%;
    position:absolute;
    background-color: #11f0da55;
    color: #a0ddf04;
    

  }
  #caixa_suj{

    width: 90%;
    margin:50px;
    text-align: center;

  }
  #text_suj{


    font-size:30px;

  }

  .caixa_lista_li{

    background-color: #77bddd;
    margin: 5%;
    border-radius:10px;

  }
  #drop_8{
    display: none;
  }
  #drop_9{
    display: none;
  }
  #drop_10{
    display: none;
  }

  .img_lista_li{

    width: 97%;
    height: 400px;
  }
  .img_lista_li_drop{

    width: 100px;
    height: 90px;
    margin-left: 20px;
  }
  
  #T1{
  display: none;
  }
  
  #T2{
  display: none;
  }
  


  .discipli{

    float:left;

    width: 300px;
    

    text-align: center;

    margin: 4px;

    background-color: #F0F8FF;

    border-radius: 7px;
    
    border: solid 2px #00005511;

    



  }
  .caixa_drop_li{

    

    

   
    background-position: center;

    background-image: url("../image/bg1.jpg");

    color: red;

  }
  #drop_8{
    display: none;
  }
  #drop_9{
    display: none;
  }
  #drop_10{
    display: none;
  }

  #pop_menu{
    width: 250px;
    margin: 10%;
    border: 3px solid #174580;
    text-align: center;
    background: navy;
    color: red;
    border-radius: 20px;
    display: none;
    position: fixed;
    
    
    
  }

  #form1{
    width: 50%;
    margin: 10%;
    border: 3px solid #174580;
    text-align: center;
    background: navy;
    color: red;
    border-radius: 20px;
    display: none;
    position: fixed;
    
    
    
  }
  #form2{
    width: 50%;
    margin: 10%;
    border: 3px solid #174580;
    text-align: center;
    background: navy;
    color: red;
    border-radius: 20px;
    display: none;
    position: fixed;
    
    
    
  }

  #img_mv{
    height: 40px;
    width:50px;
    
  }
  #img_vm{
    height: 40px;
    width:50px;
    
  }
  .pform{
    text-align: left;
    margin-left: 20px;
    border-radius: 10px;
  }
  
  input{
    width: 80%;
    height: 23px;
    border-radius: 10px;
    border: 2px solid green;
    color: teal;
    font-size: 17px;
    
  }
  
  button{
    width: 150px;
    height: 30px;
    border-radius: 10px;
    border: 2px solid #55555500;
    margin: 20px;
  }
  
  textarea{
    width: 80%;
    height: 100px;
    border-radius: 15px;
    border: 2px solid green;
    color: teal;
    font-size: 18px;
  }
  #PFF{


  }

video{
    
    border-radius: 20px;
    width: 98%;
}
  
  .imgMS{
      width: 98%;
      height: 200px;
      border-radius: 10px;
  }
  .box_temp{
      
      width: 180px;
      height: 30px;
      background-color: #555555;
      padding: 2px;
      margin: 5px;
      color: white;
      float: left;
  }
  
  .box_temp img{
      width: 20px;
      height: 20px;
      margin: 4px;
      float: right;
      border-radius: 20px;
      border: 1px solid #0077ff;
      margin-right: 8px;
  }
  </style>
</head>
<body>
  <nav id="pop_menu">
    <button onclick="close_pop_menu()" style="width:50px; font-size: 30px; color:red; background-color: yellow; float: right;" class="btnr">X</button>
    <button class="btnr">Home</button>
    <button class="btnr">Filmes</button>
    <button class="btnr">Series</button>
    <button class="btnr">Animes</button>
    <button class="btnr">Pano de Acesso</button>
    
  </nav>


  <form id="form1" >
    <p class="pform">Nome: </p>
    <input type="name" >
    <p class="pform">Numero de Telefone: </p>
    <input type="tel" >
    <p class="pform" id="PFF"><b>OPCOES DE PAGAMENTO: </b></p>
    <img onclick="seleted_mv()" id="img_mv" src="image/mvm1.png" alt="menu" >
    <img onclick="seleted_vm()" id="img_vm" src="image/vmp1.png" alt="menu" >
    <p>Semanal 50MTS</p><input name="mpay" type="radio">
    <p>Mensal 150MTS</p><input name="mpay" type="radio">
    <button type="submit">Enviar</button>
 
  </form>
<div class="caixinha" >
        <br>
    <h1 id="ddd"><mark id="mx">Moz</mark>Li</h1>
    <p>se ainda nao tens acesso inscreva se nessa plataforma
        de baixo custo para ter  acesso a livros de todas classes.
    </p>
    
    </div>
  <form class="form" id="formI">
    <p class="pform">Nome: </p>
    <input type="name" >
    <p class="pform">Seu Email: </p>
    <input type="email" >
    <p class="pform">Numero de Telefone: </p>
    <input type="phone"></textarea><br>
    
    
 <p class="pform">Criar Senha: </p>
 
  <input type="password" >
<p class="pform">Confirmar a Senha: </p>
 
  <input type="password" >
    <button type="submit">Inscrever-se</button>
    <a href="#"><p>Ja tenho o conta</p></a>
    
  </form>
  <br><br>
  <div   style="text-align: center;">
<div style="text-align: left; padding: 10px;">
<h3>"""+ttl+"""</h3>
<p>lancamento:  2025,plural editora</p>
  </div>
  
  <br>
  <div>
    """+readTemp+"""
</div>
  
  <hr>


 

<script src="/static/scripts/index.js">



</script>
</body>
</html>"""
	
	
	return serieS



@app.errorhandler(404)
def invalid_route(e):
	
	
	
	return render_template("erroh.html")


@app.route("/verifyClient", methods=["POST"])
def acessarCliente():
	
	m_tell = request.form.get('phoneClient')
	
	m_senha = request.form.get("passwordy")
	
	
	print(f"Telefone:  {m_tell}")
	print(f"Senha: {m_senha}")
	
	
	resultado = verificarCliente(m_tell,m_senha)
	
	lginfosh = "Senha Invalida!\nPorfavor digite a senha e o numero correcto! para poder acessar o sistema."
	
	lginfone = "Este numero nao tem uma conta!\nPorfavor click em criar uma conta."
	
	if resultado =="se012":
		print("Senha Invalida!")
		lginfo = lginfosh
	elif resultado == "ne013":
		print("Cliente nao Existe!")
		lginfo = lginfone
	elif resultado == "si014":
		print("dados Correctos!")
		return redirect("/home")
	else:
		lginfo = "Problemas com a sua conta contate a nossa coracao."
	
	
	
	
	
	return render_template("login.html",atvInfo="block",infoLog1 =lginfo )
	#return login()
	
	
@app.route("/createClient", methods=["POST"])
def criarCliente():
	
	m_tell = request.form.get('phoneClient')
	
	m_email = request.form.get("email")
	
	m_nome = request.form.get('nome')
	
	m_senha = request.form.get("password_")
	
	m_senha2 = request.form.get("passconfirm")
	
	if str(m_senha) == str(m_senha2):
		resultado = criarCliente_c(m_tell,m_senha,m_email,m_nome)
		
		if resultado == False:
		 	print("Numero: "+str(m_tell))
		 	print("Senha: "+str(m_senha))
		 	
		 	print("Dados Criados Com Sucesso!")
		 	return redirect("/")
		else:
			print("Cliente Existe!")
			clinfo = "Ja existe um cliente com esse numero! tente usar outro numero!"
	
		
		
	else:
		clinfo = "As Senhas Nao estao a Corresponder!"
		
	
	
	
	print(f"Telefone:  {m_tell}")
	print(f"Senha: {m_senha}")
	
	
	
	
	#snc senha nao corrresponde!
	#False significa que o cliente nao existe e foi criadk com sucesso!
	
	
	
	
	
	
	return render_template("create_account.html",atvCL="block",infoCLog1 = clinfo)



"""
 <div class="discipli">

         <br><a href="/assistir">

            <span><img class="img_lista_li"  src="{{url_for('static',filename='/series/o_protetor.jpg')}}"/></span>

            <h3><b>Mortal Kombat</b></h3>

            </a>

        </div>

"""







if __name__ == "__main__":
    #webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(port=5000)
