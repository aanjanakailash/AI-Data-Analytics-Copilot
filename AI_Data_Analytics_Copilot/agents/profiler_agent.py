import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_string_dtype,
    is_bool_dtype
)


class ProfilerAgent:

    def profile(self, df: pd.DataFrame):

        profile = {
            "rows": df.shape[0],
            "columns": df.shape[1],

            "numeric": [],
            "categorical": [],
            "datetime": [],
            "boolean": [],
            "id_columns": [],

            "missing": df.isnull().sum().to_dict(),
            "duplicates": int(df.duplicated().sum())
        }

        for column in df.columns:

            if is_numeric_dtype(df[column]):
                profile["numeric"].append(column)

            elif is_datetime64_any_dtype(df[column]):
                profile["datetime"].append(column)

            elif is_bool_dtype(df[column]):
                profile["boolean"].append(column)

            elif is_string_dtype(df[column]):
                profile["categorical"].append(column)

            if "id" in column.lower():
                profile["id_columns"].append(column)

        return profile