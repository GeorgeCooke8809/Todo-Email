from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from todo.db import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    start_date: Mapped[datetime] = mapped_column(nullable=False)
    end_date: Mapped[datetime] = mapped_column(nullable=True) # NULL = indefinite

    # ---------- Relationships ----------

    daily_repeat: Mapped[DailyRepeat] = relationship(back_populates="event")
    weekly_repeats: Mapped[list[WeeklyRepeat]] = relationship(back_populates="event")
    monthly_repeats: Mapped[list[MonthlyRepeat]] = relationship(back_populates="event")
    exceptions: Mapped[list[Exception]] = relationship(back_populates="event")
    backlog: Mapped[list[BacklogItem]] = relationship(back_populates="event")

    # ? Add priority?


class DailyRepeat(Base):
    __tablename__ = "daily_repeats"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    frequency: Mapped[int] = mapped_column(nullable=False) # the event will repeat ever x number of days
    last_occurrence: Mapped[datetime] = mapped_column(nullable=True)

    event: Mapped[Event] = relationship(back_populates="daily_repeat")


class WeeklyRepeat(Base):
    __tablename__ = "weekly_repeats"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    week_day: Mapped[int] = mapped_column(nullable=False) # limited to 1-7
    frequency: Mapped[int] = mapped_column(nullable=False) # the event will repeat ever x number of weeks on the given day of the week
    last_occurrence: Mapped[datetime] = mapped_column(nullable=True)

    event: Mapped[Event] = relationship(back_populates="daily_repeat")


class MonthlyRepeat(Base):
    __tablename__ = "monthly_repeats"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=False)
    month_day: Mapped[int] = mapped_column(nullable=False) # The day of the month it repeats on
    last_occurrence: Mapped[datetime] = mapped_column(nullable=True)

    event: Mapped[Event] = relationship(back_populates="daily_repeat")

class Exception(Base):
    __tablename__ = "repeat_exceptions"

    # TODO: Add tags to events and make exceptions to all of a tag

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=True) # Null means no scheduled events will take place at all on this date
    date: Mapped[datetime] = mapped_column(nullable=False)

    event: Mapped[Event] = relationship(back_populates="daily_repeat")

class BacklogItem(Base):
    __tablename__ = "backlog"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), nullable=True) # Null if stand alone event
    name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[datetime] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column(nullable=False) # Options: Pending, In Progress, Complete, Cancelled

    event: Mapped[Event] = relationship(back_populates="backlog")

    # ? Add priority