# 📦 Deployment Guide - Moving to Your New Repository

This guide shows you how to move the `company_interview_challenges` folder to your new `coding_challenge` repository.

---

## 🎯 Quick Deploy (2 Minutes)

### Option 1: Copy via Codespaces (Easiest)

1. **In THIS repository** (python_app_deployment):
   ```bash
   cd /workspaces/python_app_deployment
   # Or wherever your Codespace is
   ```

2. **Copy the folder**:
   ```bash
   cp -r company_interview_challenges /tmp/company_interview_challenges
   ```

3. **Switch to your NEW repository** (coding_challenge):
   - Open a new Codespace for `asishpattnaik1/coding_challenge`
   - Or `cd` to where you cloned it locally

4. **Paste the folder**:
   ```bash
   cp -r /tmp/company_interview_challenges .
   ```

5. **Commit and push**:
   ```bash
   git add company_interview_challenges
   git commit -m "Add HackerRank-style interview challenges"
   git push
   ```

---

### Option 2: Download and Upload

1. **Download from THIS repo**:
   - Go to: https://github.com/asishpattnaik1/python_app_deployment
   - Navigate to `company_interview_challenges` folder
   - Click "Code" → "Download ZIP"
   - Extract the `company_interview_challenges` folder

2. **Upload to NEW repo**:
   - Go to: https://github.com/asishpattnaik1/coding_challenge
   - Click "Add file" → "Upload files"
   - Drag the `company_interview_challenges` folder
   - Commit changes

---

### Option 3: Git Clone & Move (Advanced)

```bash
# Clone both repositories
git clone https://github.com/asishpattnaik1/python_app_deployment.git
git clone https://github.com/asishpattnaik1/coding_challenge.git

# Copy the folder
cp -r python_app_deployment/company_interview_challenges coding_challenge/

# Push to new repo
cd coding_challenge
git add company_interview_challenges
git commit -m "Add HackerRank-style interview challenges"
git push origin main
```

---

## 🚀 After Deployment

### 1. Verify Structure

In your `coding_challenge` repository, you should see:

```
coding_challenge/
└── company_interview_challenges/
    ├── README.md
    ├── QUICK_START.md
    ├── man_group/
    │   ├── problems/
    │   │   └── problem_01_trade_position_tracker.md
    │   ├── solutions/
    │   │   └── problem_01_trade_position_tracker.py
    │   └── tests/
    │       └── test_problem_01.py
    └── jpmorgan/
        ├── problems/
        ├── solutions/
        └── tests/
```

### 2. Test the Setup

```bash
cd company_interview_challenges/man_group
python tests/test_problem_01.py
```

You should see:
```
🧪 Running Test Suite: Problem 1 - Trade Position Tracker
❌ Basic BUY and SELL: FAILED  # This is expected! Tests fail until you implement
...
Success Rate: 10.0%  # Only empty test passes
```

### 3. Start Coding!

```bash
# Open the first problem
cat problems/problem_01_trade_position_tracker.md

# Edit the solution
# Open: solutions/problem_01_trade_position_tracker.py

# Implement your solution and run tests
python tests/test_problem_01.py
```

---

## 📋 What You Have Now

### ✅ Complete Problem 1: Trade Position Tracker

**Files:**
- `problems/problem_01_trade_position_tracker.md` - Full problem statement
- `solutions/problem_01_trade_position_tracker.py` - Template with TODOs
- `tests/test_problem_01.py` - 10 comprehensive test cases

**Features:**
- FIFO position tracking
- P&L calculations (realized + unrealized)
- Pydantic data validation
- Full test coverage

### 📚 Documentation
- `README.md` - Complete environment overview
- `QUICK_START.md` - 5-minute getting started guide
- Problem statement with examples, hints, and walkthrough

---

## 🎯 Next Steps

### 1. Implement Problem 1
- Follow `QUICK_START.md`
- Implement the solution
- Get all tests passing
- Learn the HackerRank-style workflow

### 2. Create Remaining Problems

I'll create all remaining problems (9 more) in the same format:
- **MAN GROUP**: Problems 2-5
- **JPMORGAN**: Problems 1-5

Each will have:
- Detailed problem statement
- Solution template with TODOs
- Comprehensive test suite
- Examples and hints

### 3. Practice Interview Schedule

**Wednesday (MAN GROUP):**
- 09:00-10:00: Problem 1 ✅ (you have this)
- 10:00-11:00: Problem 2 (I'll create)
- 11:00-12:00: Problem 3 (I'll create)
- 12:00-13:00: Problem 4 (I'll create)
- 13:00-14:00: Problem 5 (I'll create)

**Thursday (JPMORGAN):**
- 09:00-10:00: Problem 1 (I'll create)
- 10:00-10:45: Problem 2 (I'll create)
- 10:45-11:45: Problem 3 (I'll create)
- 11:45-12:45: Problem 4 (I'll create)
- 12:45-13:45: Problem 5 (I'll create)

---

## 💡 Pro Tips for Using This Environment

### 1. Set Up IDE

**VS Code (Recommended):**
```bash
# Install Python extension
# Install Pylance for type checking
# Install Python Test Explorer
```

**PyCharm:**
- Configure Python interpreter
- Enable pytest
- Set up code formatting (Black)

### 2. Install Dependencies

```bash
cd company_interview_challenges
pip install pydantic pytest pytest-cov black flake8
```

### 3. Configure Auto-Testing

**VS Code** - Add to `.vscode/settings.json`:
```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"]
}
```

### 4. Use Git for Progress Tracking

```bash
# After solving each problem
git add solutions/problem_XX.py
git commit -m "Solved Problem X: [Problem Name]"
git push
```

---

## 🎓 Learning Path

### Phase 1: Setup (Today)
1. ✅ Move files to new repository
2. ✅ Test infrastructure works
3. ✅ Read documentation

### Phase 2: Problem 1 (Today/Tomorrow)
1. Read problem completely
2. Understand FIFO accounting
3. Implement solution
4. Pass all tests
5. Review and optimize

### Phase 3: Remaining Problems (This Week)
- Complete all MAN GROUP problems
- Complete all JPMORGAN problems
- Review patterns and techniques

### Phase 4: Interview Prep (Next Week)
- Time yourself on each problem
- Practice explaining your approach
- Review solutions and alternatives

---

## ❓ FAQ

**Q: Can I modify the solution templates?**
A: Yes, but keep the function names and signatures. Tests depend on them.

**Q: Can I add helper functions?**
A: Absolutely! The template shows sections for helper functions.

**Q: What if tests don't run?**
A: Check you're in the right directory and paths are correct.

**Q: Can I use external libraries?**
A: Yes, but document dependencies. Pydantic and pytest are pre-assumed.

**Q: How do I get all remaining problems?**
A: I'll create them and you can copy them the same way.

---

## 📞 Support

If you encounter issues:

1. **Check the QUICK_START.md guide**
2. **Verify file structure matches expected layout**
3. **Test with Problem 1 first** (known to work)
4. **Check Python version** (3.10+ recommended)

---

## 🎉 You're Ready!

1. ✅ Copy `company_interview_challenges` to your new repo
2. ✅ Verify tests run
3. ✅ Start with Problem 1
4. ✅ Request remaining problems from me

**Good luck with your interview prep! 💪**

---

*After you've moved this and tested Problem 1, let me know and I'll create all remaining problems!*
