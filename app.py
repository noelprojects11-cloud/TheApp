import streamlit as st
from pathlib import Path
from PIL import Image
import os
import base64



# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'python_correct' not in st.session_state:
    st.session_state.python_correct = False
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None
# Love meter counters
if 'hugs_count' not in st.session_state:
    st.session_state.hugs_count = 0
if 'laughs_count' not in st.session_state:
    st.session_state.laughs_count = 0
if 'days_count' not in st.session_state:
    st.session_state.days_count = 0


def page_1_photo_booth():
    import base64

    # 🔁 Path to your background image
    bg_image_path = "images/final.png"

    # Convert image to base64
    with open(bg_image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    # Fullscreen background + bottom-centered button
    st.markdown(
        f"""
        <style>
        /* Remove default padding */
        .block-container {{
            padding: 0;
        }}

        /* Fullscreen background image */
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: 80%;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}

        /* Container to push button to bottom center */
        .bottom-center {{
            position: fixed;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 9999;
        }}

        /* Button styling */
        .stButton > button {{
            font-size: 1.3rem;
            padding: 0.8rem 3rem;
            margin-left: 100px;
            border-radius: 30px;
            background-color: #ff4b6e;
            color: white;
            border: none;
        }}

        .stButton > button:hover {{
            background-color: #ff335a;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Push content to bottom
    st.markdown("<div style='height: 85vh;'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Start 💕"):
            st.session_state.page = 2
            st.rerun()

def page_2_python_interaction():


    import base64

    bg_image_path = "images/Background2.jpg"

    with open(bg_image_path, "rb") as img_file:
        encoded_bg = base64.b64encode(img_file.read()).decode()
    # =========================================================================
    # CSS
    # =========================================================================
    css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;1,400&family=Nunito:wght@400;600;700&display=swap');

:root {
    --rose:     #e91e63;
    --rose-lt:  #f06292;
    --rose-pale:#fce4ec;
    --cream:    #fff8f9;
    --ink:      #4a2040;
    --ink-soft: #7a5070;
    --gold:     #f9a825;
}

.ab-wrap { font-family: 'Nunito', sans-serif; color: var(--ink); }
.ab-wrap h1, .ab-wrap h2, .ab-wrap h3 { font-family: 'Playfair Display', serif; color: var(--rose); }

/* Full page background */
.stApp {
    background-image: url("data:image/png;base64,BG_IMAGE_HERE");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Soft overlay */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(255,255,255,0.85);
    z-index: -1;
}

/* hero */
.ab-hero {
    background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 40%, #fce4ec 100%);
    border-radius: 24px;
    padding: 48px 32px 40px;
    text-align: center;
    border: 2px solid #f8bbd0;
    box-shadow: 0 8px 30px rgba(233,30,99,.12);
}
.ab-hero h1 {
    font-size: 2.6em; margin: 0 0 6px;
    background: linear-gradient(135deg, var(--rose), #ad1457);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.ab-hero .ab-sub { font-size: 1.15em; color: var(--ink-soft); font-style: italic; margin: 0; }

/* section label */
.ab-label { display: flex; align-items: center; gap: 12px; margin: 36px 0 14px;width: 90%;max-width: 1100px; }
.ab-label .ab-line { flex: 1;height: 2.5px; background: linear-gradient(90deg, transparent, var(--rose-lt)); border-radius: 2px; }
.ab-label .ab-line.ab-r { background: linear-gradient(270deg, transparent, var(--rose-lt)); }
.ab-label span { font-family: 'Playfair Display', serif; font-size: 1.5em; color: var(--rose); white-space: nowrap; }

/* constellation map */
.ab-constellation {
    position: relative;
    background: linear-gradient(180deg, #1a0033 0%, #2d1155 50%, #1a0033 100%);
    border-radius: 20px;
    padding: 60px 40px;
    margin: 20px 0;
    min-height: 280px;
    overflow: hidden;
    box-shadow: inset 0 0 40px rgba(156,39,176,.3);
}
.ab-star {
    position: absolute;
    width: 38px; height: 38px;
    background: radial-gradient(circle, #fff, #ffd700);
    border-radius: 50%;
    box-shadow: 0 0 20px #ffd700, 0 0 35px rgba(255,215,0,.6);
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    cursor: pointer;
    transition: transform .3s, box-shadow .3s;
    animation: ab-twinkle 2s ease-in-out infinite;
}
.ab-star:hover {
    transform: scale(1.4);
    box-shadow: 0 0 30px #ffd700, 0 0 50px rgba(255,215,0,.8);
}
@keyframes ab-twinkle {
    0%, 100% { opacity: 1; }
    50% { opacity: .7; }
}
.ab-star-date {
    position: absolute;
    top: -28px; left: 50%;
    transform: translateX(-50%);
    background: linear-gradient(135deg, #ff1493, #ff69b4);
    color: white;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: .75em;
    font-weight: 700;
    white-space: nowrap;
    box-shadow: 0 4px 12px rgba(255,20,147,.4);
    animation: ab-date-flash 2s ease-in-out infinite;
}
@keyframes ab-date-flash {
    0%, 100% { transform: translateX(-50%) scale(1); }
    50% { transform: translateX(-50%) scale(1.08); }
}
.ab-star-label {
    position: absolute;
    top: 42px; left: 50%;
    transform: translateX(-50%);
    background: rgba(255,255,255,.95);
    color: var(--ink);
    padding: 4px 10px;
    border-radius: 10px;
    font-size: .72em;
    font-weight: 600;
    white-space: nowrap;
    pointer-events: none;
    opacity: 0;
    transition: opacity .3s;
}
.ab-star:hover .ab-star-label { opacity: 1; }

/* connecting lines */
.ab-constellation svg {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none;
}
.ab-constellation svg line {
    stroke: rgba(255,215,0,.35);
    stroke-width: 2;
    stroke-dasharray: 5,3;
}

/* love meter stats — CLICKABLE */
.ab-stats { display: flex; gap: 20px; margin: 20px 0; flex-wrap: wrap; }
.ab-stat {
    flex: 1 1 200px;
    background: var(--cream);
    border: 2px solid var(--rose-pale);
    border-radius: 16px;
    padding: 24px 20px;
    text-align: center;
    cursor: pointer;
    transition: transform .3s, box-shadow .3s, background .3s;
}
.ab-stat:hover {
    transform: translateY(-4px) scale(1.03);
    box-shadow: 0 8px 20px rgba(233,30,99,.2);
    background: linear-gradient(135deg, #fff9fc, var(--cream));
}
.ab-stat:active { transform: translateY(-2px) scale(1.05); }
.ab-stat .ab-stat-value {
    font-family: 'Playfair Display', serif;
    font-size: 2.2em;
    font-weight: 700;
    margin-bottom: 4px;
    background: linear-gradient(135deg, var(--rose), #ad1457);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    transition: transform .2s;
}
.ab-stat:active .ab-stat-value { transform: scale(1.15); }
.ab-stat .ab-stat-label {
    font-size: .95em;
    color: var(--ink-soft);
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 600;
}
.ab-stat .ab-stat-hint {
    font-size: .72em;
    color: var(--rose-lt);
    margin-top: 4px;
    font-style: italic;
}

/* 7 days of valentine — HORIZONTAL CAROUSEL */
.ab-cards-wrap {
    position: relative;
    padding: 20px 0;
    overflow: hidden;
}
.ab-cards {
    display: flex;
    gap: 20px;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding: 10px 5px 20px;
    scrollbar-width: thin;
    scrollbar-color: var(--rose-lt) var(--cream);
}
.ab-cards::-webkit-scrollbar { height: 8px; }
.ab-cards::-webkit-scrollbar-track { background: var(--cream); border-radius: 10px; }
.ab-cards::-webkit-scrollbar-thumb { background: var(--rose-lt); border-radius: 10px; }
.ab-cards::-webkit-scrollbar-thumb:hover { background: var(--rose); }

.ab-card-wrap {
    flex: 0 0 260px;
    min-width: 260px;
    perspective: 600px;
    cursor: pointer;
    scroll-snap-align: center;
}
.ab-card {
    position: relative;
    width: 100%;
    height: 340px;
    transition: transform .6s;
    transform-style: preserve-3d;
}
.ab-card-wrap:hover .ab-card { transform: rotateY(180deg); }

.ab-card-front, .ab-card-back {
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    border-radius: 16px;
    backface-visibility: hidden;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 18px rgba(233,30,99,.15);
    border: 2px solid #f8bbd0;
}
.ab-card-front {
    background: linear-gradient(145deg, #fff0f3, #fce4ec);
}
.ab-card-front .ab-cf-day {
    font-family: 'Playfair Display', serif;
    font-size: 1.8em;
    color: var(--rose);
    font-weight: 700;
    margin-bottom: 8px;
}
.ab-card-front .ab-cf-icon { font-size: 3.5em; margin-bottom: 12px; }
.ab-card-front .ab-cf-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.2em;
    color: var(--ink);
    font-weight: 600;
    margin-top: 8px;
}

.ab-card-back {
    background: linear-gradient(145deg, var(--rose), #c2185b);
    color: white;
    transform: rotateY(180deg);
}
.ab-card-back .ab-cb-text {
    font-family: 'Nunito', sans-serif;
    font-size: 1.05em;
    line-height: 1.6;
}

/* quiz */
.ab-quiz { background: var(--cream); border: 2px solid #f8bbd0; border-radius: 20px; padding: 28px 24px; box-shadow: 0 6px 20px rgba(233,30,99,.1); }
.ab-quiz h3 { margin-top: 0; font-size: 1.35em; }

/* gift boxes */
.ab-gifts { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 8px; }
.ab-gbox {
    flex: 1 1 140px; max-width: 200px;
    background: var(--cream);
    border: 2px dashed var(--rose-lt);
    border-radius: 18px; padding: 20px 12px; text-align: center;
    transition: box-shadow .3s, transform .2s;
}
.ab-gbox:hover { box-shadow: 0 4px 18px rgba(233,30,99,.2); transform: translateY(-2px); }
.ab-gbox .ab-gicon { font-size: 2.4em; margin-bottom: 6px; }
.ab-gbox .ab-gtitle { font-family: 'Playfair Display', serif; font-size: 1em; color: var(--rose); font-weight: 600; margin-bottom: 2px; }
.ab-gbox .ab-glock { font-size: .8em; color: var(--ink-soft); font-style: italic; }

/* coupon */
.ab-coupon {
    position: relative;
    background: linear-gradient(135deg, #fff9f0, #fff3e0);
    border: 2px solid var(--gold);
    border-radius: 16px;
    padding: 18px 22px 18px 28px;
    margin-top: 10px;
    box-shadow: 0 4px 16px rgba(249,168,37,.22);
}
.ab-coupon::before {
    content: '';
    position: absolute; left: -1px; top: 0; bottom: 0; width: 18px;
    background: radial-gradient(circle at 9px 9px, white 4px, transparent 4px);
    background-size: 18px 18px;
    background-color: var(--gold);
    border-radius: 16px 0 0 16px;
}
.ab-coupon .ab-c-tag {
    display: inline-block; background: var(--gold); color: white;
    font-size: .72em; font-weight: 700; padding: 2px 10px; border-radius: 20px;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;
}
.ab-coupon .ab-c-title { font-family: 'Playfair Display', serif; font-size: 1.15em; color: var(--ink); font-weight: 600; }
.ab-coupon .ab-c-desc { font-size: .88em; color: var(--ink-soft); margin-top: 3px; line-height: 1.45; }
.ab-coupon .ab-c-stamp { text-align: right; margin-top: 8px; font-size: .75em; color: var(--gold); font-style: italic; }

/* easter egg */
.ab-egg {
    background: linear-gradient(135deg, #e8eaf6, #ede7f6);
    border: 2px solid #ce93d8; border-radius: 18px;
    padding: 22px 24px; text-align: center;
    animation: ab-eggpulse 2s ease-in-out infinite;
}
@keyframes ab-eggpulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(156,39,176,.25); }
    50%      { box-shadow: 0 0 18px 4px rgba(156,39,176,.18); }
}
.ab-egg h3 { color: #7b1fa2 !important; margin: 0 0 6px; }
.ab-egg p  { color: #5e35b1; font-size: .95em; margin: 0; }

/* hint text */
.ab-hint { color: var(--ink-soft); font-size: .92em; margin: -4px 0 12px; }
</style>
"""


    # =========================================================================
    # SESSION STATE
    # =========================================================================
    st.markdown(css.replace("BG_IMAGE_HERE", encoded_bg), unsafe_allow_html=True)

    for k, v in {"q1_done": False, "q2_done": False, "rawr_egg": False, "gifts_opened": []}.items():
        if k not in st.session_state:
            st.session_state[k] = v

    # =========================================================================
    # DATA — edit anything here
    # =========================================================================

    # Constellation moments with dates
    CONSTELLATION = [
        {"icon": "✨", "label": "Heyy .........<br> Do we know each other", "date": "30th May", "x": "15%", "y": "20%"},
        {"icon": "💬", "label": "First Date", "date": "29th Aug", "x": "35%", "y": "15%"},
        {"icon": "😂", "label": "Day I fell(For you)", "date": "28th Oct", "x": "55%", "y": "25%"},
        {"icon": "💕", "label": "Ask Out ", "date": "17th Jan", "x": "75%", "y": "18%"},
        {"icon": "🌸", "label": "Valentine ask out <3", "date": "5th Feb", "x": "90%", "y": "22%"},
    ]

    # 7 Days of Valentine
    SEVEN_DAYS = [
        {"day": "Day 1", "icon": "🌹", "title": "Rose Day", "message": "Forecast: 90% precipitation chances of light rose showers to be seen anywhere Sanika goes… <br>→ A rose for my one and only gulab jaise pretty girl but you wont believe if i tell you this , will you ?"},
        {"day": "Day 2", "icon": "🧎🏻", "title": "Propose Day", "message": "Forecast: High liklihood of the promises made here to last forever, Grab on to your umbrellas.... <br>I propose that..... In all of our dates I do the dishes while you sit on the counter and yap to me. "},
        {"day": "Day 3", "icon": "🍫", "title": "Chocolate Day", "message": "Forecast: Heavy chocolate Cumulonimbus forming with a light drizzle of strawberries....<br>Ill get us all the types of chocolates there is until we find the best ones to make the best strawberry chocolates out there. "},
        {"day": "Day 4", "icon": "🧸", "title": "Teddy Day", "message": "Forecast: Very intense stormy weather with dark clouds(Perfect weather for fight with epic battle music in the background)…<br> On this day I'll need to fight all the teddies in my collection ancient Roman Colosseum style then finally fight yer pandu and whoever wins gets to be your cuddle partner."},
        {"day": "Day 5", "icon": "💐", "title": "Promise Day", "message": "Forecast: Initially sunshine with a chance of surprise cloudy annoyance later…<br>I promise to annoy you on your good days and make you laugh harder than ever on the bad ones (Annoy you later the same day ) "},
        {"day": "Day 6", "icon": "🫂", "title": "Hug Day", "message": "Forecast: Extreme Hot temperatures warning — Adviced to switch your AC to 16 degrees … You get a Lifetime subscription to the most elite hugs ( The only thing you would need to worry about is why you got my perfume all over you )"},
        {"day": "Day 7", "icon": "😘", "title": "Kiss Day", "message": "Forecast: A powerful storm of kisses is approaching your location. Expect sudden blushing, Wet face, and bite marks on yer face.. Authorities recommend accepting all kisses immediately 💋🚨 "},
        {"day": "Day 8", "icon": "💝", "title": "Valentine's Day", "message": "Forecast: 404 Error...... Will fix it soon , Maybe try solving the below problems to fix the Weather forecast system ..... Stay tuned we have Sanika our expert Python mechanic here "},
    ]

    GIFTS = [
        {"icon": "🎀💄", "title": " One Makeup Card",    "desc": "One Chance to display your makeup skills on me with ZERO COMPLAINS(Use this wisely)",                              "stamp": "— signed with love, and regrets of future noel"},
        {"icon": "📸", "title": "One Photo Booth session",  "desc": "We get a Photobooth Picture of ourselves TODAY(whenever redeemed)", "stamp": "— Expires: ASAP i want it soo bad rn"},
        {"icon": "(ง'̀-'́)ง", "title": "Annoyance Pass",   "desc": "A whole day of you getting to do whatever you want and I cant be annoyed/complain about it.",                               "stamp": "— The 24 hours gonna go by really slow im pretty sure"},
        {"icon": "📸", "title": "Gallery Pass",    "desc": "You get to choose 5 ugly ass pictures from my gallery and can send it to yourself.",                           "stamp": "— "}
        
    ]

    # =========================================================================
    # RENDER
    # =========================================================================

    st.markdown('<div class="ab-wrap">', unsafe_allow_html=True)

    # ── HERO ─────────────────────────────────────────────────────────────────
    st.markdown(
        '<div class="ab-hero">'
        '<h1>SURPRISEEEE <3 💕💕💕</h1>'
        '<p class="ab-sub">Nothing sus here obviously</p>'
        '</div>',
        unsafe_allow_html=True
    )

    # ── CONSTELLATION MAP ────────────────────────────────────────────────────
    st.markdown(
        '<div class="ab-label">'
        '<div class="ab-line"></div>'
        '<span>✨ Our Story in the Stars</span>'
        '<div class="ab-line ab-r"></div>'
        '</div>',
        unsafe_allow_html=True
    )

    # Build SVG lines
    lines_svg = '<svg>'
    for i in range(len(CONSTELLATION) - 1):
        x1 = CONSTELLATION[i]["x"]
        y1 = CONSTELLATION[i]["y"]
        x2 = CONSTELLATION[i + 1]["x"]
        y2 = CONSTELLATION[i + 1]["y"]
        lines_svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" />'
    lines_svg += '</svg>'

    # Build constellation HTML
    constellation_html = '<div class="ab-constellation">' + lines_svg
    for star in CONSTELLATION:
        constellation_html += (
            '<div class="ab-star" style="left:' + star["x"] + '; top:' + star["y"] + ';">'
            + '<div class="ab-star-date">' + star["date"] + '</div>'
            + star["icon"]
            + '<div class="ab-star-label">' + star["label"] + '</div>'
            + '</div>'
        )
    constellation_html += '</div>'
    st.markdown(constellation_html, unsafe_allow_html=True)



    # ── 7 DAYS OF VALENTINE (horizontal carousel) ───────────────────────────
    st.markdown(
        '<div class="ab-label">'
        '<div class="ab-line"></div>'
        '<span>💝 Weather Forecast for the next 8 Days</span>'
        '<div class="ab-line ab-r"></div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<p class="ab-hint">Hover over each day to see what it means to us ✨</p>', unsafe_allow_html=True)

    st.markdown('<div class="ab-cards-wrap"><div class="ab-cards">', unsafe_allow_html=True)
    for day_card in SEVEN_DAYS:
        st.markdown(
            '<div class="ab-card-wrap"><div class="ab-card">'
            + '<div class="ab-card-front">'
            + '<div class="ab-cf-day">' + day_card["day"] + '</div>'
            + '<div class="ab-cf-icon">' + day_card["icon"] + '</div>'
            + '<div class="ab-cf-title">' + day_card["title"] + '</div>'
            + '</div>'
            + '<div class="ab-card-back">'
            + '<div class="ab-cb-text">' + day_card["message"] + '</div>'
            + '</div>'
            + '</div></div>',
            unsafe_allow_html=True
        )
    st.markdown('</div></div>', unsafe_allow_html=True)

    # ── PYTHON QUIZ ──────────────────────────────────────────────────────────
    st.markdown(
        '<div class="ab-label">'
        '<div class="ab-line"></div>'
        '<span>🐍 A Little Python Game</span>'
        '<div class="ab-line ab-r"></div>'
        '</div>',
        unsafe_allow_html=True
    )
    st.markdown('<p class="ab-hint">Coz somehow Python is the thing that brings us together &lt;3</p>', unsafe_allow_html=True)
    st.markdown('<div class="ab-quiz">', unsafe_allow_html=True)

    # --- Q1 ---
    st.markdown('<h3>Question 1 — Fill in the blank</h3>', unsafe_allow_html=True)
    st.code('def message(name):\n    return f"I ____ you, Sanika!"\n\nprint(message("Valentine"))', language="python")

    answer_q1 = st.text_input("Think… what would I want you to say?", key="q1_input", placeholder="type here…")

    if answer_q1 and not st.session_state.q1_done:
        low = answer_q1.strip().lower()
        if low == "love":
            st.session_state.q1_done = True
            st.warning("It is the correct answer but there might be an even better one")
        elif low == "rawr":
            st.session_state.rawr_egg = True
            st.session_state.q1_done  = True
            st.warning("OMFG this is even better than the actual answer… I rawr you so much <3")
        elif low == "like":
            st.error("You think I would say *that* to you? pffffft, cmon ")
        else:
            st.error("Not exactly… but try again, koi na, you get all the tries you want 💕")

    if st.session_state.q1_done:
        st.success("✅ Correct! 💕")

    st.markdown("---")

    # --- Q2 ---
    st.markdown('<h3>Question 2 — About Us</h3>', unsafe_allow_html=True)
    st.code('def us():\n    while ( We are out on a date and you drop a glass):\n        return Whose Fault Is it ', language="python")

    answer_q2 = st.text_input("What does this function return?", key="q2_input", placeholder="type the output…")

    if answer_q2 and not st.session_state.q2_done:
        if "noeh" in answer_q2.lower() :
            st.session_state.q2_done = True
        else:
            st.error("Whatever happens its _____ fault 😉")

    if st.session_state.q2_done:
        st.success("✅ Exactly chal now since im yours, its your fault too . 💕")

    st.markdown('</div>', unsafe_allow_html=True)

    # ── GIFT BOXES ───────────────────────────────────────────────────────────
    quiz_done      = st.session_state.q1_done and st.session_state.q2_done
    opened         = st.session_state.gifts_opened
    unlocked_count = min(len(opened) + 1, len(GIFTS)) if quiz_done else 0

    st.markdown(
        '<div class="ab-label">'
        '<div class="ab-line"></div>'
        '<span>🎁 Your Surprise Gifts</span>'
        '<div class="ab-line ab-r"></div>'
        '</div>',
        unsafe_allow_html=True
    )

    if not quiz_done:
        st.markdown('<p class="ab-hint">Answer the quiz above to start unlocking gifts… 🔐</p>', unsafe_allow_html=True)

    # locked placeholders
    st.markdown('<div class="ab-gifts">', unsafe_allow_html=True)
    for idx in range(len(GIFTS)):
        if idx < unlocked_count:
            continue
        st.markdown(
            '<div class="ab-gbox" style="opacity:.45; filter:blur(1px);">'
            + '<div class="ab-gicon">🔒</div>'
            + '<div class="ab-gtitle" style="color:#aaa;">Gift #' + str(idx + 1) + '</div>'
            + '<div class="ab-glock">locked</div>'
            + '</div>',
            unsafe_allow_html=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # unlocked interactive gifts
    if quiz_done:
        cols = st.columns(min(unlocked_count, 5))
        for idx in range(unlocked_count):
            g = GIFTS[idx]
            with cols[idx % len(cols)]:
                if idx in opened:
                    st.markdown(
                        '<div class="ab-coupon">'
                        + '<span class="ab-c-tag">Gift #' + str(idx + 1) + ' Unlocked</span>'
                        + '<div class="ab-c-title">' + g["icon"] + ' ' + g["title"] + '</div>'
                        + '<div class="ab-c-desc">' + g["desc"] + '</div>'
                        + '<div class="ab-c-stamp">' + g["stamp"] + '</div>'
                        + '</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        '<div class="ab-gbox">'
                        + '<div class="ab-gicon">' + g["icon"] + '</div>'
                        + '<div class="ab-gtitle">' + g["title"] + '</div>'
                        + '<div class="ab-glock">tap to open</div>'
                        + '</div>',
                        unsafe_allow_html=True
                    )
                    if st.button("Open Gift #" + str(idx + 1) + " 🎀", key="open_gift_" + str(idx), use_container_width=True):
                        st.session_state.gifts_opened.append(idx)
                        st.snow()
                        st.toast(g["title"] + " unlocked! 🎉", icon="🎁")
                        st.rerun()

    # ── EASTER EGG ───────────────────────────────────────────────────────────
    if st.session_state.rawr_egg:
        st.markdown(
            '<div class="ab-egg">'
            '<h3>🐣 Secret Easter Egg Unlocked!</h3>'
            '<p>You typed <b>rawr</b>… You have unlocked the hidden easter egg of this message <br>'
            'I rawr you Smmmm tooo Sanikaa.<br><br>'
            '🐉<em> This secret coupon is yours : One rawr = Massage your feet/Shoulders <3 </em>🐉</p>'
            '</div>',
            unsafe_allow_html=True
        )

    # ── CONTINUE ─────────────────────────────────────────────────────────────
    all_open = len(st.session_state.gifts_opened) >= len(GIFTS)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if all_open:
            if st.button("Continue 💕", use_container_width=True, key="cont_btn"):
                st.session_state.page = 3
                st.rerun()
        else:
            remaining = len(GIFTS) - len(st.session_state.gifts_opened)
            label = "🔒  Open " + str(remaining) + " more gift" + ("s" if remaining != 1 else "") + " first"
            st.button(label, disabled=True, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# PAGE 3: FINAL QUESTION - EPIC VERSION
# ============================================================================
def page_3_final_question():
    import random
    import base64

    bg_image_path = r"images/final3.jpg"

    with open(bg_image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()

    if "no_offset" not in st.session_state:
        st.session_state.no_offset = 0

    if "said_yes" not in st.session_state:
        st.session_state.said_yes = False

    st.markdown(f"""
    <style>

    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
    }}

    .question {{
        font-size: 4em;
        color: #ff1744;
        text-align: center;
        margin-top: 150px;
        margin-bottom: 60px;
        font-family: cursive;
    }}

    .stButton > button {{
        font-size: 1.3rem;
        padding: 1rem 3rem;
        border-radius: 30px;
        background:#ff4b6e;
        color:white;
        border:none;
    }}

    </style>
    """, unsafe_allow_html=True)

    # YES SCREEN
    if st.session_state.said_yes:
        st.balloons()
        st.markdown("<h1 style='text-align:center;'>She Said YES 💖</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>LESGOOOOOOOOOOOO FINALLLLY You Mah Valentine ab, Cant say No ab 😌 <br> Get Ready for the Best Valentines day EVER !!!!!!</p", unsafe_allow_html=True)

        if st.button("Start Over"):
            st.session_state.page = 1
            st.session_state.said_yes = False
            st.rerun()
        return

    # QUESTION
    st.markdown("""
    <div class="question">
        Will You Be My Valentine Sanika ? 💝
    </div>
    """, unsafe_allow_html=True)

    # CENTER BUTTONS
    col1, col2, col3 = st.columns([2,1,2])

    with col2:
        if st.button("💖 YES! 💖"):
            st.session_state.said_yes = True
            st.rerun()

    import random

    ROWS = 3
    COLS = 5

    # Init position
    if "no_row" not in st.session_state:
        st.session_state.no_row = random.randint(0, ROWS - 1)

    if "no_col" not in st.session_state:
        st.session_state.no_col = random.randint(0, COLS - 1)

    # Build grid
    for r in range(ROWS):
        cols = st.columns(COLS)
        for c in range(COLS):

            # Only place NO button in the chosen cell
            if r == st.session_state.no_row and c == st.session_state.no_col:
                with cols[c]:
                    if st.button("😢 NO", key=f"no_{r}_{c}"):
                        st.session_state.no_row = random.randint(0, ROWS - 1)
                        st.session_state.no_col = random.randint(0, COLS - 1)
    # BACK
    if st.button("← Back"):
        st.session_state.page = 2
        st.rerun()
# ============================================================================
# MAIN APP LOGIC
# ============================================================================
def main():
    """Main application router"""
    
    # Route to appropriate page based on session state
    if st.session_state.page == 1:
        page_1_photo_booth()
    elif st.session_state.page == 2:
        page_2_python_interaction()
    elif st.session_state.page == 3:
        page_3_final_question()


# Run the app
if __name__ == "__main__":

    main()












