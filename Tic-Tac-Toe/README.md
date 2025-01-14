🎮✨ Tic-Tac-Toe (❌⭕) Game

🌟 Overview

This is a 🐍 Python-based version of the classic Tic-Tac-Toe (or XOX) game. Choose from three fun modes:

1️⃣ 👤 vs 🤖2️⃣ 👤 vs 👤3️⃣ 🤖 vs 🤖

It features a 🧠 smart 🤖 that uses strategy for moves and tracks 📊 game stats.

🔥 Features

🎮 3️⃣ Game Modes: Play 🆚 a 🤖, another 👤, or watch 🤖s battle it out.

🧠 Smart 🤖 Moves: Strategic algorithm for optimal 🤖 performance.

🖥️ Dynamic Board Display: Clear 📋 tabulated visualization.

📈 Stats Tracking: Win 🏆, lose ❌, or draw 🤝 tracking.

👍 User-Friendly Interface: Smooth prompts and instructions.

⚙️ Requirements

🐍 Python 3.6+

📦 tabulate library (pip install tabulate)

🕹️ How to Play

👤 vs 🤖 Mode

1️⃣ Select mode by entering 1.2️⃣ Pick your mark (❌ or ⭕).3️⃣ Take turns placing marks on the board (1️⃣-9️⃣).4️⃣ Win 🏆, lose ❌, or draw 🤝.

👤 vs 👤 Mode

1️⃣ Select mode by entering 2.2️⃣ Players alternate placing marks (1️⃣-9️⃣).3️⃣ First to align three wins 🥇!

🤖 vs 🤖 Mode

1️⃣ Select mode by entering 3.2️⃣ Watch two 🤖s compete 🤖⚔️🤖.

🏁 Running the Game

1️⃣ Clone/download this project.2️⃣ Open terminal/IDE in the project folder.3️⃣ Run:

python xox_game.py

📌 Code Highlights

🧠 Smart 🤖 Moves

The 🤖 decides its move with this priority:
1️⃣ Win 🏆 if possible.2️⃣ Block opponent's win ❌.3️⃣ Take center 🎯 if available.4️⃣ Grab a corner ⛳.5️⃣ Random move 🎲.

🗺️ Board Layout

The board positions are:

  1️⃣ | 2️⃣ | 3️⃣
  ---------
  4️⃣ | 5️⃣ | 6️⃣
  ---------
  7️⃣ | 8️⃣ | 9️⃣

🔑 Key Functions

fill_board(value, place): Place a mark (❌ or ⭕).

check_winner(board): Check for a winner 🏆.

check_draw(board): Check for a draw 🤝.

computer_move(gameState, player): Smart 🤖 move logic.

choose_mode(): Pick the game mode 🎮.

final_statistics(): View final 📊 stats.

🎬 Game Flow

1️⃣ Welcome banner 🎉 and mode selection 🔢.2️⃣ Players (or 🤖s) alternate moves ➡️.3️⃣ Ends with a win 🏆 or draw 🤝.4️⃣ 📊 Stats shown at the end.

🛠️ Example Gameplay

=====================================
        Welcome to ❌⭕ Game!         
=====================================
Here's the board layout:

  1️⃣ | 2️⃣ | 3️⃣
  ---------
  4️⃣ | 5️⃣ | 6️⃣
  ---------
  7️⃣ | 8️⃣ | 9️⃣

📖 Instructions:
1️⃣ Player ❌ and Player ⭕ take turns.  
2️⃣ Choose a position (1️⃣-9️⃣).  
3️⃣ Align three to win!  
4️⃣ If full and no winner, it’s a draw 🤝.

🎮 Let the game begin!

📦 Dependencies

Install tabulate before playing:

pip install tabulate

🚀 Future Improvements

🎚️ Add 🤖 difficulty levels.

🖼️ Graphical interface 🖌️.

🌐 Online multiplayer 🌍.

📜 License

This project is 🆓 open-source under the MIT License.

