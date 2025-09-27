Financial Chatbot

This project is a simple rule-based financial chatbot built in Python.  
It answers a limited set of predefined queries using data from an Excel file.

Introduction: 
The chatbot provides financial insights for companies based on historical data.  
It demonstrates how predefined queries can be mapped to dataset values using simple Python logic.

How it Works: 
1. User uploads an Excel file with company financial data.  
2. The chatbot function filters data for the given **company** and **fiscal year**.  
3. Using `if-else` conditions, it matches the user query to predefined queries and returns answers.  
4. If the query is outside the predefined set, it returns a fallback message.

Queries Supported: 
The chatbot can respond to:
1. Total Revenue – “What is the total revenue of [Company] in [Year]?”  
2. Net Income Change – “How has net income changed over the last year?”  
3. Assets & Liabilities – “What are the assets and liabilities of [Company] in [Year]?”  
4. Cash Flow – “What is the cash flow from operating activities of [Company] in [Year]?”  
5. Debt-to-Asset Ratio – “What is the debt-to-asset ratio of [Company] in [Year]?”  

Example Output: 
Q: What is the total revenue?
A: The total revenue of Apple in 2023 was 260000 million USD.

Q: How has net income changed over the last year?
A: Net income for Apple changed by 5000 million USD (8%) from 2022 to 2023.

Q: What are the assets and liabilities?
A: In 2023, Apple had assets of 300000 million USD and liabilities of 150000 million USD.

Q: What is the debt-to-asset ratio?
A: The debt-to-asset ratio of Apple in 2023 was 0.50.

