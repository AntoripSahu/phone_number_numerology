import streamlit as st
import time


# ---------- CONSTANTS & CONFIG ----------

MASTER_NUMBERS = {11, 22, 33}

st.set_page_config(page_title="📲 Phone Number Numerology", layout="centered")

# ---------- STYLES ----------
st.markdown("""
    <style>

        .sum-box {
            padding: 1em;
            border: 1px solid #ccc;
            border-radius: 10px;
            margin: 1em 0;
            background: #f9f9ff;
            font-family: monospace;
        }

        .sum-title {
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 0.5em;
        }

        .master-inline {
            color: #a64ac9;
            font-weight: bold;
            background-color: #fff8e1;
            border: 2px dashed orange;
            border-radius: 8px;
            padding: 0.5em;
            margin: 0.5em 0;
        }

        .master-highlight {
            background-color: #e1bee7;
            padding: 2px 6px;
            border-radius: 6px;
            font-weight: bold;
        }

        .final-single {
            margin-top: 0.8em;
            font-size: 1.1em;
            color: #1a237e;
            font-weight: bold;
        }

        .input-wrapper {
            display: flex;
            align-items: center;
            border: 3px solid red;
            border-radius: 10px;
            background-color: white;
            padding: 10px 14px;
            font-size: 24px;
            letter-spacing: 2px;
            width: 100%;
            margin-bottom: 8px;
        }

        .input-wrapper.valid {
            border-color: green !important;
        }
            
        .input-wrapper.invalid {
            border-color: red !important;
        }
        
        .input-wrapper.all-zero {
            border-color: gray !important;
        }

        .prefix {
            color: #000;
            margin-right: 6px;
            font-weight: bold;
        }

        input.digit-display {
            background-color: #f5f5f5;
            border: none;
            outline: none;
            font-size: 24px;
            letter-spacing: 2px;
            flex: 1;
            padding: 6px;
        }

        .char-count {
            text-align: right;
            color: #888;
            font-size: 14px;
            margin-bottom: 20px;
        }

        .char-count.valid {
            color: green;
            font-weight: bold;
        }
            
        .char-count.invalid {
            color: red;
            font-weight: bold;
        }
            
        .char-count.all-zero {
            color: gray;
            font-weight: bold;
        }

        .digit-slots {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin: 12px 0 6px;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 2px;
        }

        .digit-slot {
            width: 32px;
            height: 38px;
            text-align: center;
            border-bottom: 2px solid #ccc;
        }

        .digit-slot-pointer {
            width: 32px;
            height: 38px;
            text-align: center;
        }

        .digit-labels {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-bottom: 10px;
            font-size: 12px;
            color: #999;
            letter-spacing: 1px;
        }

        .sum-box {
            background: #f8f9fa;
            padding: 18px;
            border-radius: 12px;
            margin-bottom: 20px;
            border-left: 6px solid #636efa;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            position: relative;
        }

        .master-inline {
            background-color: #fff8e1;
            border: 2px dashed #ffa500;
            padding: 8px;
            margin-top: 10px;
            border-radius: 10px;
            font-weight: 500;
            font-size: 14px;
            color: #000;
        }
            
        .master-chip {
            background-color: #e6d6f5;
            color: #4b0082;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 4px;
        }

        .sum-title {
            font-weight: 700;
            font-size: 18px;
            color: #222;
            margin-bottom: 6px;
        }

        .sum-digits {
            font-family: monospace;
            color: #444;
            font-size: 16px;
        }

        .tooltip {
            color: #f44336;
            font-size: 13px;
            margin-top: -8px;
            margin-bottom: 10px;
            text-align: center;
        }

        .final-single {
            margin-top: 0.8em;
            font-size: 1.1em;
            color: #1a237e;
            font-weight: bold;
        }
            
        /* By default, hide the floating box */
        .floating-box-left {
            display: none;
        }
            
        /* Only show floating-box-left on desktop */
         @media screen and (min-width: 1081px) {
            .floating-box-left {
                position: fixed;
                top: 50%;
                left: 20px;
                transform: translateY(-50%);
                z-index: 9999;
                display: flex;
                flex-direction: column;
                gap: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                will-change: transform;
            
                /* This centers vertically */
                transform: translateY(-50%);
            
                /* The magic: animation */
                animation: floaty 3s ease-in-out infinite;
            }



            @keyframes floaty {
                0%, 100% {
                    transform: translateY(calc(-50% + 0px));
                }
                50% {
                    transform: translateY(calc(-50% + -5px));
                }
            }


            .floating-layer {
                background-color: #f4f4f4;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.15);
                padding: 12px;
                width: 160px;
                text-align: center;
            }

            .floating-layer button {
                background-color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 8px;
                margin: 4px 0;
                width: 100%;
                cursor: pointer;
                font-weight: 600;
                color: #333;
                transition: all 0.2s ease;
            }

            .floating-layer button:hover {
                background-color: #dcdcdc;
                cursor: default;
            }
        }
            
        @keyframes shimmer {
            0%, 100% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.05); opacity: 0.92; }
        }
            
        .blackhole {
            animation: shimmer 4s ease-in-out infinite;
        }
            
        /* Light theme highlight */
        @media (prefers-color-scheme: light) {
            .highlight-slot {
                background-color: #cce5ff; /* soft sky blue */
                color: #000;               
                font-weight: bold;
            }
        }

        /* Dark theme highlight */
        @media (prefers-color-scheme: dark) {
            .highlight-slot {
                background-color: #3399ff; /* stronger blue for contrast */
                color: #fff;               
                font-weight: bold;
            }
        }

    </style>
           
    <div class="floating-box-left">
        <div class="floating-layer">
            <button style="
                background-color: #dcdcdc;
                display: flex;
                align-items: center; /* center emoji vertically */
                padding: 12px;
                height: 60px
                ">
                <!-- Left column: planet emoji -->
                <div style="display: flex; align-items: center; justify-content: center; flex: 0 0 auto; width: 30px;">
                    <span style="font-size: 1.5em;">🪐</span>
                </div>
                <!-- Right column: stacked text -->
                <div style="display: flex; flex-direction: column; line-height: 1.5; margin-left: 6px;">
                    <span>Planetary</span>
                    <span>Influence</span>
                </div>
            </button>
            <button>1 – Sun ☉</button>
            <button>2 – Moon ☽</button>
            <button>3 – Jupiter ♃</button>
            <button>4 – Rahu ☊</button>
            <button>5 – Mercury ☿</button>
            <button>6 – Venus ♀</button>
            <button>7 – Ketu ☋</button>
            <button>8 – Saturn ♄</button>
            <button>9 – Mars ♂</button>
        </div>
    </div>

""", unsafe_allow_html=True)

# Link: https://astrologyayurveda.com/blog/astrology-and-numerology/

# ---------- HEADER ----------

st.markdown("""
    <h1 style='text-align: center; font-size: 48 px;'>
    🔷 Vedic Numerology
    </h1>
    """, unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; font-weight: bold; font-style: italic; font-size: 18px;'>
    <span style='color: goldenrod;'>─────</span>   
    <span style='color: gray;'>Decode Your Destiny</span>   
    <span style='color: goldenrod;'>─────</span>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
    <h1 style='font-size: 48 px;'>Phone Number Numerology Tool*
    </h1>
    """, unsafe_allow_html=True)
st.markdown("<p style='color:gray; font-style:italic;'>*This tool is for Indian phone numbers only.</p>", unsafe_allow_html=True)
st.markdown("#### Enter 10-Digit **Indian** Phone Number: ")
st.markdown("<br>", unsafe_allow_html=True)

# ---------- INPUT FIELD ----------

with st.form("input_form", clear_on_submit=False):
    col1, col2 = st.columns([6, 1])
    with col1:
        digits_only = st.text_input("*This tool is for Indian phone numbers only.", "", max_chars=10, label_visibility="collapsed")
    with col2:
        submit = st.form_submit_button("Submit")  

valid = digits_only.isdigit() and len(digits_only) == 10
all_zero = valid and all(z == "0" for z in digits_only)

input_validation_color = "gray" if all_zero else "green" if valid else "red"
color_selector = "all-zero" if all_zero else "valid" if valid else "invalid"

if digits_only.isdigit() and not all_zero:
    with st.expander("You Have Entered: ", expanded=True):
        st.markdown(f"""
            <div class='input-wrapper {color_selector}'>
                <div class='prefix';">{"&#x1F1EE;&#x1F1F3;+91 -" if not all_zero else ""}</div>
                <div class='digit-display'; style="color: {input_validation_color}; font-weight: bold;">{digits_only}</div>
            </div>
            <div id='digitCounter' class='char-count {color_selector}'>{len(digits_only)}/10</div>
            """, unsafe_allow_html=True)

# ---------- NUMEROLOGY FUNCTIONS ----------

def sum_and_reduce(digit_str):
    history = []
    current = sum(int(d) for d in digit_str)
    history.append(current)
    while current > 9:
        current = sum(int(d) for d in str(current))
        history.append(current)
    return history

def display_result(title, digit_str):
    history = sum_and_reduce(digit_str)
    reduced_path = " → ".join(
        f"<span class='master-chip'>{h}</span>" if h in MASTER_NUMBERS else str(
            h)
        for h in history
    )
    master_found = next((h for h in history if h in MASTER_NUMBERS), None)
    final_root = history[-1]

    st.markdown(f"""
    <div class="sum-box">
        <div class="sum-title">{title}</div>
        <div class="sum-digits">Digits: {digit_str}</div>
        <div class="sum-digits">Initial Sum: {history[0]}</div>
        <div class="sum-digits">Reduction Path: {reduced_path}</div>
        {f'<div class="master-inline">🔮 Master Number ' + str(master_found) + ' detected — karmic potential</div>' if master_found else '<div></div>'}
        <div class="final-single">Final Root: <strong>{final_root}</strong></div>
    </div>
    """, unsafe_allow_html=True)

# ---------- NUMEROLOGY OUTPUT ----------

if valid and not all(z == "0" for z in digits_only):

    with st.expander("Standard Analysis: Numerology Breakdown", expanded=True):
        display_result(f"1. Sum of All 10 Digits", digits_only)
        display_result(f"2. Sum of Last 4 Digits", digits_only[-4:])
        display_result(f"3. Sum of First 4 Digits", digits_only[:4])
        display_result(f"4. Sum of First 6 Digits", digits_only[:6])

    with st.expander("#### Advanced Analysis: Slider for Custom Digits Range", expanded=False):
        if valid:
            slots_placeholder = st.empty()
            
            padded_digits = list(digits_only.ljust(10, "•"))  # Dots for missing
            start, end = st.slider("Digit Positions (1–10)", 1, 10, (7, 10))
            custom_slice = digits_only[start - 1:end]
            highlight_slot = [start <= i + 1 <= end for i in range(len(padded_digits))]

            # ---------- DIGIT SLOTS ----------

            digit_slots_html = "".join(
                f"""<div class='digit-slot {"highlight-slot" if highlight_slot[i] else ""}'>{d}</div>""" for i, d in enumerate(padded_digits))
            
            label_slots_html = "".join(
                f"<div class='digit-slot-pointer'>{i}</div>" for i in range(1, 11))

            slots_placeholder.markdown(f"""
                <div class='digit-slots'>
                    {digit_slots_html}
                </div>
                <div class='digit-labels'>
                    {label_slots_html}
                </div>
                """, unsafe_allow_html=True)
            
            display_result(f"5. Sum of Digits {start} through {end}", custom_slice)

elif digits_only.isdigit() and len(digits_only) != 10 and len(digits_only) > 0:
    st.warning("⚠️ Enter exactly 10-digit phone number.")
elif not digits_only.isdigit() and len(digits_only) > 0:
    st.warning("⚠️ Only numeric input is allowed. Enter exactly 10-digit phone number.")
elif all(z == "0" for z in digits_only) and len(digits_only) == 10:
    left, center, right = st.columns([1, 2, 1])  
    with center:
        with st.spinner('Scanning cosmic field for vibrations...'):
            time.sleep(2)
    st.markdown("""
        <div class="sum-box. master-inline">
            <div style='
                text-shadow: 0 0 2px #444, 0 0 10px #aaa;
                text-align: center; 
                font-size: 1.5em; 
                font-family: "Palatino Linotype", "Georgia", serif; 
                padding: 1.5em 1em; 
                color: #222;
            '>
                <div style='margin-top: 1em; font-size: 1em;'>
                    You typed all zeroes, and the Universe noticed.
                </div>
                <div class='blackhole' style='font-size: 3em; line-height: 1;'>🕳️</div>
                <div style='margin-top: 1em; font-size: 1em;'>
                    Welcome to the eternal void, only cosmic silence persists... <br>
                    No echoes, no vibrations, no fate. Just... null!
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div style='
            background-color: #eef6ff;
            padding: 1rem;
            border-radius: 10px;
            font-size: 1rem;
            color: #1560BD;
        '>
            Enter your Indian phone number (without +91), then click 
            <span style="color: green; font-weight: bold;">'Submit'</span> 
            or hit 
            <span style="color: green; font-weight: bold;">'Enter'</span>.
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
    <small>
    🔐 <strong>Privacy Statement:</strong> We respect your privacy. This application does <em>not collect, store, or transmit</em> any user data, including phone numbers. All processing occurs within your browser locally.
    </small>
    """, unsafe_allow_html=True)

if valid:
    st.markdown("""
        <style>
        /* By default, hide the planet bar */
        .planet-bar {
        display: none;
        }

        /* Only show this bar on mobile screens */
        @media screen and (max-width: 1080px) {
            .planet-bar {
                position: fixed;
                bottom: 1.8rem;
                left: 0;
                width: 100%;
                background: #f9f9f9;
                background-color: #f4f4f4;
                box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
                display: flex;
                justify-content: space-around;
                padding: 10px 0px;
                z-index: 9999;
                gap: 2px;
                flex-wrap: wrap;

                animation: floaty 6s ease-in-out infinite;
                will-change: transform; 
            }

            .planet-bar button {                
                flex: 1 1 auto; 
                width: fit-content;
                font-weight: 600;
                padding: 6px 6px;
                border: none;
                border-radius: 8px;
                background-color: #ffffff;
                box-shadow: 0 1px 2px rgba(0,0,0,0.1);
                cursor: pointer;
                white-space: nowrap;
                text-align: center;
                color: #333;
                transition: all 0.2s ease;
            }

            .planet-bar button:hover {
                background-color: #dcdcdc;
                cursor: default;
            }
                
            @keyframes floaty {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-5px);
                }
            }
        }
        </style>
                    
        <div class="planet-bar">
            <button>1 – Su</button>
            <button>2 – Mo</button>
            <button>3 – Ju</button>
            <button>4 – Ra</button>
            <button>5 – Me</button>
            <button>6 – Ve</button>
            <button>7 – Ke</button>
            <button>8 – Sa</button>
            <button>9 – Ma</button>
        </div>
        """, unsafe_allow_html=True)
    
st.markdown("""
    <style>
    .footer-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #f4f4f4;
        color: #333;
        padding: 6px 10px;
        font-size: 0.80rem;
        text-align: center;
        border-top: 1px solid #dcdcdc; 
        z-index: 9990; 
        box-shadow: 0 -1px 5px rgba(0,0,0,0.1);
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
    }
    </style>

    <div class="footer-bar">            
        Shared freely with the Universe ✨
    </div>
""", unsafe_allow_html=True)