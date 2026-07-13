import pandas as pd


class EDAAgent:

    def analyze(self, df: pd.DataFrame):

        report = {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "column_names": list(df.columns),

            "data_types": df.dtypes.astype(str),

            "missing_values": df.isnull().sum(),

            "duplicate_rows": df.duplicated().sum(),

            "summary": df.describe(include="all").transpose()

        }

        return report