
def roi_calculator(use_case, initial_investment, operational_cost, yearly_revenue):
    
    # Net yearly profit
    net_profit = yearly_revenue - operational_cost
    
    # ROI percentage
    roi_percentage = (net_profit / initial_investment) * 100
    
    # Break-even years
    if net_profit > 0:
        break_even_years = initial_investment / net_profit
    else:
        break_even_years = "Not achievable (No profit)"
    
    # Profitability status
    if net_profit > 0:
        status = "Profitable"
    else:
        status = "Not Profitable"
    
    
    print("Use Case:", use_case)
    print("Net Yearly Profit: ₹", net_profit)
    print("ROI Percentage:", round(roi_percentage, 2), "%")
    print("Break-even Time:", break_even_years, "years")
    print("Status:", status)