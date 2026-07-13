class DashboardAgent:

    def generate_dashboard(self, profile):

        dashboard = {
            "kpis": [],
            "charts": [],
            "filters": []
        }

        # -------------------------
        # KPI Cards
        # -------------------------

        for column in profile["numeric"]:
            dashboard["kpis"].append(column)

        # -------------------------
        # Charts
        # -------------------------

        if profile["categorical"] and profile["numeric"]:

            dashboard["charts"].append({

                "type": "bar",

                "x": profile["categorical"][0],

                "y": profile["numeric"][0]

            })

        if profile["datetime"] and profile["numeric"]:

            dashboard["charts"].append({

                "type": "line",

                "x": profile["datetime"][0],

                "y": profile["numeric"][0]

            })

        # -------------------------
        # Filters
        # -------------------------

        for column in profile["categorical"]:

            dashboard["filters"].append(column)

        return dashboard