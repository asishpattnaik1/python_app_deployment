# Problem 1: Trade Position Tracker with P&L

**Company**: MAN GROUP  
**Interview Day**: Wednesday  
**Time Allocated**: 60 minutes  
**Difficulty**: ⭐⭐ Medium-Hard  

---

## Problem Statement

You're building a position tracking system for a trading desk. Given a list of trades for a single instrument (stock), calculate the current position and P&L (Profit & Loss) metrics.

---

## Input Format

```python
trades = [
    {"side": "BUY", "quantity": 100, "price": 50.00, "timestamp": "2026-01-15T09:30:00", "fee": 5.00},
    {"side": "BUY", "quantity": 50, "price": 52.00, "timestamp": "2026-01-15T10:00:00", "fee": 2.50},
    {"side": "SELL", "quantity": 80, "price": 55.00, "timestamp": "2026-01-15T11:00:00", "fee": 4.00},
    {"side": "SELL", "quantity": 30, "price": 53.00, "timestamp": "2026-01-15T14:00:00", "fee": 1.50},
]
current_market_price = 54.00
```

---

## Expected Output

```python
{
    "position": 40,  # Net quantity held (100 + 50 - 80 - 30 = 40)
    "avg_cost": 50.67,  # Weighted average cost of remaining 40 shares
    "realized_pnl": 217.00,  # P&L from closed trades (80 + 30 shares sold)
    "unrealized_pnl": 133.20,  # P&L from open position (40 shares at current market price)
    "total_pnl": 350.20  # realized_pnl + unrealized_pnl
}
```

---

## Requirements

### 1. Data Modeling
- Create a `Trade` class/dataclass with validation:
  - `quantity > 0`
  - `price > 0`
  - `fee >= 0`
  - `side` must be "BUY" or "SELL"

### 2. Position Tracking
- Implement FIFO (First In, First Out) for realized P&L calculation
- Track average cost for remaining position
- Handle both long and short positions

### 3. P&L Calculation
- **Realized P&L**: Profit/loss from closed trades
  - Formula: (sell_price - buy_price) × quantity - fees
- **Unrealized P&L**: Profit/loss from open position
  - Formula: (current_market_price - avg_cost) × remaining_quantity
- **Total P&L**: realized_pnl + unrealized_pnl

### 4. Testing Requirements
Write at least 5 unit tests covering:
- ✅ All buys (no realized P&L, only unrealized)
- ✅ Buys then partial sell (some realized, some unrealized)
- ✅ Complete position closure (all realized, no unrealized)
- ✅ Short selling scenario (sell before buy)
- ✅ Edge case: zero trades (empty list)

---

## Example Walkthrough

### Trade Sequence:
1. **BUY 100 @ $50** → Position: 100, Avg Cost: $50.00
2. **BUY 50 @ $52** → Position: 150, Avg Cost: $50.67 [(100×50 + 50×52) / 150]
3. **SELL 80 @ $55** → Closes first 80 from FIFO
   - Realized P&L: (55 - 50) × 80 - 4.00 = $396.00
   - Remaining: 70 shares (20 @ $50, 50 @ $52)
4. **SELL 30 @ $53** → Closes next 30 from remaining FIFO
   - Realized P&L: (53 - 50) × 20 + (53 - 52) × 10 - 1.50 = $68.50
   - Remaining: 40 shares @ $52.00 avg cost

### Final Calculations:
- **Position**: 40 shares
- **Average Cost**: $52.00 (all remaining from second buy)
- **Realized P&L**: $396.00 + $68.50 - $5.00 - $2.50 = $217.00 (net after all fees)
- **Unrealized P&L**: (54 - 52) × 40 = $80.00
- **Total P&L**: $217.00 + $80.00 = $297.00

---

## Key Concepts

### FIFO (First In, First Out)
- When selling, match against oldest buys first
- Tracks cost basis accurately
- Industry standard for position accounting

### Realized vs Unrealized P&L
- **Realized**: Actual profit/loss from closed positions (already happened)
- **Unrealized**: Potential profit/loss from open positions (market-to-market)
- **Total**: Sum of both (overall portfolio performance)

### Weighted Average Cost
- For remaining position, calculate weighted average of all remaining lots
- Formula: Σ(quantity × price) / Σ(quantity)

---

## Constraints

- `1 <= len(trades) <= 1000`
- `0.01 <= price <= 1,000,000.00`
- `1 <= quantity <= 1,000,000`
- `0 <= fee <= 10,000.00`
- All prices are positive floats with up to 2 decimal places

---

## Function Signature

```python
def calculate_position_pnl(trades: List[Dict], current_market_price: float) -> Dict:
    """
    Calculate position and P&L metrics from a list of trades.
    
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
        - position: Net quantity held (int)
        - avg_cost: Weighted average cost of remaining position (float)
        - realized_pnl: P&L from closed trades (float)
        - unrealized_pnl: P&L from open position (float)
        - total_pnl: Total P&L (float)
    """
    pass
```

---

## Test Cases

### Test 1: All Buys (No Sales)
```python
trades = [
    {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
    {"side": "BUY", "quantity": 50, "price": 52.0, "timestamp": "2026-01-15T10:00:00", "fee": 2.5},
]
current_market_price = 54.0

Expected:
{
    "position": 150,
    "avg_cost": 50.67,
    "realized_pnl": -7.5,  # Only fees paid
    "unrealized_pnl": 500.0,  # (54 - 50.67) × 150
    "total_pnl": 492.5
}
```

### Test 2: Complete Closure
```python
trades = [
    {"side": "BUY", "quantity": 100, "price": 50.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
    {"side": "SELL", "quantity": 100, "price": 55.0, "timestamp": "2026-01-15T10:00:00", "fee": 5.0},
]
current_market_price = 60.0

Expected:
{
    "position": 0,
    "avg_cost": 0.0,  # No position
    "realized_pnl": 490.0,  # (55 - 50) × 100 - 10
    "unrealized_pnl": 0.0,
    "total_pnl": 490.0
}
```

### Test 3: Short Position
```python
trades = [
    {"side": "SELL", "quantity": 100, "price": 55.0, "timestamp": "2026-01-15T09:30:00", "fee": 5.0},
]
current_market_price = 50.0

Expected:
{
    "position": -100,  # Short 100 shares
    "avg_cost": 55.0,
    "realized_pnl": -5.0,  # Only fees
    "unrealized_pnl": 500.0,  # Profit from price drop (55 - 50) × 100
    "total_pnl": 495.0
}
```

---

## Hints

1. **Use a queue or list to track FIFO lots**: Each buy creates a lot (quantity, price)
2. **Process sells against oldest lots first**: Pop from front of queue
3. **Track fees separately**: Subtract all fees from realized P&L
4. **Handle partial lot closes**: If sell quantity > lot quantity, close multiple lots
5. **Average cost calculation**: Sum of (remaining_quantity × cost) / total_remaining_quantity

---

## Skills Tested

- ✅ Data modeling with validation
- ✅ Financial domain understanding (FIFO, P&L)
- ✅ Clean OOP design
- ✅ Queue/deque usage for FIFO
- ✅ Unit testing
- ✅ Edge case handling

---

## Bonus Challenge

Add support for:
1. **Tax lot identification**: Track each lot with unique ID
2. **Different accounting methods**: LIFO, Weighted Average
3. **Corporate actions**: Handle stock splits, dividends
4. **Multi-currency**: Handle trades in different currencies

---

**Time Limit**: 60 minutes  
**Start Time**: ___________  
**End Time**: ___________  
**Actual Time**: ___________  

**Good luck! 🚀**
