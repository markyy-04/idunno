import streamlit as st

# Remember which question we're on
if "step" not in st.session_state:
    st.session_state.step = 1


# =========================
# TITLE
# =========================

st.title("💌 A Little Question")


# =========================
# STEP 1
# =========================

if st.session_state.step == 1:

    st.write("### Can I take you on a date? 💗")

    if st.button("Yes 💗"):
        st.session_state.step = 2
        st.rerun()

    if st.button("No"):
        st.session_state.step = 3
        st.rerun()


# =========================
# NO → ARE YOU SURE?
# =========================

elif st.session_state.step == 3:

    st.write("### Are you sure? 🥺")

    if st.button("Yes, I'm sure"):
        st.write("Okay, I respect that. ❤️")

    if st.button("No, let me think"):
        st.session_state.step = 1
        st.rerun()


# =========================
# U SURE?
# =========================

elif st.session_state.step == 2:

    st.write("### U sure? 👀")

    if st.button("Yes"):
        st.session_state.step = 4
        st.rerun()

    if st.button("No"):
        st.session_state.step = 1
        st.rerun()


# =========================
# REALLY SURE?
# =========================

elif st.session_state.step == 4:

    st.write("### Really sure? 😳")

    if st.button("Yes"):
        st.session_state.step = 5
        st.rerun()

    if st.button("No"):
        st.session_state.step = 1
        st.rerun()


# =========================
# SUPER DUPER SURE?
# =========================

elif st.session_state.step == 5:

    st.write("### Super duper sure? 🥺")

    if st.button("Yes"):
        st.session_state.step = 6
        st.rerun()

    if st.button("No"):
        st.session_state.step = 1
        st.rerun()


# =========================
# PRETTY PLEASE
# =========================

elif st.session_state.step == 6:

    st.write("### Aww, pretty please? :<")

    if st.button("Yes"):
        st.session_state.step = 7
        st.rerun()

    if st.button("No"):
        st.session_state.step = 1
        st.rerun()


# =========================
# CHANGE YOUR MIND
# =========================

elif st.session_state.step == 7:

    st.write("### Can I change your mind? 🥺")

    if st.button("Yes"):
        st.session_state.step = 8
        st.rerun()

    if st.button("No"):
        st.session_state.step = 1
        st.rerun()


# =========================
# TRICK
# =========================

elif st.session_state.step == 8:

    st.write("### What if I do a trick? 👀")

    if st.button("Okay!"):
        st.session_state.step = 9
        st.rerun()

    if st.button("No"):
        st.session_state.step = 1
        st.rerun()


# =========================
# NUMBER TRICK
# =========================

elif st.session_state.step == 9:

    st.write("## 🪄 MAGIC TRICK 🪄")

    st.write("Think of a number. Done?")

    if st.button("Yes!"):
        st.session_state.step = 10
        st.rerun()


elif st.session_state.step == 10:

    st.write("### Double it.")

    if st.button("Okay!"):
        st.session_state.step = 11
        st.rerun()


elif st.session_state.step == 11:

    st.write("### Add 4 to that.")

    if st.button("Okay!"):
        st.session_state.step = 12
        st.rerun()


elif st.session_state.step == 12:

    st.write("### Divide by 2.")

    if st.button("Okay!"):
        st.session_state.step = 13
        st.rerun()


elif st.session_state.step == 13:

    st.write("### Now subtract your original number.")

    if st.button("Okay!"):
        st.session_state.step = 14
        st.rerun()


# =========================
# MAGIC RESULT
# =========================

elif st.session_state.step == 14:

    st.write("# IS IT 2?!? HAHAHAHA 😂")
    st.write("## I KNEW IT! 🪄✨")

    if st.button("Continue 💗"):
        st.session_state.step = 15
        st.rerun()


# =========================
# HARD WAY
# =========================

elif st.session_state.step == 15:

    st.write("### So we're gonna do this the hard way then? 😭")

    if st.button("Yes"):
        st.session_state.step = 16
        st.rerun()


# =========================
# FINAL QUESTION
# =========================

elif st.session_state.step == 16:

    st.write("## Will you go out with me? 💗")

    if st.button("YES 💗"):
        st.session_state.step = 17
        st.rerun()

    if st.button("YESSS 😭"):
        st.session_state.step = 17
        st.rerun()

    if st.button("YES! 🥹"):
        st.session_state.step = 17
        st.rerun()

    if st.button("YES PLEASE"):
        st.session_state.step = 17
        st.rerun()

    if st.button("OF COURSE!"):
        st.session_state.step = 17
        st.rerun()

    if st.button("Maybe... 👀"):
        st.session_state.step = 18
        st.rerun()


# =========================
# YES
# =========================

elif st.session_state.step == 17:

    st.balloons()

    st.write("# YAYYYYY! 💗😭")
    st.write("## IT'S A DATE!!! 🥳💗")


# =========================
# MAYBE
# =========================

elif st.session_state.step == 18:

    st.write("# Maybe? 👀")
    st.write("## It's a yes then? YAYYY! 💗😭")
    st.write("### IT'S A DATE!!! 🥳💗")
