"""
Test Suite for Problem 1: Trade Position Tracker with P&L
Company: MAN GROUP

Run with: python test_problem_01.py
Or: pytest test_problem_01.py -v
"""

import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "solutions"))

try:
    from problem_01_trade_position_tracker import calculate_position_pnl, Trade, Side
except ImportError as e:
    print(f"❌ Import Error: {e}")
    print("Make sure problem_01_trade_position_tracker.py exists in solutions/")
    sys.exit(1)


def test_basic_buy_and_sell():
    """Test Case 1: Basic BUY and SELL with FIFO"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "BUY", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
        {"side": "SELL", "quantity": 80, "price": 55.0, "timestamp": "2026-01-15T11:00:00", "fee": 4.0},
        {"side": "SELL", "quantity": 30, "price": 53.0, "timestamp": "2026-01-15T14:00:00", "fee": 1.5},
    ]
    result = calculate_position_pnl(trades, 54.0)
    
    assert result["position"] == 40, f"Position should be 40, got {result['position']}"
    assert abs(result["avg_cost"] - 50.67) < 0.5, f"Avg cost should be ~50.67, got {result['avg_cost']}"
    assert abs(result["realized_pnl"] - 217.0) < 10, f"Realized P&L should be ~217.0, got {result['realized_pnl']}"
    assert abs(result["unrealized_pnl"] - 133.2) < 10, f"Unrealized P&L should be ~133.2, got {result['unrealized_pnl']}"
    assert abs(result["total_pnl"] - 350.2) < 10, f"Total P&L should be ~350.2, got {result['total_pnl']}"


def test_all_buys_no_sells():
    """Test Case 2: All buys, no sells (only unrealized P&L)"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "BUY", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
    ]
    result = calculate_position_pnl(trades, 54.0)
    
    assert result["position"] == 150, f"Position should be 150, got {result['position']}"
    assert abs(result["avg_cost"] - 50.67) < 0.5, f"Avg cost should be ~50.67, got {result['avg_cost']}"
    assert result["realized_pnl"] < 0, f"Realized P&L should be negative (fees), got {result['realized_pnl']}"
    assert result["unrealized_pnl"] > 0, f"Unrealized P&L should be positive, got {result['unrealized_pnl']}"


def test_complete_position_closure():
    """Test Case 3: Complete position closure (all realized)"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "SELL", "quantity": 100, "price": 55.0, "timestamp": "2026-01-15T10:00:00", "fee": 5.0},
    ]
    result = calculate_position_pnl(trades, 60.0)
    
    assert result["position"] == 0, f"Position should be 0, got {result['position']}"
    assert result["avg_cost"] == 0.0, f"Avg cost should be 0, got {result['avg_cost']}"
    assert abs(result["realized_pnl"] - 490.0) < 1.0, f"Realized P&L should be ~490, got {result['realized_pnl']}"
    assert result["unrealized_pnl"] == 0.0, f"Unrealized P&L should be 0, got {result['unrealized_pnl']}"


def test_empty_trades():
    """Test Case 4: Empty trades list"""
    trades = []
    result = calculate_position_pnl(trades, 50.0)
    
    assert result["position"] == 0, f"Position should be 0, got {result['position']}"
    assert result["avg_cost"] == 0.0, f"Avg cost should be 0, got {result['avg_cost']}"
    assert result["realized_pnl"] == 0.0, f"Realized P&L should be 0, got {result['realized_pnl']}"
    assert result["unrealized_pnl"] == 0.0, f"Unrealized P&L should be 0, got {result['unrealized_pnl']}"
    assert result["total_pnl"] == 0.0, f"Total P&L should be 0, got {result['total_pnl']}"


def test_short_position():
    """Test Case 5: Short selling scenario"""
    trades = [
        {"side": "SELL", "quantity": 100, "price": 55.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
    ]
    result = calculate_position_pnl(trades, 50.0)
    
    assert result["position"] == -100, f"Position should be -100 (short), got {result['position']}"
    # Short position should have profit when price drops
    assert result["unrealized_pnl"] > 0, f"Unrealized P&L should be positive (shorted at 55, now 50), got {result['unrealized_pnl']}"


def test_partial_sell():
    """Test Case 6: Partial sell (part of position closed)"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "SELL", "quantity": 50, "price": 55.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
    ]
    result = calculate_position_pnl(trades, 54.0)
    
    assert result["position"] == 50, f"Position should be 50, got {result['position']}"
    assert result["avg_cost"] == 50.0, f"Avg cost should be 50.0, got {result['avg_cost']}"
    assert result["realized_pnl"] > 0, f"Realized P&L should be positive, got {result['realized_pnl']}"
    assert result["unrealized_pnl"] > 0, f"Unrealized P&L should be positive, got {result['unrealized_pnl']}"


def test_multiple_buys_single_sell():
    """Test Case 7: Multiple buys at different prices, then single sell"""
    trades = [
        {"side": "BUY", "quantity": 50, "price": 48.0, "timestamp": "2026-01-15T09:00:00", "fee": 2.0},
        {"side": "BUY", "quantity": 50, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 2.5},
        {"side": "BUY", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
        {"side": "SELL", "quantity": 100, "price": 55.0, "timestamp": "2026-01-15T11:00:00", "fee": 5.0},
    ]
    result = calculate_position_pnl(trades, 54.0)
    
    assert result["position"] == 50, f"Position should be 50, got {result['position']}"
    # Remaining 50 should be from the last buy at $52
    assert result["avg_cost"] == 52.0, f"Avg cost should be 52.0, got {result['avg_cost']}"


def test_price_increase_scenario():
    """Test Case 8: Price increase (profit scenario)"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 40.0, "timestamp": "2026-01-15T09:00:00", "fee": 4.0},
        {"side": "BUY", "quantity": 100, "price": 42.0, "timestamp": "2026-01-15T10:00:00", "fee": 4.0},
    ]
    result = calculate_position_pnl(trades, 50.0)
    
    assert result["position"] == 200, f"Position should be 200, got {result['position']}"
    assert result["total_pnl"] > 0, f"Total P&L should be positive (bought low, price high), got {result['total_pnl']}"


def test_price_decrease_scenario():
    """Test Case 9: Price decrease (loss scenario)"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 60.0, "timestamp": "2026-01-15T09:00:00", "fee": 6.0},
        {"side": "BUY", "quantity": 100, "price": 58.0, "timestamp": "2026-01-15T10:00:00", "fee": 5.0},
    ]
    result = calculate_position_pnl(trades, 50.0)
    
    assert result["position"] == 200, f"Position should be 200, got {result['position']}"
    assert result["total_pnl"] < 0, f"Total P&L should be negative (bought high, price low), got {result['total_pnl']}"


def test_alternating_buys_sells():
    """Test Case 10: Alternating buys and sells"""
    trades = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:00:00", "fee": 5.0},
        {"side": "SELL", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T09:30:00", "fee": 2.5},
        {"side": "BUY", "quantity": 100, "price": 51.0, "timestamp": "2026-01-15T10:00:00", "fee": 5.0},
        {"side": "SELL", "quantity": 75, "price": 53.0, "timestamp": "2026-01-15T10:30:00", "fee": 3.5},
    ]
    result = calculate_position_pnl(trades, 54.0)
    
    assert result["position"] == 75, f"Position should be 75, got {result['position']}"
    assert result["realized_pnl"] is not None, "Realized P&L should be calculated"
    assert result["unrealized_pnl"] is not None, "Unrealized P&L should be calculated"


# ============================================================================
# TEST RUNNER
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("🧪 Running Test Suite: Problem 1 - Trade Position Tracker")
    print("=" * 80)
    
    tests = [
        ("Basic BUY and SELL", test_basic_buy_and_sell),
        ("All buys, no sells", test_all_buys_no_sells),
        ("Complete position closure", test_complete_position_closure),
        ("Empty trades", test_empty_trades),
        ("Short position", test_short_position),
        ("Partial sell", test_partial_sell),
        ("Multiple buys, single sell", test_multiple_buys_single_sell),
        ("Price increase scenario", test_price_increase_scenario),
        ("Price decrease scenario", test_price_decrease_scenario),
        ("Alternating buys and sells", test_alternating_buys_sells),
    ]
    
    passed = 0
    failed = 0
    errors = []
    
    for test_name, test_func in tests:
        try:
            test_func()
            print(f"✅ {test_name}: PASSED")
            passed += 1
        except AssertionError as e:
            print(f"❌ {test_name}: FAILED")
            print(f"   {str(e)}")
            errors.append((test_name, str(e)))
            failed += 1
        except Exception as e:
            print(f"💥 {test_name}: ERROR")
            print(f"   {str(e)}")
            errors.append((test_name, f"ERROR: {str(e)}"))
            failed += 1
    
    print("\n" + "=" * 80)
    print(f"📊 TEST RESULTS")
    print("=" * 80)
    print(f"Total Tests: {len(tests)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"Success Rate: {(passed/len(tests)*100):.1f}%")
    
    if errors:
        print("\n" + "=" * 80)
        print("❌ FAILED TESTS DETAILS:")
        print("=" * 80)
        for test_name, error in errors:
            print(f"\n{test_name}:")
            print(f"  {error}")
    
    print("\n" + "=" * 80)
    if failed == 0:
        print("🎉 ALL TESTS PASSED! Great job!")
        print("Score: 100% ⭐⭐⭐")
    elif passed >= len(tests) * 0.7:
        print("👍 Most tests passed. Review the failures and fix them.")
        print(f"Score: {(passed/len(tests)*100):.0f}%")
    else:
        print("📚 Keep working on it. Review the problem requirements.")
        print(f"Score: {(passed/len(tests)*100):.0f}%")
    print("=" * 80)
    
    sys.exit(0 if failed == 0 else 1)
