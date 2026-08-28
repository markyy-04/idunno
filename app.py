import streamlit as st

# Remember the current step
if "step" not in st.session_state:
    st.session_state.step = 1


st.title("💌 A Little Question")


# =========================
# 1. FIRST QUESTION
# =========================

if st.session_state.step == 1:

    st.write("## Can I take you on a date? 💗")

    if st.button("Yes 💗"):
        st.session_state.step = 2
        st.rerun()

    if st.button("No"):
        st.session_state.step = 3
        st.rerun()


# =========================
# 2. U SURE?
# =========================

elif st.session_state.step == 2:

    st.write("## U sure? 👀")

    if st.button("Yes", key="sure_yes"):
        st.session_state.step = 4
        st.rerun()

    if st.button("No", key="sure_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 3. ARE YOU SURE?
# =========================

elif st.session_state.step == 3:

    st.write("## Are you sure? 🥺")

    if st.button("Yes", key="certain_yes"):
        st.session_state.step = 1
        st.rerun()

    if st.button("No", key="certain_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 4. REALLY SURE?
# =========================

elif st.session_state.step == 4:

    st.write("## Really sure? 😳")

    if st.button("Yes", key="really_yes"):
        st.session_state.step = 5
        st.rerun()

    if st.button("No", key="really_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 5. SUPER DUPER SURE?
# =========================

elif st.session_state.step == 5:

    st.write("## Super duper sure? 🥺")

    if st.button("Yes", key="super_yes"):
        st.session_state.step = 6
        st.rerun()

    if st.button("No", key="super_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 6. PRETTY PLEASE
# =========================

elif st.session_state.step == 6:

    st.write("## Aww, pretty please? :<")

    if st.button("Yes", key="please_yes"):
        st.session_state.step = 7
        st.rerun()

    if st.button("No", key="please_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 7. CHANGE YOUR MIND
# =========================

elif st.session_state.step == 7:

    st.write("## Can I change your mind? 🥺")

    if st.button("Yes", key="change_yes"):
        st.session_state.step = 8
        st.rerun()

    if st.button("No", key="change_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 8. THE TRICK
# =========================

elif st.session_state.step == 8:

    st.write("## What if I do a trick? 👀")

    if st.button("Okay!", key="trick_yes"):
        st.session_state.step = 9
        st.rerun()

    if st.button("No", key="trick_no"):
        st.session_state.step = 1
        st.rerun()


# =========================
# 9. NUMBER TRICK
# =========================

elif st.session_state.step == 9:

    st.write("## 🪄 MAGIC TRICK 🪄")
    st.write("### Think of a number. Done?")

    if st.button("Yes!", key="number_done"):
        st.session_state.step = 10
        st.rerun()


# =========================
# 10. DOUBLE IT
# =========================

elif st.session_state.step == 10:

    st.write("## Double it.")

    if st.button("Okay!", key="double"):
        st.session_state.step = 11
        st.rerun()


# =========================
# 11. ADD 4
# =========================

elif st.session_state.step == 11:

    st.write("## Add 4 to that.")

    if st.button("Okay!", key="add_four"):
        st.session_state.step = 12
        st.rerun()


# =========================
# 12. DIVIDE BY 2
# =========================

elif st.session_state.step == 12:

    st.write("## Divide by 2.")

    if st.button("Okay!", key="divide"):
        st.session_state.step = 13
        st.rerun()


# =========================
# 13. SUBTRACT ORIGINAL
# =========================

elif st.session_state.step == 13:

    st.write("## Now subtract your original number.")

    if st.button("Okay!", key="subtract"):
        st.session_state.step = 14
        st.rerun()


# =========================
# 14. RESULT
# =========================

elif st.session_state.step == 14:

    st.write("# IS IT 2?!? HAHAHAHA 😂")
    st.write("## I KNEW IT! 🪄✨")

    if st.button("Continue 💗", key="continue_trick"):
        st.session_state.step = 15
        st.rerun()


# =========================
# 15. HARD WAY
# =========================

elif st.session_state.step == 15:

    st.write("## So we're gonna do this the hard way then? 😭")

    if st.button("Yes", key="hard_way"):
        st.session_state.step = 16
        st.rerun()


# =========================
# 16. FINAL QUESTION
# =========================

elif st.session_state.step == 16:

    st.write("## Will you go out with me? 💗")

    if st.button("YES 💗", key="final_yes1"):
        st.session_state.step = 17
        st.rerun()

    if st.button("YESSS 😭", key="final_yes2"):
        st.session_state.step = 17
        st.rerun()

    if st.button("YES! 🥹", key="final_yes3"):
        st.session_state.step = 17
        st.rerun()

    if st.button("YES PLEASE", key="final_yes4"):
        st.session_state.step = 17
        st.rerun()

    if st.button("OF COURSE!", key="final_yes5"):
        st.session_state.step = 17
        st.rerun()

    if st.button("Maybe... 👀", key="final_maybe"):
        st.session_state.step = 18
        st.rerun()


# =========================
# 17. YES RESULT
# =========================

elif st.session_state.step == 17:

    st.balloons()

    st.write("# YAYYYYY! 💗😭")
    st.write("## IT'S A DATE!!! 🥳💗")


# =========================
# 18. MAYBE
# =========================

elif st.session_state.step == 18:

    st.write("# Maybe? 👀")
    st.write("## It's a yes then? YAYYY! 💗😭")
    st.write("### IT'S A DATE!!! 🥳💗")
