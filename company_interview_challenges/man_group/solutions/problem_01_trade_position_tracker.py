"""
Problem 1: Trade Position Tracker with P&L
Company: MAN GROUP
Time: 60 minutes

Instructions:
1. Read the problem statement in problems/problem_01_trade_position_tracker.md
2. Implement the required functions below
3. Run tests: python tests/test_problem_01.py
4. All tests must pass for full credit

Scoring:
- Correctness: 40% (all tests pass)
- Code Quality: 25% (clean, readable code)
- Efficiency: 20% (optimal algorithm)
- Testing: 15% (comprehensive tests)
"""

from dataclasses import dataclass
from typing import List, Dict
from collections import deque
from enum import Enum


class Side(str, Enum):
    """Trade side enumeration."""
    BUY = "BUY"
    SELL = "SELL"


@dataclass
class Trade:
    """
    Represents a single trade.
    
    TODO: Add validation:
    - quantity must be > 0
    - price must be > 0
    - fee must be >= 0
    """
    side: Side
    quantity: int
    price: float
    timestamp: str
    fee: float
    
    def __post_init__(self):
        """Add validation here."""
        # TODO: Implement validation
        pass


def calculate_position_pnl(trades: List[Dict], current_market_price: float) -> Dict:
    """
    Calculate position and P&L metrics from a list of trades.
    
    This is the main function you need to implement using FIFO accounting.
    
    Args:
        trades: List of trade dictionaries with keys:
                - side: "BUY" or "SELL"
                - quantity: int (positive)
                - price: float (positive)
                - timestamp: str (ISO format)
                - fee: float (non-negative)
        current_market_price: Current market price for unrealized P&L
        
    Returns:
        Dictionary with keys:
        - position: Net quantity held (int, can be negative for short)
        - avg_cost: Weighted average cost of remaining position (float)
        - realized_pnl: P&L from closed trades (float)
        - unrealized_pnl: P&L from open position (float)
        - total_pnl: Total P&L (float)
        
    Algorithm Hints:
    1. Use FIFO (First In, First Out) for matching sells against buys
    2. Track lots in a queue: [(quantity, price), ...]
    3. For each SELL, match against oldest BUY lots
    4. Calculate realized P&L as: (sell_price - buy_price) × quantity - fees
    5. Calculate unrealized P&L on remaining position
    
    Example:
        >>> trades = [
        ...     {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        ...     {"side": "SELL", "quantity": 50, "price": 55.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
        ... ]
        >>> result = calculate_position_pnl(trades, 54.0)
        >>> result["position"]
        50
        >>> result["realized_pnl"]
        242.5
    """
    # TODO: Implement this function
    
    # Initialize tracking variables
    buy_lots = deque()  # Queue of (quantity, price) for FIFO
    realized_pnl = 0.0
    total_fees = 0.0
    
    # Process each trade
    for trade_data in trades:
        # TODO: Convert dict to Trade object
        # TODO: Validate trade
        
        side = trade_data["side"]
        quantity = trade_data["quantity"]
        price = trade_data["price"]
        fee = trade_data["fee"]
        
        total_fees += fee
        
        if side == "BUY":
            # TODO: Add to buy_lots queue
            pass
        elif side == "SELL":
            # TODO: Match against buy_lots using FIFO
            # TODO: Calculate realized P&L for matched trades
            pass
    
    # Calculate remaining position and average cost
    # TODO: Calculate position (sum of remaining lots)
    # TODO: Calculate avg_cost (weighted average of remaining lots)
    
    position = 0  # TODO: Calculate
    avg_cost = 0.0  # TODO: Calculate
    
    # Calculate unrealized P&L
    # TODO: unrealized_pnl = (current_market_price - avg_cost) × position
    unrealized_pnl = 0.0
    
    # Adjust realized P&L for fees
    realized_pnl -= total_fees
    
    # Calculate total P&L
    total_pnl = realized_pnl + unrealized_pnl
    
    return {
        "position": position,
        "avg_cost": round(avg_cost, 2),
        "realized_pnl": round(realized_pnl, 2),
        "unrealized_pnl": round(unrealized_pnl, 2),
        "total_pnl": round(total_pnl, 2)
    }


# ============================================================================
# HELPER FUNCTIONS (Optional - implement if needed)
# ============================================================================

def validate_trade(trade: Dict) -> None:
    """
    Validate trade data.
    
    Args:
        trade: Trade dictionary
        
    Raises:
        ValueError: If validation fails
    """
    # TODO: Implement validation
    pass


def calculate_weighted_average_cost(lots: deque) -> float:
    """
    Calculate weighted average cost of remaining lots.
    
    Args:
        lots: Deque of (quantity, price) tuples
        
    Returns:
        Weighted average cost
    """
    # TODO: Implement
    pass


# ============================================================================
# TESTING SECTION - Run this file to test your implementation
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Testing Problem 1: Trade Position Tracker with P&L")
    print("=" * 80)
    
    # Test Case 1: Basic BUY and SELL
    print("\n📝 Test 1: Basic BUY and SELL")
    trades_1 = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "BUY", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
        {"side": "SELL", "quantity": 80, "price": 55.0, "timestamp": "2026-01-15T11:00:00", "fee": 4.0},
        {"side": "SELL", "quantity": 30, "price": 53.0, "timestamp": "2026-01-15T14:00:00", "fee": 1.5},
    ]
    result_1 = calculate_position_pnl(trades_1, 54.0)
    print(f"Result: {result_1}")
    print(f"Expected position: 40")
    print(f"Expected avg_cost: ~50.67")
    print(f"Expected realized_pnl: ~217.00")
    print(f"Expected unrealized_pnl: ~133.20")
    print(f"Expected total_pnl: ~350.20")
    
    # Test Case 2: All Buys (No Sells)
    print("\n📝 Test 2: All Buys (No realized P&L)")
    trades_2 = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "BUY", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
    ]
    result_2 = calculate_position_pnl(trades_2, 54.0)
    print(f"Result: {result_2}")
    print(f"Expected position: 150")
    print(f"Expected realized_pnl: -7.5 (just fees)")
    
    # Test Case 3: Complete Closure
    print("\n📝 Test 3: Complete Position Closure")
    trades_3 = [
        {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
        {"side": "SELL", "quantity": 100, "price": 55.0, "timestamp": "2026-01-15T10:00:00", "fee": 5.0},
    ]
    result_3 = calculate_position_pnl(trades_3, 60.0)
    print(f"Result: {result_3}")
    print(f"Expected position: 0")
    print(f"Expected realized_pnl: 490.0")
    print(f"Expected unrealized_pnl: 0.0")
    
    # Test Case 4: Empty trades
    print("\n📝 Test 4: Empty Trades List")
    trades_4 = []
    result_4 = calculate_position_pnl(trades_4, 50.0)
    print(f"Result: {result_4}")
    print(f"Expected: all zeros")
    
    print("\n" + "=" * 80)
    print("✅ Manual testing complete! Run 'python tests/test_problem_01.py' for full test suite")
    print("=" * 80)
