
class ParticipantSlots:

    __slots__ = ['name', 'score', 'penalty']

    def __init__(self, name: str, score: int, penalty: int) -> None:
        self.name = name
        self.score = int(score)
        self.penalty = int(penalty)

    def __getitem__(cls, field):
        return getattr(cls, field)

    def __lt__(self, other) -> bool:
        if other.score == self.score and other.penalty == self.penalty:
            return self.name < other.name
        elif other.score == self.score:
            return self.penalty < other.penalty
        return self.score < other.score

    def __str__(self):
        return f'{self.name}'
