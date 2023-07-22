from dataclasses import dataclass


@dataclass(frozen=True)
class TodoDomain:
    title: str
    date: str
    description: str
