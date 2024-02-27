from ..chains import employee_profile, team_info, agenda_management


class ResponseGenerator:
    def employee_profile(self, user: str, query: str):
        return employee_profile.response_chain(query=query, user=user)

    def team_info(self, user: str, query: str):
        return team_info.response_chain(query=query)

    def agenda_management(self, user: str, query: str):
        return agenda_management.response_chain(query=query, user=user)
