import streamlit as st

st.set_page_config(page_title="🔢 Phone Number Numerology", layout="centered")

# ---------- STYLES ----------
st.markdown("""
    <style>

        .master-chip {
            background-color: #e6d6f5;
            color: #4b0082;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 4px;
        }

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

        .input-wrapper.get-number {
            border-color: grey !important;
        }

        .input-wrapper.valid {
            border-color: green !important;
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
            
        /* Floating Box Container */
        #floating-box {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        /* Each Layer (like burger stack) */
        .floating-layer {
            background-color: #f4f4f4;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            padding: 12px;
            width: 160px;
            text-align: center;
        }

        /* Buttons inside the layer */
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
        }
            
            /* Floating Box Container */
    #floating-box-left {
        position: fixed;
        top: 50%;
        left: 20px;
        transform: translateY(-50%);
        z-index: 9999;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

</style>
      
<div id="floating-box-left">
    <div class="floating-layer">
        <button style="background-color: #dcdcdc">Planetary Influence</button>
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
<span style='color: goldenrod;'>──────────</span>   
<span style='color: gray;'>Decode Your Destiny</span>   
<span style='color: goldenrod;'>──────────</span>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""
<h1 style='font-size: 48 px;'>Phone Number Numerology Tool*
</h1>
""", unsafe_allow_html=True)
st.markdown(
    "<p style='color:gray; font-style:italic;'>*This tool is for Indian phone numbers only.</p>",
    unsafe_allow_html=True
)

st.markdown("#### Enter 10-digit **Indian** phone number: ")

st.markdown("<br>", unsafe_allow_html=True)

# ---------- INPUT FIELD ----------

digits_only = st.text_input("*This tool is for Indian phone numbers only.",
                                                        "", max_chars=10, label_visibility="collapsed")

valid = digits_only.isdigit() and len(digits_only) == 10

if digits_only.isdigit():
    st.markdown("---")
    st.markdown("#### You have entered: ")
    st.markdown(f"""
        <div class='input-wrapper {"valid" if valid else ""}'>
            <div class='prefix'>&#x1F1EE;&#x1F1F3;+91 -</div>
            <div class='digit-display'>{digits_only}</div>
        </div>
        <div id='digitCounter' class='char-count {"valid" if valid else ""}'>{len(digits_only)}/10</div>
        """, unsafe_allow_html=True)

# ---------- NUMEROLOGY FUNCTIONS ----------

MASTER_NUMBERS = {11, 22}

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
        <div>Initial Sum: {history[0]}</div>
        <div>Reduction Path: {reduced_path}</div>
        {f'<div class="master-inline">🔮 Master Number ' + str(master_found) + ' detected — karmic potential</div>' if master_found else '<div></div>'}
        <div class="final-single">Final Root: <strong>{final_root}</strong></div>
    </div>
    """, unsafe_allow_html=True)

# ---------- NUMEROLOGY OUTPUT ----------

if valid:
    st.markdown("---")
    st.markdown("#### Numerology Breakdown: ")

    display_result(f"1. Sum of All 10 Digits", digits_only)
    display_result(f"2. Sum of Last 4 Digits", digits_only[-4:])
    display_result(f"3. Sum of First 4 Digits", digits_only[:4])
    display_result(f"4. Sum of First 6 Digits", digits_only[:6])

    st.markdown("---")
    st.markdown("#### Slider for Custom Digits Range: ")

    # ---------- DIGIT SLOTS ----------

    padded_digits = list(digits_only.ljust(10, "•"))  # Dots for missing
    digit_slots_html = "".join(
        f"<div class='digit-slot'>{d}</div>" for d in padded_digits)
    label_slots_html = "".join(
        f"<div class='digit-slot-pointer'>{i}</div>" for i in range(1, 11))
    st.markdown(f"""
    <div class='digit-slots'>
        {digit_slots_html}
    </div>
    <div class='digit-labels'>
        {label_slots_html}
    </div>
    """, unsafe_allow_html=True)

    # ---------- SLIDER ----------

    if valid:
        start, end = st.slider("Digit Positions (1–10)", 1, 10, (7, 10))
        custom_slice = digits_only[start - 1:end]
    else:
        custom_slice = ""

    if custom_slice:
        display_result(f"5. Sum of Digits {start} through {end}", custom_slice)

elif digits_only.isdigit() and len(digits_only) != 10 and len(digits_only) > 0:
    st.warning("⚠️ Enter exactly 10-digit phone number.")
elif not digits_only.isdigit() and len(digits_only) > 0:
    st.warning("⚠️ Only numeric input is allowed. Enter exactly 10-digit phone number.")
else:
    st.info("Enter your Indian phone number (without +91) and hit `'Enter'`. ")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("""
<small>
🔐 <strong>Privacy Statement:</strong> We respect your privacy. This application does <em>not collect, store, or transmit</em> any user data, including phone numbers. All processing occurs locally within your browser and is neither retained nor shared.
</small>
""", unsafe_allow_html=True)