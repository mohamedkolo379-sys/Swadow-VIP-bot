from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>MHD - MHMD112</title>
<style>
body{background:#08080a;color:white;font-family:Arial;margin:0;padding:10px}
.card{background:#151515;border-radius:16px;overflow:hidden;border:1px solid #222;text-align:center;margin:10px;padding-bottom:10px;width:45%;display:inline-block;vertical-align:top}
.card-img{height:130px;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:bold}
.mines{background:linear-gradient(135deg,#2daae1,#0a7abf)}
.mines2{background:linear-gradient(135deg,#2a8aff,#0044aa)}
.lucky{background:linear-gradient(135deg,#7a5cff,#3a2a8a)}
.aviator{background:#8a0a1a}
.btn{background:#ff7a00;color:black;border:none;padding:8px 20px;border-radius:20px;font-weight:bold;width:85%;margin:8px;cursor:pointer}
.top{text-align:center;padding:10px;border-bottom:1px solid #222;color:#aaa;font-size:12px}
.top b{color:gold}
</style>
</head>
<body>
<div class="top">CODE PROMO <b>MHMD112</b> - Ta technique ici</div>

<div class="card"><div class="card-img mines">MINES</div><p>Mines</p><button class="btn" onclick="alert('TA TECHNIQUE MINES CLASSIC: 1 Mine=14 etoiles etc - Je vais coder ca')">Ouvrir</button></div>
<div class="card"><div class="card-img aviator">Aviator</div><p>Aviator</p><button class="btn" style="background:transparent;color:#666;border:1px dashed #444">Sous maintenance</button></div>
<div class="card"><div class="card-img lucky">LUCKY JET</div><p>Lucky Jet</p><button class="btn" onclick="alert('TA TECHNIQUE LUCKY JET')">Ouvrir</button></div>
<div class="card"><div class="card-img mines2">MINES</div><p>New Mines</p><button class="btn" onclick="alert('TA TECHNIQUE NEW MINES')">Ouvrir</button></div>

<script>
// ICI TU METS TA TECHNIQUE
// Exemple pour Mines: 
function maTechniqueMines(nombreMines){
  // 1 mine = 14 etoiles
  // 3 mines = 5/6/7 etoiles
  // etc - C'est toi qui decides
  console.log("Technique pour", nombreMines, "mines");
}
</script>
</body>
</html>
    """

# PAS DE if __name__ == "__main__" POUR VERCEL - C'EST CA QUI FAIT PLANTER
