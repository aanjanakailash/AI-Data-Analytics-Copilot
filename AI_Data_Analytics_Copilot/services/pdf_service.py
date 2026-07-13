from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


class PDFService:

    def __init__(self):
        self.styles = getSampleStyleSheet()

    def generate(
        self,
        filename,
        dataset_name,
        df,
        profile,
        insights,
        dax
    ):

        doc = SimpleDocTemplate(filename)

        elements = []

        # ==========================
        # Cover Page
        # ==========================

        elements.append(
            Paragraph(
                "<font size=22><b>AI Data Analytics Report</b></font>",
                self.styles["Title"]
            )
        )

        elements.append(Spacer(1, 0.3 * inch))

        elements.append(
            Paragraph(
                f"<b>Dataset :</b> {dataset_name}",
                self.styles["Heading2"]
            )
        )

        elements.append(Spacer(1, 0.4 * inch))

        # ==========================
        # Dataset Summary
        # ==========================

        elements.append(
            Paragraph(
                "<b>Dataset Summary</b>",
                self.styles["Heading1"]
            )
        )

        summary = [

            ["Rows", str(df.shape[0])],
            ["Columns", str(df.shape[1])],
            ["Missing Values", str(df.isnull().sum().sum())],
            ["Duplicate Rows", str(df.duplicated().sum())]

        ]

        table = Table(summary)

        table.setStyle(

            TableStyle(

                [

                    ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),

                ]

            )

        )

        elements.append(table)

        elements.append(Spacer(1, 0.4 * inch))

        # ==========================
        # Dataset Profile
        # ==========================

        elements.append(
            Paragraph(
                "<b>Dataset Profile</b>",
                self.styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                str(profile),
                self.styles["BodyText"]
            )
        )

        elements.append(Spacer(1, 0.4 * inch))

        # ==========================
        # AI Insights
        # ==========================

        elements.append(
            Paragraph(
                "<b>AI Insights</b>",
                self.styles["Heading1"]
            )
        )

        if insights:

            elements.append(
                Paragraph(
                    str(insights),
                    self.styles["BodyText"]
                )
            )

        else:

            elements.append(
                Paragraph(
                    "AI Insights were not generated.",
                    self.styles["BodyText"]
                )
            )

        elements.append(Spacer(1, 0.4 * inch))

        # ==========================
        # DAX Measures
        # ==========================

        elements.append(
            Paragraph(
                "<b>DAX Measures</b>",
                self.styles["Heading1"]
            )
        )

        if dax:

            elements.append(
                Paragraph(
                    str(dax),
                    self.styles["BodyText"]
                )
            )

        else:

            elements.append(
                Paragraph(
                    "DAX Measures were not generated.",
                    self.styles["BodyText"]
                )
            )

        # ==========================
        # Build PDF
        # ==========================

        doc.build(elements)

        return filename