
import streamlit as st

# Starting point
if "step" not in st.session_state:
    st.session_state.step = 1


def go_to(step):
    st.session_state.step = step
    st.rerun()


st.title("💌 A Little Question 💌")


# 1
if st.session_state.step == 1:

    st.write("## Can I take you on a date? 💗")

    if st.button("Yes 💗"):
        go_to(19)

    elif st.button("No"):
        go_to(2)


# 2
elif st.session_state.step == 2:

    st.write("## U sure? 👀")

    if st.button("Yes"):
        go_to(3)

    elif st.button("No"):
        go_to(1)


# 3
elif st.session_state.step == 3:

    st.write("## Are you sure? 🥺")

    if st.button("Yes"):
        go_to(4)

    elif st.button("No"):
        go_to(1)


# 4
elif st.session_state.step == 4:

    st.write("## Really sure? 😳")

    if st.button("Yes"):
        go_to(5)

    elif st.button("No"):
        go_to(5)


# 5
elif st.session_state.step == 5:

    st.write("## Super duper sure? 🥺")

    if st.button("Yes"):
        go_to(6)

    elif st.button("No"):
        go_to(6)


# 6
elif st.session_state.step == 6:

    st.write("## Aww, pretty please? :<")

    if st.button("Okay, yes"):
        go_to(1)

    elif st.button("No"):
        go_to(7)


# 7
elif st.session_state.step == 7:

    st.write("## Can I change your mind? 🥺")

    if st.button("Yes"):
        go_to(8)

    elif st.button("No"):
        go_to(8)


# 8
elif st.session_state.step == 8:

    st.write("## What if I do a trick? 👀")

    if st.button("Okay!"):
        go_to(9)

    elif st.button("No"):
        go_to(9)


# 9
elif st.session_state.step == 9:

    st.write("## 🪄 MAGIC TRICK 🪄")
    st.write("Think of a number. Done?")

    if st.button("Yes!"):
        go_to(10)


# 10
elif st.session_state.step == 10:

    st.write("## Double it.")

    if st.button("Okay!"):
        go_to(11)


# 11
elif st.session_state.step == 11:

    st.write("## Add 4 to that.")

    if st.button("Okay!"):
        go_to(12)


# 12
elif st.session_state.step == 12:

    st.write("## Divide by 2.")

    if st.button("Okay!"):
        go_to(13)


# 13
elif st.session_state.step == 13:

    st.write("## Now subtract your original number.")

    if st.button("Okay!"):
        go_to(14)


# 14
elif st.session_state.step == 14:

    st.write("# IS IT 2?!? HAHAHAHA 😂")
    st.write("I KNEW IT! 🪄✨")
    st.write("Did I changed your mind? hehe")
    if st.button("Yes💗"):
        go_to(1)
    if st.button("No "):
        go_to(15)


# 15
elif st.session_state.step == 15:

    st.write("## So we're gonna do this the hard way then? 😭")

    if st.button("Yes"):
        go_to(16)


# 16
elif st.session_state.step == 16:

    st.write("## Will you go out with me? 💗")

    if st.button("YES 💗"):
        go_to(17)

    elif st.button("YESSS 😭"):
        go_to(17)

    elif st.button("YES! 🥹"):
        go_to(17)

    elif st.button("YES PLEASE"):
        go_to(17)

    elif st.button("OF COURSE!"):
        go_to(17)

    elif st.button("Maybe... 👀"):
        go_to(18)


# 17
elif st.session_state.step == 17:

    st.balloons()

    st.write("# YAYYYYY! 💗😭")
    st.write("## IT'S A DATE!!! 🥳💗")


# 18
elif st.session_state.step == 18:

    st.write("# Maybe? 👀")
    st.write("## It's a yes then? YAYYY! 💗😭")
    st.write("### IT'S A DATE!!! 🥳💗")

elif st.session_state.step == 19:

    st.write("# WOAAHHHH!")
    st.write("## It's a yes? YAYYY! 💗😭")
    st.write("### IT'S A DATE!!! 🥳💗")
