#!/bin/bash

# ============================================================================
# 🚀 SIMPLE DEPLOYMENT SCRIPT - Copy to New Repository
# ============================================================================
# This script helps you copy the interview practice folders to your new repo
# ============================================================================

set -e  # Exit on error

echo "════════════════════════════════════════════════════════════════════════"
echo "🚀 Deployment Script - Copy Interview Practice Folders"
echo "════════════════════════════════════════════════════════════════════════"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "📍 Current directory: $SCRIPT_DIR"
echo ""

# Check if folders exist
if [ ! -d "$SCRIPT_DIR/company_interview_challenges" ]; then
    echo "❌ ERROR: company_interview_challenges folder not found!"
    exit 1
fi

if [ ! -d "$SCRIPT_DIR/coding_interview_practice" ]; then
    echo "❌ ERROR: coding_interview_practice folder not found!"
    exit 1
fi

echo "✅ Found company_interview_challenges folder"
echo "✅ Found coding_interview_practice folder"
echo ""

# Ask user for the new repository path
echo "════════════════════════════════════════════════════════════════════════"
echo "📂 Where is your new 'coding_challenge' repository?"
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "Examples:"
echo "  • If in Codespaces: /workspaces/coding_challenge"
echo "  • If local: /home/yourname/coding_challenge"
echo "  • If local (Mac): /Users/yourname/coding_challenge"
echo ""
read -p "Enter the full path to your coding_challenge repository: " NEW_REPO_PATH

# Expand ~ to home directory if present
NEW_REPO_PATH="${NEW_REPO_PATH/#\~/$HOME}"

echo ""
echo "You entered: $NEW_REPO_PATH"
echo ""

# Check if the new repo exists
if [ ! -d "$NEW_REPO_PATH" ]; then
    echo "❌ ERROR: Directory $NEW_REPO_PATH does not exist!"
    echo ""
    echo "Please make sure you:"
    echo "  1. Created the repository on GitHub"
    echo "  2. Cloned it locally or opened it in Codespaces"
    echo "  3. Entered the correct path"
    exit 1
fi

echo "✅ Found the new repository at: $NEW_REPO_PATH"
echo ""

# Confirm before copying
echo "════════════════════════════════════════════════════════════════════════"
echo "📋 Ready to copy the following folders:"
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "  FROM: $SCRIPT_DIR"
echo "    • company_interview_challenges/"
echo "    • coding_interview_practice/"
echo ""
echo "  TO: $NEW_REPO_PATH"
echo ""
read -p "Continue? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "❌ Aborted by user"
    exit 0
fi

echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo "🚚 Copying folders..."
echo "════════════════════════════════════════════════════════════════════════"
echo ""

# Copy company_interview_challenges
echo "📦 Copying company_interview_challenges..."
cp -r "$SCRIPT_DIR/company_interview_challenges" "$NEW_REPO_PATH/"
echo "   ✅ Done!"
echo ""

# Copy coding_interview_practice
echo "📦 Copying coding_interview_practice..."
cp -r "$SCRIPT_DIR/coding_interview_practice" "$NEW_REPO_PATH/"
echo "   ✅ Done!"
echo ""

echo "════════════════════════════════════════════════════════════════════════"
echo "✅ COPY COMPLETE!"
echo "════════════════════════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo ""
echo "1. Change to your new repository:"
echo "   cd $NEW_REPO_PATH"
echo ""
echo "2. Check what was copied:"
echo "   ls -la"
echo ""
echo "3. Add the files to git:"
echo "   git add company_interview_challenges coding_interview_practice"
echo ""
echo "4. Commit the files:"
echo "   git commit -m \"Add interview practice environments\""
echo ""
echo "5. Push to GitHub:"
echo "   git push origin main"
echo ""
echo "6. Test the setup:"
echo "   cd company_interview_challenges/man_group"
echo "   python tests/test_problem_01.py"
echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo "🎉 All done! Your interview practice environment is ready!"
echo "════════════════════════════════════════════════════════════════════════"
