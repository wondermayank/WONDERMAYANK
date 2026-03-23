<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wondermayank ✨</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
:root {
    --primary: #c8a2ff;
    --secondary: #aeefff;
    --bg: linear-gradient(135deg,#fdfbff,#ebfaff);
    --glass: rgba(255,255,255,0.35);
    --border: rgba(255,255,255,0.5);
}

*{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif;}

body{
    background:var(--bg);
    color:#111;
}

/* NAV */
nav{
    position:fixed;
    width:100%;
    top:0;
    padding:15px 10%;
    display:flex;
    justify-content:space-between;
    backdrop-filter:blur(20px);
    background:var(--glass);
    border-bottom:1px solid var(--border);
}

nav a{ text-decoration:none; color:#111; margin:0 10px; }

/* HERO */
.hero{
    height:100vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
    padding:20px;
}

.hero h1{
    font-size:3.5rem;
    margin-bottom:20px;
}

.hero p{
    color:#666;
    max-width:500px;
}

/* ACTION BOXES */
.action-boxes{
    display:flex;
    gap:20px;
    margin-top:30px;
    flex-wrap:wrap;
}

.action-box{
    background:var(--glass);
    border:1px solid var(--border);
    padding:20px 30px;
    border-radius:20px;
    text-decoration:none;
    color:#111;
    text-align:center;
    transition:.3s;
}

.action-box span{font-size:2rem;}

.action-box:hover{
    transform:translateY(-5px) scale(1.05);
    border-color:var(--primary);
}

/* IMAGE */
.ecosystem{
    margin-top:50px;
}

.ecosystem img{
    width:300px;
    border-radius:20px;
}

/* TECH STACK */
.tech{
    padding:80px 10%;
    text-align:center;
}

.tech h2{margin-bottom:30px;}

.tech-stack{
    display:flex;
    justify-content:center;
    gap:30px;
    flex-wrap:wrap;
}

.tech-item{
    background:var(--glass);
    border:1px solid var(--border);
    padding:15px;
    border-radius:15px;
    transition:.3s;
}

.tech-item img{
    width:40px;
}

.tech-item:hover{
    transform:translateY(-5px);
    box-shadow:0 10px 30px rgba(174,239,255,0.4);
}

/* FOOTER */
footer{
    text-align:center;
    padding:30px;
    color:#666;
}
</style>
</head>

<body>

<nav>
    <h3>Wondermayank ✨</h3>
    <div>
        <a href="#">Home</a>
        <a href="#tech">Tech</a>
    </div>
</nav>

<section class="hero">
    <h1>Digital Hub of Mayank</h1>
    <p>Explore my projects, tools and creative ecosystem in one place.</p>

    <!-- BOX BUTTONS -->
    <div class="action-boxes">
        <a href="#tech" class="action-box">
            <span>🚀</span>
            <h3>Launch Interface</h3>
        </a>

        <a href="https://github.com/wondermayank" target="_blank" class="action-box">
            <span>📂</span>
            <h3>GitHub Profile</h3>
        </a>
    </div>

    <!-- ECOSYSTEM IMAGE -->
    <div class="ecosystem">
        <img src="assets/ecosystem.png" alt="Ecosystem">
    </div>
</section>

<!-- TECH STACK -->
<section class="tech" id="tech">
    <h2>⚡ Tech Stack</h2>

    <div class="tech-stack">
        <div class="tech-item">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg">
            <p>HTML</p>
        </div>

        <div class="tech-item">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg">
            <p>CSS</p>
        </div>

        <div class="tech-item">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg">
            <p>JS</p>
        </div>

        <div class="tech-item">
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg">
            <p>GitHub</p>
        </div>
    </div>
</section>

<footer>
    © 2026 Wondermayank
</footer>

</body>
</html>
