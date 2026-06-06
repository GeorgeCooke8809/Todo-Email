from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=True) # NULL = indefinite


class DailyRepeat(Base):
    __tablename__ = "daily_repeats"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    frequency: Mapped[int] = mapped_column(nullable=False) # the event will repeat ever x number of days


class WeeklyRepeat(Base):
    __tablename__ = "weekly_repeats"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    week_day: Mapped[int] = mapped_column(nullable=False) # limited to 1-7
    frequency: Mapped[int] = mapped_column(nullable=False) # the event will repeat ever x number of weeks on the given day of the week

class MonthlyRepeat(Base):
    __tablename__ = "monthly_repeats"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    month_day: Mapped[int] = mapped_column(nullable=False) # The day of the month it repeats on

class Exception(Base):
    __tablename__ = "repeat_exceptions"

    # TODO: Add tags to events and make exceptions to all of a tag

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=True) # Null means no scheduled events will take place
    date: Mapped[datetime] = mapped_column(nullable=False)