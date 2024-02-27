from config.dev import environ

AGENDA_MANAGEMENT = (
    environ.BASE_DIR / "repositories" / "caches" / "agenda_management.pkl"
)

COMPANY_POLICIES = environ.BASE_DIR / "repositories" / "caches" / "company_policies.pkl"

EMPLOYEE_FEEDBACK = (
    environ.BASE_DIR / "repositories" / "caches" / "employee_feedback.pkl"
)

EMPLOYEE_PROFILE = environ.BASE_DIR / "repositories" / "caches" / "employee_profile.pkl"

JOB_OPENINGS = environ.BASE_DIR / "repositories" / "caches" / "job_openings.pkl"

LEAVE_PLANNING = environ.BASE_DIR / "repositories" / "caches" / "leave_planning.pkl"

MEAL_PLANNING = environ.BASE_DIR / "repositories" / "caches" / "meal_planning.pkl"

PERSONAL_PROFILE = environ.BASE_DIR / "repositories" / "caches" / "personal_profile.pkl"

PROJECT_MANAGEMENT = (
    environ.BASE_DIR / "repositories" / "caches" / "project_management.pkl"
)

TEAM_INFO = environ.BASE_DIR / "repositories" / "caches" / "team_info.pkl"

TECHNICAL_QUESTIONS = (
    environ.BASE_DIR / "repositories" / "caches" / "technical_questions.pkl"
)
