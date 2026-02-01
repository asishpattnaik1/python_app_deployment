# 🚀 Quick Start Guide - Company Interview Challenges

**Get started in 5 minutes!**

---

## ⚡ Setup (30 seconds)

### If you're in GitHub Codespaces:
```bash
# You're already set up! Just navigate to the folder:
cd company_interview_challenges
```

### If you're local:
```bash
# Clone the repo (if not already done)
git clone https://github.com/asishpattnaik1/coding_challenge.git
cd coding_challenge

# Install dependencies
pip install pydantic pytest
```

---

## 📝 Your First Problem (5 minutes)

### Step 1: Choose a Problem (10 seconds)
```bash
cd man_group/problems
cat problem_01_trade_position_tracker.md
```

### Step 2: Open Solution Template (10 seconds)
```bash
cd ../solutions
# Open in your editor: problem_01_trade_position_tracker.py
```

The file already has:
- ✅ Function signatures
- ✅ Type hints  
- ✅ Docstrings
- ✅ TODO comments guiding you
- ✅ Example code structure

**You just write the logic!**

### Step 3: Implement Your Solution (40 minutes)

Find the TODO comments and implement:
```python
def calculate_position_pnl(trades: List[Dict], current_market_price: float) -> Dict:
    # TODO: Implement this function
    
    buy_lots = deque()  # Already set up for you!
    # ... rest of your logic here
```

### Step 4: Test Your Solution (5 minutes)

Run the test file:
```bash
cd ../tests
python test_problem_01.py
```

You'll see:
```
================================================================================
🧪 Running Test Suite: Problem 1 - Trade Position Tracker
================================================================================
✅ Basic BUY and SELL: PASSED
✅ All buys, no sells: PASSED
✅ Complete position closure: PASSED
...

📊 TEST RESULTS
Total Tests: 10
✅ Passed: 10
❌ Failed: 0
Success Rate: 100.0%

🎉 ALL TESTS PASSED! Great job!
Score: 100% ⭐⭐⭐
```

### Step 5: Submit (30 seconds)
```bash
git add .
git commit -m "Solved Problem 1: Trade Position Tracker"
git push
```

**Done! Move to next problem!** 🎉

---

## 🎯 HackerRank-Style Workflow

```
1. Read Problem     →  problems/problem_XX.md
2. Write Code       →  solutions/problem_XX.py  
3. Run Tests        →  python tests/test_problem_XX.py
4. See Results      →  Instant pass/fail feedback
5. Fix & Retry      →  Iterate until 100%
6. Submit           →  git commit & push
```

---

## 📁 File Structure

```
company_interview_challenges/
│
├── man_group/              # Wednesday - MAN GROUP
│   ├── problems/           # Problem statements
│   │   ├── problem_01_trade_position_tracker.md
│   │   ├── problem_02_multi_currency_portfolio.md
│   │   ├── problem_03_trade_validator.md
│   │   ├── problem_04_pnl_report_generator.md
│   │   └── problem_05_market_data_analyzer.md
│   │
│   ├── solutions/          # YOUR CODE HERE
│   │   ├── problem_01_trade_position_tracker.py
│   │   ├── problem_02_multi_currency_portfolio.py
│   │   └── ...
│   │
│   └── tests/              # Auto-grading tests
│       ├── test_problem_01.py
│       ├── test_problem_02.py
│       └── ...
│
└── jpmorgan/               # Thursday - JPMORGAN
    ├── problems/
    ├── solutions/
    └── tests/
```

---

## 🧪 Running Tests

### Single Problem
```bash
python tests/test_problem_01.py
```

### With Pytest (more details)
```bash
pytest tests/test_problem_01.py -v
```

### All Problems
```bash
pytest tests/ -v
```

### See Coverage
```bash
pytest tests/test_problem_01.py --cov=solutions --cov-report=html
```

---

## 💡 Pro Tips

### 1. Read Twice, Code Once
- Understand ALL requirements before coding
- Note the edge cases mentioned
- Check the example walkthrough

### 2. Use the Template Structure
- Don't rename functions or change signatures
- Tests expect exact function names
- Follow the TODO comments

### 3. Test Early, Test Often
```bash
# After writing each function:
python solutions/problem_01_trade_position_tracker.py
```

### 4. Debug with Print Statements
```python
# Add these to see what's happening:
print(f"DEBUG: buy_lots = {buy_lots}")
print(f"DEBUG: realized_pnl = {realized_pnl}")
```

### 5. Check Test Output Carefully
```
❌ Basic BUY and SELL: FAILED
   Position should be 40, got 35
```
This tells you exactly what's wrong!

---

## 🎓 Interview Day Schedule

### Wednesday - MAN GROUP (5 hours)
- **09:00-10:00**: Problem 1 - Trade Position Tracker
- **10:00-11:00**: Problem 2 - Multi-Currency Portfolio  
- **11:00-12:00**: Problem 3 - Trade Validator
- **12:00-13:00**: Problem 4 - P&L Report Generator
- **13:00-14:00**: Problem 5 - Market Data Analyzer

### Thursday - JPMORGAN (4.75 hours)
- **09:00-10:00**: Problem 1 - Trade Message Validator
- **10:00-10:45**: Problem 2 - Refactor Messy Code
- **10:45-11:45**: Problem 3 - Order Book Processor
- **11:45-12:45**: Problem 4 - Settlement Calculator
- **12:45-13:45**: Problem 5 - Trade Reconciliation

---

## ⏱️ Time Management

### For 60-Minute Problems:
- **0-10 min**: Read & understand problem
- **10-15 min**: Plan approach (pseudocode)
- **15-45 min**: Implement solution
- **45-55 min**: Test & debug
- **55-60 min**: Final review & edge cases

### For 45-Minute Problems:
- **0-5 min**: Read problem
- **5-10 min**: Plan
- **10-35 min**: Code
- **35-45 min**: Test

---

## 🐛 Common Issues

### Import Errors
```python
# Make sure you're running from the right directory
cd company_interview_challenges/man_group
python tests/test_problem_01.py
```

### Function Not Found
```
❌ Import Error: cannot import name 'calculate_position_pnl'
```
→ Check function name matches exactly (including capitalization)

### Tests All Fail
```
❌ All tests: FAILED
```
→ You probably haven't implemented the function yet (that's OK!)

---

## 📊 Scoring

Each problem scored out of 100:
- **40 points**: Correctness (all tests pass)
- **25 points**: Code quality (clean, readable)
- **20 points**: Efficiency (optimal algorithm)
- **15 points**: Testing (handles edge cases)

**70+ = Pass | 90+ = Excellent**

---

## 🆘 Stuck?

1. **Re-read the problem statement**
2. **Check the example walkthrough section**
3. **Look at the hints section**
4. **Review the test cases** - they show expected behavior
5. **Try the simpler test cases first**
6. **Draw it out on paper**

---

## ✅ Checklist Before Submitting

- [ ] Read problem statement completely
- [ ] Implemented all required functions
- [ ] All tests pass (100%)
- [ ] Tested edge cases
- [ ] Code is clean and commented
- [ ] Time complexity documented
- [ ] Ready for review

---

## 🎯 Ready?

```bash
# Start with Problem 1
cd man_group/problems
cat problem_01_trade_position_tracker.md

# Set a timer for 60 minutes
# Start coding!
```

**Good luck! 🚀**

---

*Remember: This is practice. Learn from mistakes. Iterate and improve!*
