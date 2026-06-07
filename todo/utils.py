from todo.models import Event, DailyRepeat, WeeklyRepeat, MonthlyRepeat, Exception, BacklogItem
from todo.db import session
from sqlalchemy.orm import query
from main import DEBUGGING_STATE
from datetime import datetime

# TODO Add these functions


def add_standalone_event(name: str, date: datetime):
    pass


def add_repeating_event(name: str, repeats: list[dict], start_date: datetime, end_date: datetime = None):
    pass


def add_daily_repeat(event_id: int, repeat_frequency: int, start_date: datetime):
    pass


def add_weekly_repeat(event_id: int, day_of_week: int, repeat_frequency: int, start_date: datetime):
    if day_of_week <= 0 or day_of_week >= 8:
        raise ValueError(f"Error adding weekly repeat. Day of week must be between 1 and 7 inclusive. {day_of_week = }")


def add_monthly_repeat():
    pass


def add_exception():
    pass

def create_backlog(name: str, date: str, state: str = "Pending", event_id: int = None):
    pass


def update_status(event_id: int, new_status: str):
    if new_status not in ["Pending", "In Progress", "Done", "Cancelled"]:
        raise ValueError(f'Update status new status is not valid option. Options are: "Pending", "In Progress", "Done", and "Cancelled" (all are case sensitive). {new_status = }')