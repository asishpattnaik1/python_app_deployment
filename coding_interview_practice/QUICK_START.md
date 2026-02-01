# 🚀 Quick Start Guide - Get Coding in 5 Minutes!

Follow these steps to start practicing coding interviews right now.

---

## ⚡ Quick Setup (Choose Your Path)

### Option A: GitHub Codespaces (Easiest - Recommended!)

1. **Open the repository on GitHub**
   - Go to: `https://github.com/asishpattnaik1/python_app_deployment`

2. **Launch Codespace**
   - Click the green **"Code"** button
   - Click **"Codespaces"** tab
   - Click **"Create codespace on main"**
   - Wait 30 seconds for VS Code to load in browser

3. **You now have a full IDE!**
   - Navigate to `coding_interview_practice/problems/`
   - Pick a problem to solve
   - Create your solution in `coding_interview_practice/solutions/`

4. **Test your solution**
   ```bash
   # In the terminal at bottom of VS Code:
   python coding_interview_practice/solutions/two_sum.py
   ```

5. **When ready, commit and request review**
   - Use Source Control panel (left sidebar)
   - Commit your changes
   - Push to GitHub
   - Comment that you're ready for review!

### Option B: Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/asishpattnaik1/python_app_deployment.git
   cd python_app_deployment
   ```

2. **Open in your favorite IDE**
   - VS Code: `code .`
   - PyCharm: Open folder
   - Or any other IDE

3. **Start coding!**
   - Navigate to `coding_interview_practice/`
   - Pick a problem, write solution
   - Test locally

4. **Push and get review**
   ```bash
   git add coding_interview_practice/solutions/your_solution.py
   git commit -m "Solution: Problem Name"
   git push
   ```

---

## 📝 Your First Problem (5-Minute Tutorial)

Let's solve **Two Sum** together:

### Step 1: Read the Problem
Open: `coding_interview_practice/problems/two_sum.md`

**Quick summary:** Given array and target, find two numbers that sum to target.

### Step 2: Open the Solution Template
Open: `coding_interview_practice/solutions/two_sum.py`

You'll see a template with TODO comments.

### Step 3: Think About the Approach

**Brute Force (O(n²)):**
```python
# Try every pair - nested loops
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Optimal (O(n)):**
```python
# Use hash map for O(1) lookup
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Step 4: Write Your Solution

Pick an approach and implement it in the template!

### Step 5: Test It

Run the file:
```bash
python coding_interview_practice/solutions/two_sum.py
```

Or run the automated tests:
```bash
python coding_interview_practice/tests/test_two_sum.py
```

### Step 6: Document Your Approach

Fill in the template comments:
```python
"""
Approach:
I use a hash map to store numbers I've seen. For each number,
I check if its complement (target - num) exists in the map.
This gives us O(n) time with O(n) space.

Time Complexity: O(n)
Space Complexity: O(n)
"""
```

### Step 7: Request Review

Once your tests pass:
1. Commit your solution
2. Push to GitHub  
3. Comment: "Ready for review on Two Sum solution!"

---

## 🎯 Recommended Learning Path

### Week 1: Arrays & Strings (Easy Problems)
1. ✅ Two Sum
2. ✅ Valid Palindrome
3. Try these patterns:
   - Hash maps for fast lookup
   - Two pointers for arrays/strings

### Week 2: Linked Lists (Easy Problems)
1. ✅ Reverse Linked List
2. Practice pointer manipulation
3. Draw diagrams!

### Week 3: Trees (Easy → Medium)
1. ✅ Binary Tree Level Order Traversal
2. Learn BFS and DFS
3. Practice recursion

### Week 4: Dynamic Programming (Medium)
1. ✅ Maximum Subarray
2. Learn Kadane's Algorithm
3. Build from subproblems

---

## 🧪 Testing Your Solutions

### Run Individual Solution
```bash
cd /home/runner/work/python_app_deployment/python_app_deployment
python coding_interview_practice/solutions/two_sum.py
```

### Run Automated Tests
```bash
# Single problem tests
python coding_interview_practice/tests/test_two_sum.py

# All tests (if pytest installed)
pytest coding_interview_practice/tests/ -v
```

---

## 💡 Pro Tips

### While Solving:

1. **Read Twice, Code Once**
   - Understand the problem fully first
   - Identify edge cases
   - Plan before coding

2. **Start Simple**
   - Get a working solution first
   - Then optimize
   - Brute force → Better approach

3. **Test Early, Test Often**
   - Run after each significant change
   - Check edge cases manually
   - Use provided test files

4. **Use the Template**
   - It guides your thinking
   - Documents your approach
   - Makes review easier

### Code Quality Checklist:

- [ ] Descriptive variable names (not `x`, `y`, `temp`)
- [ ] Comments explain WHY, not WHAT
- [ ] Edge cases handled (empty, null, negatives)
- [ ] Time/space complexity documented
- [ ] Code is readable and clean
- [ ] Tests pass ✅

---

## 🆘 Stuck? Try This:

1. **Re-read the Problem**
   - Often we misunderstand the requirements

2. **Try Examples by Hand**
   - Walk through the examples step-by-step
   - What pattern do you notice?

3. **Think About Simpler Versions**
   - What if array had only 2 elements?
   - What if all numbers were positive?

4. **Look at Hints**
   - Check the problem file for hints
   - Don't go straight to solutions!

5. **Take a Break**
   - Sometimes stepping away helps
   - Come back with fresh eyes

6. **Ask Questions**
   - Clarify with me if stuck
   - Real interviews encourage questions!

---

## 📊 Track Your Progress

Keep a simple log:

```
Problem: Two Sum
Date: 2026-02-01
Time Taken: 25 min
Difficulty: Easy
Status: ✅ Solved
Approach: Hash map
Complexity: O(n) time, O(n) space
Feedback: [Wait for review]
Learnings: Hash maps are great for O(1) lookup!
```

---

## 🎯 What to Expect in Reviews

I'll provide feedback on:

1. **Correctness** - Does it work?
2. **Efficiency** - Is it optimal?
3. **Code Quality** - Is it clean?
4. **Edge Cases** - Did you handle them?
5. **Explanation** - Can you articulate your approach?

Example feedback snippet:
```
✅ Strengths:
- Correct solution with optimal O(n) time
- Good variable names
- Handled edge cases well

⚠️ Areas for Improvement:
- Consider what happens if input is empty
- Add a comment explaining why you use a hash map

💡 Next Steps:
- Try Valid Palindrome (similar two-pointer pattern)
```

---

## 🎓 Before Your First Review

Make sure you have:

- [x] Read the problem completely
- [x] Implemented a working solution
- [x] Tested with provided examples
- [x] Thought about edge cases
- [x] Documented time/space complexity
- [x] Cleaned up your code
- [x] Can explain your approach

---

## 🚀 Ready? Let's Go!

1. **Pick a problem** from `problems/` folder
2. **Write your solution** in `solutions/` folder
3. **Test it** using the test files
4. **Commit and push** your code
5. **Request review** and get feedback!

**Start with Two Sum - it's a classic for a reason! 🎯**

---

## 📚 More Resources

- `README.md` - Full environment documentation
- `INTERVIEW_GUIDE.md` - Detailed review process
- `problems/` - All problem statements
- `solutions/` - Your solution files
- `tests/` - Automated test files

**Questions? Just ask! I'm here to help you improve. 💪**
