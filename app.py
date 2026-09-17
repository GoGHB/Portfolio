import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Shubhanshu Singh | ML Engineer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# STREAMLIT CSS
# ============================================================

st.markdown("""
<style>
    html, body, [class*="css"] {
        margin: 0;
        padding: 0;
    }

    .stApp {
        background: #12161D;
    }

    [data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stToolbar"] {
        display: none;
    }

    [data-testid="stDecoration"] {
        display: none;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 100%;
        padding: 0;
        margin: 0;
    }

    footer {
        display: none;
    }

    iframe {
        width: 100% !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# VIDEO
# ============================================================

video_path = Path("1000009006.mp4")

video_url = ""

if video_path.exists():
    try:
        video_bytes = video_path.read_bytes()
        video_base64 = base64.b64encode(video_bytes).decode("utf-8")
        video_url = f"data:video/mp4;base64,{video_base64}"
    except Exception:
        video_url = ""

# ============================================================
# PORTFOLIO HTML
# ============================================================

portfolio_html = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Shubhanshu Singh — Aspiring ML Engineer</title>

<link rel="preconnect"
      href="https://fonts.googleapis.com">

<link rel="preconnect"
      href="https://fonts.gstatic.com"
      crossorigin>

<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@400;500;600;700&display=swap"
      rel="stylesheet">

<style>

:root {{
    --ink:#12161D;
    --ink-2:#1B2129;
    --paper:#F3F1E9;
    --paper-dim:#A9A79A;
    --amber:#E8B339;
    --steel:#6E9CC4;
    --green:#8FB98F;
    --line:rgba(243,241,233,0.12);
    --max-w:1100px;
}}

* {{
    box-sizing:border-box;
}}

html {{
    scroll-behavior:smooth;
    height:100%;
}}

html, body {{
    margin:0;
    height:100%;
    overflow:hidden;
}}

body {{
    background:var(--ink);
    color:var(--paper);
    font-family:'Inter',sans-serif;
    line-height:1.6;
    -webkit-font-smoothing:antialiased;
}}

#page-scroll {{
    position:relative;
    z-index:1;
    height:100%;
    overflow-y:auto;
    overflow-x:hidden;
    -webkit-overflow-scrolling:touch;
    scroll-behavior:smooth;
}}

#video-bg {{
    position:fixed;
    inset:0;
    z-index:0;
    overflow:hidden;
    pointer-events:none;
    background:var(--ink);
}}

#video-bg video {{
    position:absolute;
    top:50%;
    left:50%;
    width:100%;
    height:100%;
    object-fit:cover;
    transform:translate(-50%, -50%);
    opacity:0.25;
}}

#video-bg::after {{
    content:"";
    position:absolute;
    inset:0;
    background:
        linear-gradient(
            180deg,
            rgba(18,22,29,0.85) 0%,
            rgba(18,22,29,0.65) 45%,
            rgba(18,22,29,0.95) 100%
        );
}}

header {{
    position:sticky;
    top:0;
    z-index:10;
    background:rgba(18,22,29,0.92);
    backdrop-filter:blur(8px);
    border-bottom:1px solid var(--line);
}}

.nav-row {{
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:16px 28px;
    max-width:var(--max-w);
    margin:0 auto;
}}

.nav-mark {{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.95rem;
    color:var(--paper);
}}

.nav-mark span {{
    color:var(--amber);
}}

.cursor {{
    animation:blink 1.1s steps(1) infinite;
}}

@keyframes blink {{
    0%,49% {{opacity:1;}}
    50%,100% {{opacity:0;}}
}}

nav ul {{
    list-style:none;
    display:flex;
    gap:22px;
    margin:0;
    padding:0;
    font-family:'IBM Plex Mono',monospace;
    font-size:0.85rem;
}}

nav a {{
    color:var(--paper-dim);
    text-decoration:none;
}}

nav a:hover {{
    color:var(--amber);
}}

.wrap {{
    max-width:var(--max-w);
    margin:0 auto;
    padding:0 28px;
}}

.hero {{
    padding:90px 0 70px;
}}

.hero-grid {{
    display:grid;
    grid-template-columns:1.15fr 0.85fr;
    gap:44px;
    align-items:center;
}}

.prompt-line {{
    font-family:'IBM Plex Mono',monospace;
    color:var(--green);
    font-size:0.85rem;
    margin:0 0 18px;
}}

.prompt-line::before {{
    content:"$ ";
    color:var(--paper-dim);
}}

h1 {{
    font-family:'IBM Plex Mono',monospace;
    font-weight:600;
    font-size:clamp(2rem,5vw,3.2rem);
    line-height:1.2;
    margin:0 0 8px;
}}

.role {{
    font-family:'IBM Plex Mono',monospace;
    color:var(--steel);
    font-size:1.05rem;
    margin:0 0 24px;
}}

.summary {{
    max-width:60ch;
    font-size:1.03rem;
    margin:0 0 30px;
}}

.term-card {{
    background:rgba(27,33,41,0.92);
    border:1px solid var(--line);
    box-shadow:0 30px 60px -30px rgba(0,0,0,0.6);
}}

.term-bar {{
    display:flex;
    align-items:center;
    gap:8px;
    padding:10px 14px;
    border-bottom:1px solid var(--line);
}}

.dot {{
    width:9px;
    height:9px;
    border-radius:50%;
}}

.dot.r {{
    background:#E8746B;
}}

.dot.y {{
    background:var(--amber);
}}

.dot.g {{
    background:var(--green);
}}

.term-title {{
    margin-left:8px;
    font-family:'IBM Plex Mono',monospace;
    font-size:0.75rem;
    color:var(--paper-dim);
}}

.term-body {{
    margin:0;
    padding:18px 16px;
    font-family:'IBM Plex Mono',monospace;
    font-size:0.83rem;
    line-height:1.9;
}}

.tk {{
    color:var(--steel);
}}

.tv {{
    color:var(--amber);
}}

.tc {{
    color:var(--paper-dim);
}}

.contact-row {{
    display:flex;
    flex-wrap:wrap;
    gap:18px;
}}

.contact-row a {{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width:42px;
    height:42px;
    border:1px solid var(--line);
    color:var(--paper-dim);
    transition:0.2s;
}}

.contact-row a:hover {{
    color:var(--amber);
    border-color:var(--amber);
}}

.contact-row svg {{
    width:19px;
    height:19px;
    fill:none;
    stroke:currentColor;
    stroke-width:1.6;
}}

section:not(.hero) {{
    border-top:1px solid var(--line);
}}

section {{
    padding:60px 0;
}}

.def-label {{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.95rem;
    color:var(--paper-dim);
    margin:0 0 30px;
}}

.def-label .kw {{
    color:var(--steel);
}}

.def-label .fn {{
    color:var(--amber);
}}

.entry {{
    margin-bottom:30px;
    padding-left:20px;
    border-left:2px solid var(--line);
}}

.entry-head {{
    display:flex;
    justify-content:space-between;
    align-items:baseline;
    flex-wrap:wrap;
    gap:6px 14px;
}}

.entry-title {{
    font-weight:600;
    font-size:1.05rem;
}}

.entry-org {{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.82rem;
    color:var(--paper-dim);
}}

.entry ul {{
    margin:8px 0 0;
    padding-left:18px;
    color:var(--paper-dim);
}}

.entry li::marker {{
    color:var(--amber);
}}

.proj-grid {{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:16px;
}}

.proj {{
    position:relative;
    border:1px solid var(--line);
    padding:22px 20px 20px;
    background:rgba(27,33,41,0.92);
    transition:0.2s;
}}

.proj:hover {{
    border-color:var(--amber);
    transform:translateY(-3px);
}}

.proj-tag {{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.72rem;
    color:var(--green);
    margin:0 0 10px;
}}

.proj h3 {{
    margin:0 0 8px;
    font-size:1.02rem;
}}

.proj p {{
    margin:0;
    font-size:0.9rem;
    color:var(--paper-dim);
}}

.proj-link {{
    display:inline-block;
    margin-top:12px;
    font-family:'IBM Plex Mono',monospace;
    font-size:0.82rem;
    color:var(--amber);
    text-decoration:none;
}}

.proj-link:hover {{
    text-decoration:underline;
}}

.skill-row {{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
}}

.skill-pill {{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.85rem;
    padding:7px 14px;
    border:1px solid var(--line);
    color:var(--paper);
}}

.skill-pill .sym {{
    color:var(--amber);
    margin-right:8px;
}}

.edu-entry {{
    display:flex;
    justify-content:space-between;
    align-items:baseline;
    flex-wrap:wrap;
    gap:4px 14px;
    padding:12px 0;
    border-bottom:1px solid var(--line);
}}

.edu-name {{
    color:var(--paper);
    font-size:0.98rem;
}}

.edu-meta {{
    font-family:'IBM Plex Mono',monospace;
    font-size:0.82rem;
    color:var(--paper-dim);
    text-align:right;
}}

.ach {{
    font-size:0.98rem;
    color:var(--paper-dim);
    padding-left:20px;
    position:relative;
}}

.ach::before {{
    content:"✓";
    position:absolute;
    left:0;
    color:var(--green);
}}

footer {{
    padding:44px 0 64px;
    font-family:'IBM Plex Mono',monospace;
    font-size:0.8rem;
    color:var(--paper-dim);
    border-top:1px solid var(--line);
}}

.footer-row {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    flex-wrap:wrap;
    gap:10px;
}}

.to-top {{
    color:var(--paper-dim);
    text-decoration:none;
}}

@media (max-width:720px) {{

    .hero-grid {{
        grid-template-columns:1fr;
    }}

    nav ul {{
        gap:10px;
        font-size:0.72rem;
    }}

    .nav-row {{
        padding:14px 18px;
    }}

    .wrap {{
        padding:0 18px;
    }}
}}

@media (max-width:600px) {{

    .proj-grid {{
        grid-template-columns:1fr;
    }}
}}

</style>

</head>

<body>

<!-- ========================================================
     IFRAME AUTO-RESIZE (matches real browser height so the
     fixed video never scrolls with the outer Streamlit page)
========================================================= -->

<script>
(function() {{
  function resizeFrame() {{
    try {{
      var iframes = window.parent.document.querySelectorAll('iframe');
      var targetHeight = window.parent.innerHeight;
      for (var i = 0; i < iframes.length; i++) {{
        if (iframes[i].contentWindow === window) {{
          iframes[i].style.height = targetHeight + 'px';
          break;
        }}
      }}
    }} catch (e) {{}}
  }}
  window.addEventListener('resize', resizeFrame);
  resizeFrame();
  setTimeout(resizeFrame, 300);
}})();
</script>

<!-- ========================================================
     BACKGROUND VIDEO
========================================================= -->

<div id="video-bg">

<video
    autoplay
    muted
    loop
    playsinline
    preload="auto"
    aria-hidden="true">

    <source
        src="{video_url}"
        type="video/mp4">

</video>

</div>

<!-- ========================================================
     SCROLLABLE PAGE WRAPPER (video-bg stays outside this,
     so it is truly fixed and never scrolls with content)
========================================================= -->

<div id="page-scroll">

<!-- ========================================================
     HEADER
========================================================= -->

<header id="top">

<div class="nav-row">

<div class="nav-mark">
    shubhanshu<span>.py</span>
    <span class="cursor">_</span>
</div>

<nav>

<ul>

<li>
<a href="#experience">
experience
</a>
</li>

<li>
<a href="#projects">
projects
</a>
</li>

<li>
<a href="#skills">
skills
</a>
</li>

<li>
<a href="#education">
education
</a>
</li>

</ul>

</nav>

</div>

</header>

<!-- ========================================================
     MAIN
========================================================= -->

<main class="wrap">

<!-- HERO -->

<section class="hero">

<div class="hero-grid">

<div>

<p class="prompt-line">
whoami
</p>

<h1>
Shubhanshu Singh
</h1>

<p class="role">
Aspiring ML Engineer
</p>

<p class="summary">

Python developer building a foundation in machine learning —
regression models, data preprocessing, and applied ML projects
like an AI-assisted diagnosis system. Currently strengthening
skills in TensorFlow, Pandas, NumPy, and SciPy while working
toward an ML Engineer role.

</p>

<div class="contact-row">

<!-- MAIL -->

<a
href="mailto:shubhanshusingh@zohomail.in"
aria-label="Email">

<svg viewBox="0 0 24 24">

<rect
x="2"
y="4"
width="20"
height="16"
rx="2"/>

<path
d="m3 6 9 7 9-7"/>

</svg>

</a>

<!-- GITHUB -->

<a
href="https://github.com/GoGHB"
target="_blank"
rel="noopener"
aria-label="GitHub">

<svg viewBox="0 0 24 24">

<path
d="M12 2C6.48 2 2 6.58 2 12.24c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49v-1.7c-2.78.62-3.37-1.22-3.37-1.22-.46-1.2-1.11-1.52-1.11-1.52-.91-.64.07-.63.07-.63 1.01.08 1.54 1.06 1.54 1.06.9 1.58 2.35 1.12 2.92.86.09-.67.35-1.12.64-1.38-2.22-.26-4.55-1.15-4.55-5.08 0-1.12.39-2.04 1.03-2.76-.1-.26-.45-1.31.1-2.73 0 0 .84-.27 2.75 1.05A9.16 9.16 0 0 1 12 6.1c.85 0 1.7.12 2.49.36 1.91-1.32 2.75-1.05 2.75-1.05.55 1.42.2 2.47.1 2.73.64.72 1.03 1.64 1.03 2.76 0 3.94-2.34 4.82-4.57 5.07.36.32.68.94.68 1.9v2.81c0 .27.18.59.69.49A10.25 10.25 0 0 0 22 12.24C22 6.58 17.52 2 12 2z"/>

</svg>

</a>

<!-- INSTAGRAM -->

<a
href="https://www.instagram.com/shubhanshu_s0/"
target="_blank"
rel="noopener"
aria-label="Instagram">

<svg viewBox="0 0 24 24">

<rect
x="2"
y="2"
width="20"
height="20"
rx="5"/>

<circle
cx="12"
cy="12"
r="4"/>

<circle
cx="17.5"
cy="6.5"
r="1"
fill="currentColor"
stroke="none"/>

</svg>

</a>

<!-- LINKEDIN -->

<a
href="https://www.linkedin.com/in/shubhanshu-singh-12b174421/"
target="_blank"
rel="noopener"
aria-label="LinkedIn">

<svg viewBox="0 0 24 24">

<path
d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/>

<rect
x="2"
y="9"
width="4"
height="12"/>

<circle
cx="4"
cy="4"
r="2"/>

</svg>

</a>

</div>

</div>

<!-- TERMINAL -->

<div class="term-card">

<div class="term-bar">

<span class="dot r"></span>
<span class="dot y"></span>
<span class="dot g"></span>

<span class="term-title">
about.py
</span>

</div>

<pre class="term-body"><code>

<span class="tk">name</span>   =
<span class="tv">"Shubhanshu Singh"</span>

<span class="tk">goal</span>   =
<span class="tv">"ML Engineer"</span>

<span class="tk">stack</span>  =
[
<span class="tv">"Python"</span>,
<span class="tv">"TensorFlow"</span>,
<span class="tv">"Pandas"</span>,
<span class="tv">"NumPy"</span>
]

<span class="tk">status</span> =
<span class="tv">"building & learning"</span>

<span class="tc"># open to ML / Python roles</span>

</code></pre>

</div>

</div>

</section>

<!-- ========================================================
     EXPERIENCE
========================================================= -->

<section id="experience">

<p class="def-label">

<span class="kw">def</span>
<span class="fn"> experience</span>():

</p>

<div class="entry">

<div class="entry-head">

<span class="entry-title">
Python Intern
</span>

<span class="entry-org">
IBM Watson Studio (AKTU)
</span>

</div>

<ul>

<li>
Worked on machine learning projects using IBM Watson Studio
</li>

<li>
Developed a salary prediction system using regression techniques
</li>

<li>
Implemented a Random Forest Regression model for data prediction
</li>

<li>
Gained hands-on experience in data preprocessing and model building
</li>

</ul>

</div>

<div class="entry">

<div class="entry-head">

<span class="entry-title">
Python Trainee
</span>

<span class="entry-org">
College Training — 1st Year
</span>

</div>

<ul>

<li>
Learned core Python concepts including functions, OOP, and data structures
</li>

<li>
Built basic applications, including a calculator, using Python
</li>

<li>
Developed problem-solving skills through coding exercises
</li>

</ul>

</div>

</section>

<!-- ========================================================
     PROJECTS
========================================================= -->

<section id="projects">

<p class="def-label">

<span class="kw">def</span>
<span class="fn"> projects</span>():

</p>

<div class="proj-grid">

<div class="proj">

<p class="proj-tag">
# hackathon — U Hack
</p>

<h3>
AI-Powered Diagnosis System
</h3>

<p>

A healthcare-based system that analyses MRI, CT scan,
and X-ray images to assist in early disease detection
using AI concepts. Built with a team under hackathon
time pressure.

</p>

</div>

<div class="proj">

<p class="proj-tag">
# machine learning
</p>

<h3>
Salary Prediction System
</h3>

<p>

A regression-based ML model that predicts salaries
from input data, covering data analysis and preprocessing
end to end.

</p>

<a
class="proj-link"
href="https://salarypredictionmodel-yj4ewpbsigtz3nccxchpmn.streamlit.app/"
target="_blank"
rel="noopener">

View live app →

</a>

</div>

<div class="proj">

<p class="proj-tag">
# machine learning — NLP
</p>

<h3>
Fake News Detector
</h3>

<p>

A text classification app that predicts whether a news
article is real or fake, deployed as a live web app.

</p>

<a
class="proj-link"
href="https://fakenewsdetection-qkaymoxsicsu2yytuaxbgu.streamlit.app/"
target="_blank"
rel="noopener">

View live app →

</a>

</div>

<div class="proj">

<p class="proj-tag">
# event — Gyan Manthan, UIM
</p>

<h3>
Travel Website
</h3>

<p>

A responsive travel website built with HTML,
focused on UI/UX and clean layout structuring.

</p>

</div>

<div class="proj">

<p class="proj-tag">
# fundamentals
</p>

<h3>
Basic Calculator
</h3>

<p>

A simple Python calculator implementing arithmetic
operations and user input handling.

</p>

</div>

</div>

</section>

<!-- ========================================================
     SKILLS
========================================================= -->

<section id="skills">

<p class="def-label">

<span class="kw">def</span>
<span class="fn"> skills</span>():

</p>

<div class="skill-row">

<span class="skill-pill">
<span class="sym">&gt;&gt;&gt;</span>
Python with OOP
</span>

<span class="skill-pill">
<span class="sym">∇</span>
TensorFlow
</span>

<span class="skill-pill">
<span class="sym">▤</span>
Pandas
</span>

<span class="skill-pill">
<span class="sym">∑</span>
NumPy
</span>

<span class="skill-pill">
<span class="sym">∫</span>
SciPy
</span>

<span class="skill-pill">
<span class="sym">▦</span>
PostgreSQL
</span>

<span class="skill-pill">
<span class="sym">()=&gt;</span>
JavaScript
</span>

<span class="skill-pill">
<span class="sym">&lt;/&gt;</span>
HTML
</span>

<span class="skill-pill">
<span class="sym">{{ }}</span>
CSS
</span>

</div>

</section>

<!-- ========================================================
     EDUCATION
========================================================= -->

<section id="education">

<p class="def-label">

<span class="kw">def</span>
<span class="fn"> education</span>():

</p>

<div class="edu-entry">

<span class="edu-name">

B.Tech, Computer Science &amp; Engineering
(AIML) — United College of Engineering and Research,
Prayagraj

</span>

<span class="edu-meta">
2026 – Present · CGPA 6.13/10
</span>

</div>

<div class="edu-entry">

<span class="edu-name">

12th Standard — Raja Kamlakatr Inter College,
Shankargarh

</span>

<span class="edu-meta">
2021 · 79%
</span>

</div>

<div class="edu-entry">

<span class="edu-name">

10th Standard — Raja Kamlakatr Inter College,
Shankargarh

</span>

<span class="edu-meta">
2019 · 70%
</span>

</div>

</section>

<!-- ========================================================
     ACHIEVEMENTS
========================================================= -->

<section id="achievements">

<p class="def-label">

<span class="kw">def</span>
<span class="fn"> achievements</span>():

</p>

<p class="ach">

Successfully completed a Python Training Program
covering core programming concepts

</p>

</section>

</main>

<!-- ========================================================
     FOOTER
========================================================= -->

<footer>

<div class="wrap footer-row">

<span>
© 2026 Shubhanshu Singh
</span>

<a
class="to-top"
href="#top">

↑ back to top

</a>

</div>

</footer>

</div><!-- /#page-scroll -->

</body>

</html>
"""

# ============================================================
# RENDER PORTFOLIO
# ============================================================

components.html(
    portfolio_html,
    height=800,
    scrolling=False
)