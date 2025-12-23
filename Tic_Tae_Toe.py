import numpy as np

board=np.zeros((3,3),dtype=int)

def print_board(b):
    symbols={
        0:" ",
        1:"X",
        -1:"O"
    }

    for r in range(3):
        row=" | ".join(symbols[val] for val in b[r])
        print(" " + row)
        if r < 2:
            print(" ---+---+--- ")
    print()


def check_winner(b):
    if 3 in np.sum(b,axis=0) or 3 in np.sum(b,axis=1):
        return "X"
    if -3 in np.sum(b,axis=0) or -3 in np.sum(b,axis=1):
        return "O"
    
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"
    
    if not 0 in b:
        return "DRAW"
    return None
    
current=1
print("Welcome Tic-Tac_Toe Game")
print_board(board)

while True:
    if current == 1:
        player = "X"
    else:
        player = "O"
    

    try:
        row=int(input(player + " - Enter Row(0-1-2) :-  "))
        col=int(input(player + " - Enter COlumn(0-1-2);-  "))

    except ValueError:
        print(f"Some error ocured..\n")
        continue


    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Sorry Row or Column must be between 0 to 2!!!")
    
    if board[row,col] != 0:
        print("Cell Alredy Taken!!")
    
    board[row,col] = current
    print_board(board)

    result=check_winner(board)

    if result is not None:
        if result == "DRAW":
            print("It's DRAW!!!")
        else:
            print(result,"wins")

        break

    if current == 1 :
        current = -1
    else:
        current = 1




#With UI Using Streamlit Code...
'''
import streamlit as st
import numpy as np

st.set_page_config(page_title="Tic Tac Toe", layout="centered")

# ---------- GAME LOGIC ----------
def check_winner(board):
    for i in range(3):
        if abs(board[i].sum()) == 3:
            return board[i, 0]
        if abs(board[:, i].sum()) == 3:
            return board[0, i]

    diag1 = board.trace()
    diag2 = np.fliplr(board).trace()

    if abs(diag1) == 3:
        return board[0, 0]
    if abs(diag2) == 3:
        return board[0, 2]

    if not (board == 0).any():
        return 0  # Draw

    return None

def symbol(val):
    if val == 1:
        return "❌"
    if val == -1:
        return "⭕"
    return " "

# ---------- SESSION STATE ----------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3,3), dtype=int)
    st.session_state.player = 1
    st.session_state.game_over = False
    st.session_state.message = "❌ Player X Turn"

# ---------- UI ----------
st.title("🎮 Tic Tac Toe")
st.markdown("### Player ❌ vs Player ⭕")

st.info(st.session_state.message)

st.write("")

# ---------- GAME BOARD ----------
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        cols[j].button(
            symbol(st.session_state.board[i][j]),
            key=f"cell_{i}_{j}",
            use_container_width=True,
            disabled=st.session_state.board[i][j] != 0 or st.session_state.game_over,
            on_click=lambda r=i, c=j: handle_click(r, c)
        )

# ---------- CLICK HANDLER ----------
def handle_click(row, col):
    if st.session_state.game_over:
        return

    st.session_state.board[row][col] = st.session_state.player
    result = check_winner(st.session_state.board)

    if result == 1:
        st.session_state.message = "🎉 Player ❌ Wins!"
        st.session_state.game_over = True
    elif result == -1:
        st.session_state.message = "🎉 Player ⭕ Wins!"
        st.session_state.game_over = True
    elif result == 0:
        st.session_state.message = "🤝 It's a Draw!"
        st.session_state.game_over = True
    else:
        st.session_state.player *= -1
        st.session_state.message = (
            "❌ Player X Turn" if st.session_state.player == 1 else "⭕ Player O Turn"
        )

# ---------- RESTART ----------
st.write("")
if st.button("🔄 Restart Game", use_container_width=True):
    st.session_state.board = np.zeros((3,3), dtype=int)
    st.session_state.player = 1
    st.session_state.game_over = False
    st.session_state.message = "❌ Player X Turn"

'''