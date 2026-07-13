import streamlit as st
import pandas as pd

from services.chart_service import ChartService


def show_dashboard(df, profile):

    st.header("📊 Smart Dashboard")

    chart = ChartService()

    cols = chart.detect_columns(df)

    numeric = cols["numeric"]
    categorical = cols["categorical"]

    value_col = chart.detect_measure_column(df)
    date_col = chart.detect_date_column(df)

    # -----------------------------
    # KPI Cards
    # -----------------------------

    kpi = chart.generate_kpis(df)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Rows", kpi["rows"])
    c2.metric("Columns", kpi["columns"])
    c3.metric("Missing Values", kpi["missing"])
    c4.metric("Memory (MB)", kpi["memory"])

    st.divider()

    # -----------------------------
    # Time Trend
    # -----------------------------

    if date_col is not None and value_col is not None:

        try:

            temp = df.copy()

            temp[date_col] = pd.to_datetime(temp[date_col])

            trend = (
                temp.groupby(date_col)[value_col]
                .sum()
                .reset_index()
            )

            st.subheader("📈 Time Trend")

            fig = chart.line_chart(
                trend,
                date_col,
                value_col,
                f"{value_col} Over Time"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            pass

    # -----------------------------
    # Category Analysis
    # -----------------------------

    if len(categorical) > 0 and value_col is not None:

        st.divider()

        st.subheader("📊 Category Analysis")

        for col in categorical:

            # Skip ID columns
            if "id" in col.lower():
                continue

            try:

                grouped = (
                    df.groupby(col)[value_col]
                    .sum()
                    .reset_index()
                )

                unique = grouped[col].nunique()

                if unique <= 10:

                    fig = chart.pie_chart(
                        grouped,
                        col,
                        value_col,
                        f"{value_col} by {col}"
                    )

                elif unique <= 30:

                    fig = chart.bar_chart(
                        grouped,
                        col,
                        value_col,
                        f"{value_col} by {col}"
                    )

                else:

                    grouped = grouped.nlargest(10, value_col)

                    fig = chart.bar_chart(
                        grouped,
                        col,
                        value_col,
                        f"Top 10 {col}"
                    )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            except:
                continue

    # -----------------------------
    # Numeric Distribution
    # -----------------------------

    if len(numeric) > 0:

        st.divider()

        st.subheader("📉 Numeric Distribution")

        for col in numeric:

            c1, c2 = st.columns(2)

            with c1:

                try:
                    fig = chart.histogram(df, col)
                    st.plotly_chart(fig, use_container_width=True)
                except:
                    pass

            with c2:

                try:
                    fig = chart.box_plot(df, col)
                    st.plotly_chart(fig, use_container_width=True)
                except:
                    pass

    # -----------------------------
    # Scatter Plot
    # -----------------------------

    if len(numeric) >= 2:

        try:

            st.divider()

            st.subheader("🎯 Scatter Plot")

            fig = chart.scatter_chart(
                df,
                numeric[0],
                numeric[1],
                f"{numeric[0]} vs {numeric[1]}"
            )

            st.plotly_chart(fig, use_container_width=True)

        except:
            pass

    # -----------------------------
    # Correlation Heatmap
    # -----------------------------

    if len(numeric) >= 2:

        try:

            st.divider()

            st.subheader("🔥 Correlation Heatmap")

            fig = chart.heatmap(df)

            st.plotly_chart(fig, use_container_width=True)

        except:
            pass

    # -----------------------------
    # Missing Values
    # -----------------------------

    try:

        fig = chart.missing_chart(df)

        if fig is not None:

            st.divider()

            st.subheader("⚠ Missing Values")

            st.plotly_chart(fig, use_container_width=True)

    except:
        pass