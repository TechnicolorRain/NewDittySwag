import pandas as pd

# Data collected from the web search
data = [
    {'title': 'Subscription Box Market Size Share, Growth, Trends 2024-2032', 'market_size': 'USD 31.85 billion', 'growth_rate': '18.4%'},
    {'title': 'North America Subscription Box Market Size, Share 2024-2032', 'market_size': 'Not specified', 'growth_rate': '16.8%'},
    {'title': 'Subscription Box Market - IMARC Group', 'market_size': 'USD 32.9 Billion', 'growth_rate': '14%'},
    {'title': 'Subscription Box Market Size, Share, Growth, And Industry Analysis by ...', 'market_size': 'USD 22000 million', 'growth_rate': '19.51 %'},
    {'title': 'Subscription Box Market Size, Industry Trends Report | 2031', 'market_size': 'USD 27 Billion', 'growth_rate': '18.4%'},
    {'title': 'Subscription Box Market Growth, Trends, Share, Analysis, Demand ...', 'market_size': 'Not specified', 'growth_rate': 'Not specified'},
    {'title': 'Global Subscription Box Market to Reach US$ 73.6 Billion by 2028', 'market_size': 'USD 28.1 Billion', 'growth_rate': 'Not specified'}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Calculate the average growth rate
average_growth_rate = df['growth_rate'].str.rstrip('%').astype('float').mean()

average_growth_rate