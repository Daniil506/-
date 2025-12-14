from dataclasses import dataclass, field
from typing import List
import uuid


def make_id() -> str:
    return str(uuid.uuid4())


@dataclass
class Card:
    id: str
    title: str
    description: str = ""
    completed: bool = False


@dataclass
class Column:
    id: str
    title: str
    cards: List[Card] = field(default_factory=list)


@dataclass
class Board:
    id: str
    title: str
    columns: List[Column] = field(default_factory=list)


def demo_board() -> Board:
    todo = Column(
        id=make_id(),
        title="Неделя",
        cards=[
            Card(id=make_id(), title="Найти заказ на видеомонтаж", completed=False),
            Card(id=make_id(), title="Выложить пост в ВК с фото", completed=False),
            Card(id=make_id(), title="Улучшить личный сайт", completed=False),
        ],
    )
    done = Column(
        id=make_id(),
        title="Готово",
        cards=[
            Card(id=make_id(), title="Выложить фото в фотобанк", completed=True),
        ],
    )
    return Board(
        id=make_id(),
        title="Задачи",
        columns=[todo, done],
    )
