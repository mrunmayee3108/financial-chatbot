import pandas as pd

def financial_chatbot(user_query, company, year, df):
    user_query = user_query.lower()

    data = df[(df['Fiscal Year'] == year) & (df['Company'].str.lower() == company.lower())]
    if data.empty:
        return f"No data found for {company} in the year {year}"

    if "revenue" in user_query:
        revenue = data['Total Revenue (USD millions)'].values[0]
        return f"The total revenue of {company} in the year {year} was ${revenue} million USD"
    
    elif "net income" in user_query or "income" in user_query:
        net_income = data['Net Income (USD millions)'].values[0]
        return f"The net income of {company} in the year {year} was ${net_income} million USD"
    
    elif "assets" in user_query or "liabilities" in user_query or "asset" in user_query:
        assets = data["Total Assets (USD millions)"].values[0]
        liabilities = data["Total Liabilities (USD millions)"].values[0]
        return f"In {year}, {company} had:\nAssets: ${assets} million USD\nLiabilities: ${liabilities} million USD"
    
    elif "cash flow" in user_query or "flow of cash" in user_query:
        cashflow = data["Cash Flow from Operating Activities (USD millions)"].values[0]
        return f"The cash flow from operating activities of {company} in {year} was ${cashflow} million USD"
    
    elif "debt" in user_query or "ratio" in user_query or "debt to asset" in user_query:
        assets = data["Total Assets (USD millions)"].values[0]
        liabilities = data["Total Liabilities (USD millions)"].values[0]
        ratio = liabilities / assets if assets != 0 else 0
        return f"The debt-to-asset ratio of {company} in {year} was {ratio:.2f} ({ratio*100:.1f}%)"
    
    else:
        return "I can only help with revenue, net income, assets/liabilities, cash flow, or debt-to-asset ratio. Contact the company for more details."

try:

    df = pd.read_excel("Large_Financials_Dataset.xlsx")
    
    print("🤖FINANCIAL CHATBOT READY!")
    print("I can answer 5 types of questions about companies:")
    print("1. Revenue\n2. Net Income\n3. Assets/Liabilities\n4. Cash Flow\n5. Debt Ratio\n")

    companies = df['Company'].unique()
    years = sorted(df['Fiscal Year'].unique())
    print(f"Available Companies: {', '.join(companies)}")
    print(f"Available Years: {min(years)} to {max(years)}\n")
    
    while True:
        print("-" * 50)

        company = input("Enter company name (or 'quit' to exit): ")
        if company.lower() in ['quit', 'exit', 'stop']:
            print("👋 Goodbye!")
            break
  
        try:
            year = int(input("Enter year: "))
        except ValueError:
            print("❌ Please enter a valid year!")
            continue

        print(f"\nReady to answer questions about {company} ({year})")
        print("Type 'change' to pick a different company/year")
        
        while True:
            question = input(f"\nEnter your question about {company}: ")
            
            if question.lower() == 'change':
                break
            elif question.lower() in ['quit', 'exit', 'stop']:
                print("👋 Goodbye!")
                exit()
            
            response = financial_chatbot(question, company, year, df)
            print(f"🤖 {response}")

except FileNotFoundError:
    print("❌ Error: Large_Financials_Dataset.xlsx not found!")
    print("Make sure the Excel file is in the same folder as this code.")
except Exception as e:
    print(f"❌ Error: {e}")