import pandas as pd


class PandasExecutor:

    @staticmethod
    def execute(df: pd.DataFrame, code: str):

        local_vars = {
            "df": df.copy(),
            "result": None,
            "pd": pd
        }

        try:
            exec(code, {}, local_vars)
            return local_vars["result"], None

        except Exception as e:
            return None, str(e)