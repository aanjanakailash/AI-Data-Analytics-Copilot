class Router:

    QUERY_KEYWORDS = [
        "top",
        "highest",
        "lowest",
        "maximum",
        "minimum",
        "average",
        "avg",
        "sum",
        "count",
        "list",
        "show",
        "display",
        "sales",
        "profit",
        "customer",
        "city",
        "product",
        "category",
        "payment",
        "order"
    ]

    INSIGHT_KEYWORDS = [
        "why",
        "reason",
        "increase",
        "decrease",
        "improve",
        "recommend",
        "suggest",
        "insight",
        "trend",
        "strategy",
        "opportunity",
        "future"
    ]

    def detect(self, question):

        q = question.lower()

        for word in self.INSIGHT_KEYWORDS:
            if word in q:
                return "insight"

        for word in self.QUERY_KEYWORDS:
            if word in q:
                return "query"

        return "query"