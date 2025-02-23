from typing import Dict, Optional
from pydantic import BaseModel, Field

class TaxExpenses(BaseModel):
    current_tax: Optional[int] = Field(None, alias="Current Tax")
    deferred_tax: Optional[int] = Field(None, alias="Deferred Tax")
    total_tax_expenses: Optional[int] = Field(None, alias="Total Tax Expenses")


class FinancialStatement(BaseModel):
    revenue_from_operations: Optional[int] = Field(None, alias="Revenue From Operations")
    other_income: Optional[int] = Field(None, alias="Other Income")
    total_revenue: Optional[int] = Field(None, alias="Total Revenue")

    cost_of_materials_consumed: Optional[int] = Field(None, alias="Cost Of Materials Consumed")
    purchases_of_stock_in_trade: Optional[int] = Field(None, alias="Purchases Of Stock-in-trade")
    changes_in_inventories: Optional[int] = Field(None, alias="Changes In Inventories of Finished Goods,Stock-in-Trade and Work-in-Progress")

    employee_benefit_expenses: Optional[int] = Field(None, alias="Employee Benefit Expenses")
    finance_cost: Optional[int] = Field(None, alias="Finance Cost")
    depreciation_and_amortisation_expenses: Optional[int] = Field(None, alias="Depreciation And Amortisation Expenses")
    other_expenses: Optional[int] = Field(None, alias="Other Expenses")

    total_expenses: Optional[int] = Field(None, alias="Total Expenses")
    profit_loss_before_exceptional_items_and_tax: Optional[int] = Field(None, alias="Profit/Loss Before Exceptional Items And Tax")
    profit_loss_before_tax: Optional[int] = Field(None, alias="Profit/Loss Before Tax")

    tax_expenses: Optional[TaxExpenses] = Field(None, alias="Tax Expenses")
    net_profit_loss_for_the_period: Optional[int] = Field(None, alias="Net Profit/Loss For The Period From Continuing Operations")


class FinancialResults(BaseModel):
    quarter_ended: Optional[Dict[str, FinancialStatement]] = Field(None, alias="Quarter Ended")
    nine_months_ended: Optional[Dict[str, FinancialStatement]] = Field(None, alias="Nine Month Ended")
    year_ended: Optional[Dict[str, FinancialStatement]] = Field(None, alias="Year Ended")


class FullFinancialData(BaseModel):
    standalone_financial_results: FinancialResults = Field(..., alias="Standalone Financial Results For All Months")
    balance_sheet: Optional[str] = Field(None, alias="Balance Sheet")
    cash_flow_statements: Optional[str] = Field(None, alias="Cash Flow Statements")
    consolidated_financial_results: FinancialResults = Field(..., alias="Statement Consolidated Finanacial Results For All Months")