# api/services/analytics_service.py

import time

class AnalyticsService:

    def __init__(self):
        self.total_requests = 0
        self.chat_requests = 0
        self.tool_usage = {}
        self.popular_queries = {}
        self.start_time = time.time()

    def track_request(self):
        self.total_requests += 1

    def track_chat(self, query: str):
        self.chat_requests += 1
        self.popular_queries[query] = \
            self.popular_queries.get(query, 0) + 1

    def track_tool(self, tool_name: str):
        self.tool_usage[tool_name] = \
            self.tool_usage.get(tool_name, 0) + 1

    def get_analytics(self):
        uptime = round(time.time() - self.start_time, 2)

        return {
            "total_requests": self.total_requests,
            "chat_requests": self.chat_requests,
            "tool_usage": self.tool_usage,
            "popular_queries": self.popular_queries,
            "uptime_seconds": uptime
        }


# Create single global instance
analytics_service = AnalyticsService()