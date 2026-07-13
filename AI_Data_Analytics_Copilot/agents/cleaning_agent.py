import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_string_dtype
)


class CleaningAgent:

    def clean(self, df: pd.DataFrame):

        cleaned_df = df.copy()

        # Remove duplicate rows
        cleaned_df = cleaned_df.drop_duplicates()

        # Fill missing values
        for column in cleaned_df.columns:

            if is_numeric_dtype(cleaned_df[column]):

                cleaned_df[column] = cleaned_df[column].fillna(
                    cleaned_df[column].median()
                )

            elif is_string_dtype(cleaned_df[column]):

                cleaned_df[column] = cleaned_df[column].fillna("Unknown")

            else:

                cleaned_df[column] = cleaned_df[column].fillna(
                    cleaned_df[column].mode()[0]
                )

        return cleaned_df