class DAXAgent:

    def generate(self, profile):

        measures = []

        for column in profile["numeric"]:

            measures.append({
                "name": f"Total {column}",
                "formula": f"SUM(Data[{column}])"
            })

        return measures