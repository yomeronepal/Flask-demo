from dataclasses import dataclass

@dataclass(frozen=True  )
class TodoDomain:
    content: int