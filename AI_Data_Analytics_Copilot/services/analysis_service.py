import pandas as pd


class AnalysisService:

    @staticmethod
    def analyze(df):

        analysis = {}

        # Total Sales by City
        if "City" in df.columns and "Total_Amount" in df.columns:

            analysis["city_sales"] = (
                df.groupby("City")["Total_Amount"]
                .sum()
                .sort_values(ascending=False)
                .to_string()
            )

        # Orders by City
        if "City" in df.columns:

            analysis["city_orders"] = (
                df.groupby("City")
                .size()
                .sort_values(ascending=False)
                .to_string()
            )

        # Product Category Sales
        if "Product_Category" in df.columns and "Total_Amount" in df.columns:

            analysis["category_sales"] = (
                df.groupby("Product_Category")["Total_Amount"]
                .sum()
                .sort_values(ascending=False)
                .to_string()
            )

        # Payment Mode
        if "Payment_Mode" in df.columns:

            analysis["payment_mode"] = (
                df["Payment_Mode"]
                .value_counts()
                .to_string()
            )

        # Order Status
        if "Order_Status" in df.columns:

            analysis["order_status"] = (
                df["Order_Status"]
                .value_counts()
                .to_string()
            )

        return analysis