import streamlit as st
import pandas as pd

# --- Page Setup ---
st.set_page_config(page_title="Full Squat Challenge", page_icon="🏋🏿")

# --- Developer / School Credit Header ---
st.markdown("""
<div style='background: linear-gradient(135deg, #002D72 0%, #003DA5 100%); 
            padding: 20px; border-radius: 10px; margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
    <div style='color: white;'>
        <h2 style='margin: 0; color: #FFC72C; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
            🏋🏿 Full Squat Challenge: What's the Observers' Consensus?
        </h2>
        <p style='margin: 5px 0; font-size: 1.1em; font-weight: 500;'>
            Mr. H Math ⭐
        </p>
        <p style='margin: 5px 0; opacity: 0.95;'>8th Grade Mathematics | Developed by Mr. H</p>
        <hr style='border: 1px solid rgba(255,255,255,0.3); margin: 10px 0;'>
        <p style='margin: 5px 0; font-size: 0.95em;'>📊 Theme: Live Data & Judged Consensus | Unit: Statistics & Probability</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Title / Intro ---
st.title("⭐ Data Analysts: The Full Squat Challenge")
st.markdown("""
Welcome, **mathematicians**! Today's data comes from a real physical challenge: one student does **20 bodyweight squats**, 
and **3 judges** each independently call every rep either **Full (F)** — all the way down, all the way up, no pausing — 
or **Not Full / X** — if it was too shallow, too fast, or paused mid-rep.

Your job isn't to judge the squats. It's to **organize and analyze what the judges said**, using two-way tables and 
data distributions — real tools statisticians use whenever multiple observers rate the same event.
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.info("🏋🏿 **Squats performed**\n\n20")
with col2:
    st.info("👀 **Judges watching**\n\n3")
with col3:
    st.info("✅ **Rule for 'Full'**\n\nBottom → top, no pausing")

st.success("**🎯 Learning Target:** I can organize categorical data into a two-way table, calculate relative frequencies, and build a data distribution to describe consensus among multiple observers.")

st.markdown("---")

# ============================================================
# INTRO / RESEARCH CONNECTION
# ============================================================
st.header("🧭 Why Squats? The Real Research Behind Today's Data")
st.markdown("""
This isn't just a random movement to collect data on. The **squat** — and its close cousin, the **sit-to-stand** — 
is one of the most studied movements in aging and longevity research. Scientists use how well (and how fast) someone 
can squat down and stand back up as a real predictor of long-term health.

A well-known 2014 study followed **2,002 adults ages 51–80** for over 6 years, scoring how well they could sit down 
on the floor and rise back up without using their hands. People who scored low on this test had a **meaningfully 
higher risk of death** over the following years, even after accounting for age and other health factors.

**Citation:** Brito LBB, Ricardo DR, Araújo CGS, et al. *Ability to sit and rise from the floor as a predictor of 
all-cause mortality.* European Journal of Preventive Cardiology. 2014;21(7):892-898.
""")

with st.expander("🔗 Read more about squatting & longevity research"):
    st.markdown("""
    - [AARP — Sit-to-Stand: A Simple Way to Test Longevity](https://www.aarp.org/health/healthy-living/10-second-sitting-rising-test-longevity/)
    - [Squats and Longevity — Why the Sit-to-Stand Test Predicts How Long You Live](https://www.typeatraining.com/blog/squats-and-longevity-guide/)
    - [Sit-to-Stand Test as a Longevity Marker — research summary](https://getfitcraft.com/science/sit-to-stand-test-longevity)
    """)

st.info("💡 **The connection to today's math:** Researchers didn't just watch one person squat once — they needed **multiple observers and consistent scoring rules** to trust their data. That's exactly what you're about to analyze!")

st.markdown("---")

# ============================================================
# MICHIGAN STANDARDS DROPDOWN
# ============================================================
st.header("📚 Michigan Standards & Common Core Equivalents Covered in This Lesson")

standard_choice = st.selectbox("Select a Michigan Standard:", [
    "MI.8.SP.A.4 — Construct and interpret two-way tables; calculate relative frequencies",
    "MI.6.SP.B.5 — Summarize numerical data sets in relation to their context",
    "MP.3 — Construct viable arguments and critique the reasoning of others",
    "MP.4 — Model with mathematics",
    "MP.6 — Attend to precision"
])

standard_details = {
    "MI.8.SP.A.4": {
        "cc": "CCSS.MATH.CONTENT.8.SP.A.4",
        "rigor": "Organizing bivariate categorical data (Judge A vs. Judge B calls) into a two-way frequency and relative frequency table.",
        "where": "Part 2 — The Two-Way Table"
    },
    "MI.6.SP.B.5": {
        "cc": "CCSS.MATH.CONTENT.6.SP.B.5",
        "rigor": "Summarizing the distribution of '# of judges calling a squat Full' across all 20 attempts.",
        "where": "Part 3 — The Distribution"
    },
    "MP.3": {
        "cc": "CCSS.MATH.PRACTICE.MP3",
        "rigor": "Evaluating whether the judges' disagreement reflects a real pattern or random noise — critiquing the observers' reasoning using data.",
        "where": "Discussion questions after Part 3"
    },
    "MP.4": {
        "cc": "CCSS.MATH.PRACTICE.MP4",
        "rigor": "Translating a real, physical, judged event into an organized statistical table.",
        "where": "Part 1 — The Log → Part 2 — The Two-Way Table"
    },
    "MP.6": {
        "cc": "CCSS.MATH.PRACTICE.MP6",
        "rigor": "Precisely tallying F/X calls per judge without transposition errors — small counting mistakes compound fast in a two-way table.",
        "where": "Throughout Parts 1-3"
    }
}
selected_code = standard_choice.split(" — ")[0]
details = standard_details[selected_code]
st.markdown(f"""
<div style='background-color: #f0f4fa; padding: 15px; border-radius: 8px; border-left: 5px solid #002D72;'>
    <p style='margin: 4px 0;'><strong>Michigan Standard:</strong> {selected_code}</p>
    <p style='margin: 4px 0;'><strong>Common Core Equivalent:</strong> {details['cc']}</p>
    <p style='margin: 4px 0;'><strong>🧭 Rigor Skill It Builds:</strong> {details['rigor']}</p>
    <p style='margin: 4px 0;'><strong>📍 Where in Today's Activity:</strong> {details['where']}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Overarching Goal Statement ---
st.markdown("""
<div style='background: linear-gradient(135deg, #FFC72C 0%, #E8A317 100%); 
            padding: 18px; border-radius: 10px; margin-bottom: 15px;'>
    <h4 style='color: #002D72; margin-top: 0;'>🧭 The Big Picture: Why This Activity Matters</h4>
    <p style='color: #002D72; margin: 0; font-size: 0.98em;'>
    Whenever multiple people judge the same event — referees, doctors, researchers, even judges in a courtroom — 
    <strong>disagreement is normal, and organized data is how you make sense of it.</strong> Today you're building the same 
    skill scientists use to check whether observers agree: <strong>organize raw calls into a table, calculate frequencies, 
    and look for patterns in the disagreement itself.</strong> That's not just a statistics unit — it's how real research, 
    from longevity studies to sports instant replay, actually works.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# THE DATA
# ============================================================
SQUATS = list(range(1, 21))
JUDGE_A = list("FFFFFFFFFFXFXXXXXXXX")
JUDGE_B = list("FFFFFFFFFXFXFXXXXXXX")
JUDGE_C = list("FFFFFFFFXFFXXFXXXXXX")

DF = pd.DataFrame({"Squat #": SQUATS, "Judge A": JUDGE_A, "Judge B": JUDGE_B, "Judge C": JUDGE_C})
DF["# Judges Full"] = DF[["Judge A", "Judge B", "Judge C"]].apply(lambda r: sum(x == "F" for x in r), axis=1)

st.header("📝 Part 1: The Log")
st.markdown("Below is the raw call log from all 3 judges for all 20 squats. **F = Full, counted. X = Not full, not counted.**")
st.dataframe(DF, use_container_width=True, hide_index=True)

a_total = JUDGE_A.count("F")
b_total = JUDGE_B.count("F")
c_total = JUDGE_C.count("F")
t1, t2, t3 = st.columns(3)
t1.metric("Judge A total Full calls", a_total)
t2.metric("Judge B total Full calls", b_total)
t3.metric("Judge C total Full calls", c_total)

st.info("👀 **Notice anything?** All three judges landed on the same *total* — but did they agree on *which* squats? That question is exactly what a two-way table answers.")

st.markdown("---")

# ============================================================
# PLAIN-LANGUAGE EXPLAINER: WHAT IS A TWO-WAY TABLE?
# ============================================================
st.header("🧠 What IS a Two-Way Table? (Plain-Language Explainer)")
st.markdown("""
**This section is for everyone — students AND teachers. If two-way tables never fully clicked before, start here.**

A two-way table just answers one question: **"When two things happen at the same time, how often does each combination show up?"**

**Forget squats for a second.** Imagine you asked 20 people two yes/no questions:
1. Do you like pizza? (Yes/No)
2. Do you like tacos? (Yes/No)

A two-way table just sorts everyone into **4 boxes**, based on their two answers at once:

| | Likes Tacos | Doesn't Like Tacos |
|---|---|---|
| **Likes Pizza** | Box 1: people who said YES to both | Box 2: pizza-yes, taco-no |
| **Doesn't Like Pizza** | Box 3: pizza-no, taco-yes | Box 4: said NO to both |

That's it. That's the whole idea. **Every person on Earth falls into exactly ONE of those 4 boxes**, based on their two answers.

---

**Now swap "pizza and tacos" for "Judge A and Judge B."** Instead of yes/no, it's **Full/Not Full**. Instead of 20 people, 
it's **20 squats**. The 4 boxes become:

| | Judge B says FULL | Judge B says NOT FULL |
|---|---|---|
| **Judge A says FULL** | Both judges agreed it counted | A said yes, B said no |
| **Judge A says NOT FULL** | A said no, B said yes | Both judges agreed it didn't count |

**How do you fill it in?** Go through the Part 1 log **one squat at a time**. For EACH of the 20 squats, look at ONLY 
Judge A's letter and Judge B's letter, decide which of the 4 boxes it belongs in, and add a tally mark to that box. 
After all 20 squats, count up the tally marks in each box — those are your 4 numbers.

**The #1 mistake people make:** rushing and putting a squat in the wrong box because they only looked at one judge's 
letter, not both at the same time. Slow down and check BOTH letters for every single squat.
""")

st.markdown("---")

# ============================================================
# PART 2: TWO-WAY TABLE (with diagnostic per-cell feedback)
# ============================================================
st.header("🔢 Part 2: The Two-Way Table (Judge A vs. Judge B)")
st.markdown("Now that you understand the boxes, fill in the real two-way table comparing **Judge A's** and **Judge B's** calls across all 20 squats.")

both_full = sum(1 for a, b in zip(JUDGE_A, JUDGE_B) if a == "F" and b == "F")
a_only = sum(1 for a, b in zip(JUDGE_A, JUDGE_B) if a == "F" and b == "X")
b_only = sum(1 for a, b in zip(JUDGE_A, JUDGE_B) if a == "X" and b == "F")
neither = sum(1 for a, b in zip(JUDGE_A, JUDGE_B) if a == "X" and b == "X")

st.markdown("**Fill in each of the 4 boxes, then check your work:**")
tw1, tw2, tw3, tw4 = st.columns(4)
with tw1:
    in_both = st.number_input("Box 1: A=Full & B=Full", min_value=0, max_value=20, step=1, key="tw_both")
with tw2:
    in_aonly = st.number_input("Box 2: A=Full & B=Not Full", min_value=0, max_value=20, step=1, key="tw_aonly")
with tw3:
    in_bonly = st.number_input("Box 3: A=Not Full & B=Full", min_value=0, max_value=20, step=1, key="tw_bonly")
with tw4:
    in_neither = st.number_input("Box 4: A=Not Full & B=Not Full", min_value=0, max_value=20, step=1, key="tw_neither")

if 'tw_attempts' not in st.session_state:
    st.session_state.tw_attempts = 0

if st.button("Check My Two-Way Table", key="tw_check"):
    checks = {
        "Box 1 (A=Full & B=Full)": (in_both == both_full, in_both, both_full),
        "Box 2 (A=Full & B=Not Full)": (in_aonly == a_only, in_aonly, a_only),
        "Box 3 (A=Not Full & B=Full)": (in_bonly == b_only, in_bonly, b_only),
        "Box 4 (A=Not Full & B=Not Full)": (in_neither == neither, in_neither, neither),
    }
    wrong_boxes = {k: v for k, v in checks.items() if not v[0]}

    if not wrong_boxes:
        st.balloons()
        st.success(f"✅ Correct! Box 1: {both_full}, Box 2: {a_only}, Box 3: {b_only}, Box 4: {neither} — and they all sum to 20.")
        st.session_state.tw_attempts = 0
    else:
        st.session_state.tw_attempts += 1
        total_entered = in_both + in_aonly + in_bonly + in_neither
        if st.session_state.tw_attempts == 1:
            st.warning(f"❌ Not quite yet — {len(wrong_boxes)} of your 4 boxes need another look.")
            st.info(f"""
            💡 **Diagnostic hint:** Your 4 numbers currently add up to **{total_entered}** (they must add up to exactly 20, 
            since there are 20 squats total).
            
            The box(es) that need rechecking: **{', '.join(wrong_boxes.keys())}**
            
            Go back to the Part 1 log and re-scan just those squats — for each row, look at Judge A's letter AND 
            Judge B's letter together, not one at a time.
            """)
        else:
            st.error("❌ Still not matching. Here's the fully worked answer:")
            st.markdown(f"""
            | | Judge B = FULL | Judge B = NOT FULL |
            |---|---|---|
            | **Judge A = FULL** | {both_full} | {a_only} |
            | **Judge A = NOT FULL** | {b_only} | {neither} |

            **Why:** Going squat-by-squat through Part 1, count each combination of A's letter and B's letter. 
            {both_full} squats had both judges say Full, {a_only} had only A say Full, {b_only} had only B say Full, 
            and {neither} had neither judge say Full. Together: {both_full}+{a_only}+{b_only}+{neither} = 20 ✓
            """)

st.markdown("---")

# ============================================================
# PART 3: THE DISTRIBUTION (with diagnostic per-cell feedback)
# ============================================================
st.header("📊 Part 3: The Distribution")
st.markdown("""
A **distribution** just answers: *"Out of all 20 squats, how many had 0 judges agree it was full? How many had 1? 2? 3?"* 
Use the **"# Judges Full"** column from the Part 1 table above — just count how many rows have each value.
""")

dist = DF["# Judges Full"].value_counts().sort_index()
correct_dist = {i: int(dist.get(i, 0)) for i in range(4)}

d1, d2, d3, d4 = st.columns(4)
with d1:
    in0 = st.number_input("0 judges said Full", min_value=0, max_value=20, step=1, key="d0")
with d2:
    in1 = st.number_input("1 judge said Full", min_value=0, max_value=20, step=1, key="d1")
with d3:
    in2 = st.number_input("2 judges said Full", min_value=0, max_value=20, step=1, key="d2")
with d4:
    in3 = st.number_input("3 judges said Full", min_value=0, max_value=20, step=1, key="d3")

if 'dist_attempts' not in st.session_state:
    st.session_state.dist_attempts = 0

if st.button("Check My Distribution", key="dist_check"):
    checks = {
        "0 judges said Full": (in0 == correct_dist[0], in0, correct_dist[0]),
        "1 judge said Full": (in1 == correct_dist[1], in1, correct_dist[1]),
        "2 judges said Full": (in2 == correct_dist[2], in2, correct_dist[2]),
        "3 judges said Full": (in3 == correct_dist[3], in3, correct_dist[3]),
    }
    wrong_counts = {k: v for k, v in checks.items() if not v[0]}

    if not wrong_counts:
        st.balloons()
        st.success(f"✅ Correct! 3 judges agreed on {correct_dist[3]} squats, 2 on {correct_dist[2]}, 1 on {correct_dist[1]}, and 0 on {correct_dist[0]}.")
        st.bar_chart(pd.Series(correct_dist, name="# of Squats"))
        st.session_state.dist_attempts = 0
    else:
        st.session_state.dist_attempts += 1
        total_entered = in0 + in1 + in2 + in3
        if st.session_state.dist_attempts == 1:
            st.warning(f"❌ Not quite yet — {len(wrong_counts)} of your 4 numbers need another look.")
            st.info(f"""
            💡 **Diagnostic hint:** Your 4 numbers currently add up to **{total_entered}** (they must add up to exactly 20).
            
            The count(s) that need rechecking: **{', '.join(wrong_counts.keys())}**
            
            Go back to the **"# Judges Full"** column in Part 1 and literally count how many rows show each number (0, 1, 2, 3).
            """)
        else:
            st.error("❌ Still not matching. Here's the fully worked answer:")
            st.markdown(f"""
            - **0 judges said Full:** {correct_dist[0]} squats
            - **1 judge said Full:** {correct_dist[1]} squats
            - **2 judges said Full:** {correct_dist[2]} squats
            - **3 judges said Full:** {correct_dist[3]} squats

            Together: {correct_dist[0]}+{correct_dist[1]}+{correct_dist[2]}+{correct_dist[3]} = 20 ✓ 
            (matches the 20 total squats).
            """)

st.markdown("---")

# ============================================================
# DISCUSSION / MP.3
# ============================================================
st.header("💬 Discussion: Critique the Judges' Reasoning (MP.3)")
st.markdown("""
Look at the squats where judges disagreed most (the middle of the log). Why might reasonable, attentive judges 
disagree on the exact same squat?
""")
discussion = st.text_area("Your reasoning:", key="discussion", height=100, placeholder="e.g., 'Full' is a judgment call at the very bottom of the squat, so different angles or attention...")

if st.button("Submit My Reasoning", key="discussion_submit"):
    if discussion.strip():
        st.balloons()
        st.success("🎉 Great thinking! Just like the longevity researchers had to define exact criteria for a 'countable' rise from the floor, judges need a shared, precise standard — and even then, disagreement at the edges is normal.")
    else:
        st.warning("Please share your reasoning to complete this discussion.")

st.markdown("---")

# ============================================================
# EXTRA PRACTICE RESOURCES
# ============================================================
st.header("🔗 Extra Practice: Two-Way Tables at Home")
res_col1, res_col2 = st.columns(2)
with res_col1:
    st.markdown("""
    <div style='background-color: #f0f4fa; padding: 15px; border-radius: 8px; border-left: 5px solid #002D72; height: 100%;'>
        <h4 style='margin-top: 0; color: #002D72;'>📊 IXL Practice</h4>
        <p style='margin: 4px 0;'><strong>Interpret two-way frequency tables</strong></p>
        <a href='https://www.ixl.com/math/grade-8/interpret-two-way-frequency-tables' target='_blank'>👉 Practice on IXL</a>
    </div>
    """, unsafe_allow_html=True)
with res_col2:
    st.markdown("""
    <div style='background-color: #fff8ea; padding: 15px; border-radius: 8px; border-left: 5px solid #FFC72C; height: 100%;'>
        <h4 style='margin-top: 0; color: #002D72;'>🎓 Khan Academy Practice</h4>
        <p style='margin: 4px 0;'><strong>Two-way frequency tables</strong></p>
        <a href='https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-data/two-way-tables/e/two-way-frequency-tables' target='_blank'>👉 Practice on Khan Academy</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.header("⭐ What You've Learned Today")
st.markdown("""
**Congratulations, Data Analysts!** Today you built a two-way table, summarized a data distribution, and thought 
critically about why even careful, well-trained observers disagree — the same real-world skill behind the squatting 
and longevity research you read about at the start.

Keep organizing the data, mathematicians! ⭐📊
""")
