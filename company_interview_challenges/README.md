# 🏢 Company Interview Challenges - HackerRank Style

Welcome to your professional interview preparation environment! This setup mimics HackerRank's interview platform to help you practice real company interview problems.

---

## 📁 Structure

```
company_interview_challenges/
├── README.md (this file)
├── man_group/          # Wednesday Interview Problems
│   ├── problems/       # Problem statements
│   ├── solutions/      # Your solutions go here
│   └── tests/          # Automated test cases
└── jpmorgan/           # Thursday Interview Problems
    ├── problems/       # Problem statements
    ├── solutions/      # Your solutions go here
    └── tests/          # Automated test cases
```

---

## 🎯 Interview Schedule

### Wednesday - MAN GROUP (5 Problems, 5 Hours)
1. **Trade Position Tracker with P&L** (60 min) - OOP, Financial domain
2. **Multi-Currency Portfolio Exposure** (60 min) - Currency conversion, Pydantic
3. **Real-time Trade Validator** (60 min) - Business rules, Validation
4. **Daily P&L Report Generator** (60 min) - Data aggregation, Performance
5. **Market Data Price Series Analyzer** (60 min) - Financial metrics, Statistics

### Thursday - JPMORGAN (5 Problems, 5 Hours)
1. **Trade Message Validator** (60 min) - Pydantic mastery, Validation
2. **Refactor Messy Code** (45 min) - Code review, Clean code
3. **Order Book Event Processor** (60 min) - Event-driven, State management
4. **Trade Settlement Calculator** (60 min) - Date arithmetic, Business logic
5. **Trade Reconciliation System** (60 min) - Data comparison, Reporting

---

## 🚀 Quick Start (HackerRank Style)

### Step 1: Choose a Problem
```bash
# Navigate to the company and problem
cd man_group/problems/
cat problem_01_trade_position_tracker.md
```

### Step 2: Open Solution Template
```bash
# Solution file is pre-created with structure
cd ../solutions/
# Edit: problem_01_trade_position_tracker.py
```

### Step 3: Run Tests Locally
```bash
# Test your solution
python ../tests/test_problem_01.py

# Or run with pytest
pytest ../tests/test_problem_01.py -v
```

### Step 4: Validate Solution
```bash
# Run all tests for the problem
python solutions/problem_01_trade_position_tracker.py
```

---

## 💻 HackerRank-Style Features

### ✅ What You Get:

1. **Pre-structured Templates**
   - Function signatures already defined
   - Type hints included
   - Docstrings with examples
   - You just write the logic!

2. **Instant Validation**
   - Run tests immediately
   - See exactly what passed/failed
   - Compare expected vs actual output

3. **Test Cases Included**
   - Basic cases
   - Edge cases
   - Performance cases
   - Hidden test cases (revealed after submission)

4. **Time Limits**
   - Each problem has a recommended time
   - Practice under interview pressure
   - Track your completion time

5. **Auto-grading**
   - Tests show pass/fail immediately
   - Point system for partial credit
   - Performance metrics

---

## 📋 How to Work on Problems

### 1. Read the Problem
- Understand requirements thoroughly
- Note input/output formats
- Check constraints and edge cases
- Review example test cases

### 2. Plan Your Approach
- Think about data structures
- Consider time/space complexity
- Identify edge cases
- Plan your classes/functions

### 3. Implement Solution
- Use the provided template
- Follow the function signatures
- Add your logic
- Keep code clean and documented

### 4. Test Locally
- Run basic tests first
- Add your own test cases
- Handle edge cases
- Optimize if needed

### 5. Submit for Review
- Commit your solution
- Request code review
- Get feedback on approach
- Iterate and improve

---

## 🎓 Interview Tips

### Time Management
- **60-minute problems**: Spend 10 min planning, 40 min coding, 10 min testing
- **45-minute problems**: Spend 5 min planning, 30 min coding, 10 min testing
- Don't get stuck! Move on if blocked, come back later

### Code Quality
- Use meaningful variable names
- Add comments for complex logic
- Follow PEP 8 style guide
- Write modular, testable code

### Testing Strategy
- Test with provided examples first
- Think about edge cases (empty input, single element, large data)
- Test boundary conditions
- Consider performance with large inputs

### Communication
- Add docstrings explaining your approach
- Comment on time/space complexity
- Explain trade-offs you considered
- Ask clarifying questions if needed

---

## 🧪 Testing Your Solutions

### Run Single Test File
```bash
python tests/test_problem_01.py
```

### Run with Pytest (Detailed)
```bash
pytest tests/test_problem_01.py -v
```

### Run All Tests for a Company
```bash
# All MAN GROUP tests
pytest man_group/tests/ -v

# All JPMORGAN tests
pytest jpmorgan/tests/ -v
```

### Run Tests with Coverage
```bash
pytest tests/test_problem_01.py --cov=solutions --cov-report=html
```

---

## 📊 Scoring Rubric

Each problem is scored on:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Correctness** | 40% | All tests pass, handles edge cases |
| **Code Quality** | 25% | Clean, readable, well-structured |
| **Efficiency** | 20% | Optimal time/space complexity |
| **Testing** | 15% | Comprehensive test coverage |

**Passing Score**: 70% or higher
**Excellent**: 90% or higher

---

## 🔧 Development Setup

### Required Dependencies
```bash
pip install pydantic pytest pytest-cov
```

### Optional (for better experience)
```bash
pip install black flake8 mypy  # Code formatting and type checking
```

### IDE Setup
- **VS Code**: Recommended extensions
  - Python
  - Pylance
  - Python Test Explorer
- **PyCharm**: Built-in Python support
- **Codespaces**: Everything pre-configured

---

## 📚 Domain Knowledge Reference

### Financial Terms You'll Encounter:
- **P&L (Profit & Loss)**: Realized and unrealized gains/losses
- **FIFO (First In, First Out)**: Position accounting method
- **Position**: Net long/short quantity held
- **Notional**: Total value (quantity × price)
- **Settlement**: Trade finalization date (T+1, T+2)
- **Order Book**: List of buy/sell orders at different prices
- **Bid/Ask**: Best buy price / Best sell price
- **Spread**: Difference between bid and ask

### Python Concepts You'll Use:
- **Pydantic**: Data validation and settings management
- **Dataclasses**: Structured data containers
- **Enums**: Type-safe constants
- **Type Hints**: Static type checking
- **Decorators**: @validator, @property
- **Collections**: defaultdict, deque, OrderedDict

---

## 🎯 Problem Difficulty

| Level | Problems | Time | Skills |
|-------|----------|------|--------|
| ⭐ Medium | 1, 3, 5 (MAN), 2, 4 (JPM) | 45-60 min | Core Python, Domain knowledge |
| ⭐⭐ Medium-Hard | 2, 4 (MAN), 1, 5 (JPM) | 60 min | Pydantic, Complex logic |
| ⭐⭐⭐ Hard | 3 (JPM) | 60 min | System design, State management |

---

## 📖 Additional Resources

### Pydantic Documentation
- Official docs: https://docs.pydantic.dev/
- Validation: Custom validators, root validators
- Models: BaseModel, Field, validators

### Testing
- pytest docs: https://docs.pytest.org/
- unittest: Python standard library
- Test patterns: AAA (Arrange, Act, Assert)

### Financial Concepts
- Trade lifecycle basics
- Settlement conventions
- Position accounting (FIFO, LIFO, Weighted Average)
- Market data structures

---

## ✨ Success Tips

1. **Start with the easiest**: Build confidence
2. **Read carefully**: Understand all requirements
3. **Plan before coding**: 10 minutes planning saves 30 minutes debugging
4. **Test incrementally**: Don't wait until the end
5. **Use Pydantic**: It will save you validation headaches
6. **Think edge cases**: Empty inputs, zeros, negatives, very large numbers
7. **Time yourself**: Practice under pressure
8. **Review solutions**: Learn from feedback

---

## 🚨 Common Pitfalls to Avoid

- ❌ Not handling edge cases (empty lists, None values)
- ❌ Forgetting to validate input data
- ❌ Using wrong data structures (list when dict is better)
- ❌ Not considering time complexity with large datasets
- ❌ Poor variable naming (x, tmp, data)
- ❌ No docstrings or comments
- ❌ Not testing with provided examples first
- ❌ Over-complicating simple problems

---

## 📞 Getting Help

**Stuck on a problem?**
1. Re-read the requirements
2. Check the example inputs/outputs
3. Draw out the logic on paper
4. Try a simpler version first
5. Look at test cases for hints
6. Ask for clarification on requirements

**Found a bug in tests?**
- Report it immediately
- Provide example that fails
- Suggest fix if possible

---

## 🎉 Ready to Start?

1. **Choose your interview day**: MAN GROUP (Wed) or JPMORGAN (Thu)
2. **Pick problem 1**: Start with the first problem
3. **Set a timer**: 60 minutes for most problems
4. **Code & test**: Use the HackerRank-style workflow
5. **Submit**: Commit and request review

**Good luck with your interview prep! You've got this! 💪**

---

*This environment is designed to simulate real HackerRank interview experiences. Treat each problem as if you're in an actual interview.*
