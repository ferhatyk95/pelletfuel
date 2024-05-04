# Define a class to represent a SWOT analysis
class SWOTAnalysis:
    def __init__(self, strengths, weaknesses, opportunities, threats):
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.opportunities = opportunities
        self.threats = threats

    def analyze(self):
        print("SWOT Analysis:")
        print("Strengths:")
        for strength in self.strengths:
            print(f"- {strength}")
        print("Weaknesses:")
        for weakness in self.weaknesses:
            print(f"- {weakness}")
        print("Opportunities:")
        for opportunity in self.opportunities:
            print(f"- {opportunity}")
        print("Threats:")
        for threat in self.threats:
            print(f"- {threat}")

# Define a class to represent a profit-loss table
class ProfitLossTable:
    def __init__(self, revenues, costs):
        self.revenues = revenues
        self.costs = costs

    def generate_table(self):
        print("Profit-Loss Table:")
        print("Revenues:")
        for revenue in self.revenues:
            print(f"- {revenue}")
        print("Costs:")
        for cost in self.costs:
            print(f"- {cost}")
        profit = sum(self.revenues) - sum(self.costs)
        print(f"Profit: {profit}")

# Create a SWOT analysis instance
swot_analysis = SWOTAnalysis(
    strengths=["High-quality products", "Skilled employees", "Strong brand"],
    weaknesses=["High production costs", "Limited market share", "Dependence on few suppliers"],
    opportunities=["Growing demand for eco-friendly products", "Expansion into new markets", "Partnership with a leading technology company"],
    threats=["Increasing competition", "Economic downturn", "Regulatory changes"]
)

# Create a profit-loss table instance
profit_loss_table = ProfitLossTable(
    revenues=["Sales revenue: $100,000", "Interest income: $5,000"],
    costs=["Production costs: $60,000", "Marketing expenses: $20,000", "Salaries: $30,000"]
)

# Perform the SWOT analysis and generate the profit-loss table
swot_analysis.analyze()
profit_loss_table.generate_table()