import pandas as pd


class KPIService:

    def generate(self, df):

        kpis = {}

        # Rows
        kpis["Total Rows"] = len(df)

        # Columns
        kpis["Columns"] = len(df.columns)

        # Missing Values
        kpis["Missing"] = int(df.isnull().sum().sum())

        # Numeric Columns
        numeric = df.select_dtypes(include="number").columns

        # Total Sales
        if "Total_sales" in df.columns:
            kpis["Total Sales"] = round(df["Total_sales"].sum(), 2)

        # Profit
        if "Profit" in df.columns:
            kpis["Profit"] = round(df["Profit"].sum(), 2)

        # Quantity
        if "Quantity" in df.columns:
            kpis["Quantity"] = int(df["Quantity"].sum())

        # Orders
        if "Order_ID" in df.columns:
            kpis["Orders"] = df["Order_ID"].nunique()

        # Customers
        if "Customer_ID" in df.columns:
            kpis["Customers"] = df["Customer_ID"].nunique()

        # Generic Numeric KPIs
        for col in numeric:

            if col not in [
                "Total_sales",
                "Profit",
                "Quantity"
            ]:

                kpis[f"Avg {col}"] = round(df[col].mean(),2)

        return kpis