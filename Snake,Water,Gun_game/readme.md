# 🐍 Snake Water Gun Game in Python

A simple Python implementation of the classic **Snake Water Gun** game, where the user plays against the computer. The computer randomly selects its choice, and the program determines the winner based on the game's rules.

---

## 📌 Features

* User vs Computer gameplay
* Random computer choice using Python's `random` module
* Input validation
* Displays both player's and computer's choices
* Determines the winner based on game rules
* Beginner-friendly Python project

---

## 🎮 Game Rules

* 🐍 Snake drinks Water → **Snake Wins**
* 💧 Water damages Gun → **Water Wins**
* 🔫 Gun kills Snake → **Gun Wins**
* If both players choose the same option → **Draw**

---

## 🛠️ Technologies Used

* Python 3
* `random` module

---

## 📂 Project Structure

```text
Snake-Water-Gun/
│
├── snake_water_gun.py
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/Snake-Water-Gun.git
```

2. Navigate to the project folder:

```bash
cd Snake-Water-Gun
```

3. Run the Python program:

```bash
python snake_water_gun.py
```

---

## 💻 Sample Output

```text
Enter your choice (s = Snake, w = Water, g = Gun): s

You chose: Snake
Computer chose: Gun
💻 Computer Wins!
```

---

## 📖 How It Works

1. The computer randomly chooses **Snake**, **Water**, or **Gun**.
2. The user enters one of the following:

   * `s` for Snake
   * `w` for Water
   * `g` for Gun
3. The program compares both choices.
4. It displays whether the user wins, loses, or the game ends in a draw.

---

## 📚 Concepts Used

* Variables
* Dictionaries
* Conditional Statements (`if`, `elif`, `else`)
* User Input (`input()`)
* Random Number Generation
* Basic Game Logic

---

## 🚀 Future Improvements

* Add score tracking
* Play multiple rounds
* Add a graphical user interface (GUI)
* Add difficulty levels
* Keep a history of previous matches

---

## 👨‍💻 Author

**Divyaprakash Himanshu**

B.Tech – Computer Science Engineering (Data Science)

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
