import pandas as pd
import plotly.express as px


class ChartService:

    # -----------------------------
    # Detect Columns
    # -----------------------------

    def detect_columns(self, df):

        numeric = df.select_dtypes(include=["int64", "float64", "int32", "float32"]).columns.tolist()

        categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()

        date = []

        for col in df.columns:

            if "date" in col.lower():
                date.append(col)
                continue

            try:
                converted = pd.to_datetime(df[col], errors="raise")

                if converted.notna().sum() > len(df) * 0.8:
                    date.append(col)

            except:
                pass

        return {
            "numeric": numeric,
            "categorical": categorical,
            "date": date
        }

    # -----------------------------
    # Detect Best Measure Column
    # -----------------------------

    def detect_measure_column(self, df):

        priority = [

            "sales",
            "revenue",
            "amount",
            "profit",
            "income",
            "cost",
            "price",
            "quantity",
            "qty",
            "score",
            "rating"

        ]

        numeric = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

        if len(numeric) == 0:
            return None

        for p in priority:

            for col in numeric:

                if p in col.lower():
                    return col

        return numeric[0]

    # -----------------------------
    # Detect Date Column
    # -----------------------------

    def detect_date_column(self, df):

        cols = self.detect_columns(df)

        if len(cols["date"]) == 0:
            return None

        return cols["date"][0]

    # -----------------------------
    # KPI
    # -----------------------------

    def generate_kpis(self, df):

        return {

            "rows": len(df),

            "columns": len(df.columns),

            "missing": int(df.isnull().sum().sum()),

            "memory": round(df.memory_usage(deep=True).sum()/1024**2,2)

        }

    # -----------------------------
    # Charts
    # -----------------------------

    def bar_chart(self, df, x, y, title):
        return px.bar(df, x=x, y=y, title=title)

    def line_chart(self, df, x, y, title):
        return px.line(df, x=x, y=y, markers=True, title=title)

    def pie_chart(self, df, names, values, title):
        return px.pie(df, names=names, values=values, title=title)

    def scatter_chart(self, df, x, y, title):
        return px.scatter(df, x=x, y=y, title=title)

    def histogram(self, df, column):
        return px.histogram(df, x=column, title=f"{column} Distribution")

    def box_plot(self, df, column):
        return px.box(df, y=column, title=f"{column} Outliers")

    def heatmap(self, df):

        corr = df.select_dtypes(include="number").corr()

        return px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Correlation Heatmap"
        )

    def missing_chart(self, df):

        missing = df.isnull().sum()

        missing = missing[missing > 0]

        if len(missing) == 0:
            return None

        missing = missing.reset_index()

        missing.columns = ["Column", "Missing"]

        return px.bar(
            missing,
            x="Column",
            y="Missing",
            title="Missing Values"
        )