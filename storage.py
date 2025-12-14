import json
from pathlib import Path
from models import Board, Column, Card, demo_board

DATA_FILE = Path("boards.json")


def board_to_dict(board: Board) -> dict:
    return {
        "id": board.id,
        "title": board.title,
        "columns": [
            {
                "id": c.id,
                "title": c.title,
                "cards": [
                    {
                        "id": card.id,
                        "title": card.title,
                        "description": card.description,
                        "completed": card.completed,
                    }
                    for card in c.cards
                ],
            }
            for c in board.columns
        ],
    }


def board_from_dict(data: dict) -> Board:
    cols = []
    for c in data.get("columns", []):
        cards = [
            Card(
                id=cd["id"],
                title=cd["title"],
                description=cd.get("description", ""),
                completed=cd.get("completed", False),
            )
            for cd in c.get("cards", [])
        ]
        cols.append(Column(id=c["id"], title=c["title"], cards=cards))
    return Board(id=data["id"], title=data["title"], columns=cols)


def load_board() -> Board:
    if not DATA_FILE.exists():
        return demo_board()
    raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return board_from_dict(raw)


def save_board(board: Board) -> None:
    DATA_FILE.write_text(
        json.dumps(board_to_dict(board), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
