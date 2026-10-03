# 🪨 Rock Paper Scissors Game

A simple **Rock Paper Scissors** game built using **Python**.
The player competes against the computer for **5 rounds**, and the final scores are displayed at the end.

## 🎮 Features

* 🪨 Rock, 📄 Paper, and ✂️ Scissors choices
* 🤖 Computer makes a random choice
* 👤 User enters their choice
* 🔄 Game runs for **5 rounds**
* 🏆 Winner is decided based on the final score
* 📊 Displays the user's and computer's marks
* ⚖️ Handles tie rounds

## 🛠️ Technologies Used

* **Python 3**
* `random` module

## 📋 How the Game Works

The rules are:

| User Choice | Computer Choice | Result    |
| ----------- | --------------- | --------- |
| Rock 🪨     | Scissors ✂️     | User Wins |
| Paper 📄    | Rock 🪨         | User Wins |
| Scissors ✂️ | Paper 📄        | User Wins |
| Same Choice | Same Choice     | Tie       |

The computer randomly selects one of the three choices.

The player enters:

```text
1 → Rock
2 → Paper
3 → Scissors
```

Each round:

* **User wins:** User gets 1 mark
* **Computer wins:** Computer gets 1 mark
* **Tie:** No marks are awarded

After 5 rounds, the final scores are compared.

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rock-paper-scissors.git
```

### 2. Open the Project Folder

```bash
cd rock-paper-scissors
```

### 3. Run the Python Program

```bash
python rock_paper_scissors.py
```

## 💻 Example

```text
---------- Round 1 ----------
Your Turn: Rock(1), Paper(2), Scissors(3): 1

Computer chose: Scissors
You chose: Rock
You win!

---------- Round 2 ----------
Your Turn: Rock(1), Paper(2), Scissors(3): 2

Computer chose: Paper
You chose: Paper
It's a tie!

...

========== FINAL SCORE ==========
Your marks: 3
Computer marks: 2
You won the game!
```

## 📂 Project Structure

```text
rock-paper-scissors/
│
├── rock_paper_scissors.py
└── README.md
```

## 📚 What I Learned

While creating this project, I practiced:

* Python functions
* `if-elif-else` statements
* `for` loops
* User input
* Random number generation
* Variables and score tracking
* Basic game logic
* Working with GitHub repositories

## 🔮 Future Improvements

Some features that can be added later:

* Add difficulty levels
* Allow the user to choose the number of rounds
* Add a graphical user interface (GUI)
* Add sound effects
* Store game history
* Add multiplayer mode

## 👩‍💻 Author

**Disha Rana**

B.Tech CSE (AI & ML) Student

---

⭐ If you like this project, consider giving the repository a star!
