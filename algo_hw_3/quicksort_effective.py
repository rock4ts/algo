# 83540474

from collections import namedtuple
from typing import NamedTuple


def separate_by_pivot(competitors: list, left: int, right: int) -> int:
    pivot = competitors[right]
    pivot_ix = left - 1

    for j in range(left, right):
        if competitors[j] <= pivot:
            pivot_ix += 1
            competitors[pivot_ix], competitors[j] = (
                competitors[j], competitors[pivot_ix]
            )
    pivot_ix += 1
    competitors[pivot_ix], competitors[right] = (
        competitors[right], competitors[pivot_ix]
    )
    return pivot_ix


def quicksort_effective(competitors: list, left: int, right: int) -> None:
    if left < right:
        pivot_ix = separate_by_pivot(competitors, left, right)
        quicksort_effective(competitors, left, pivot_ix - 1)
        quicksort_effective(competitors, pivot_ix + 1, right)


def prepare_competitor_data(
        competitor: list, NamedTupleFactory: type
    ) -> NamedTuple:
    return NamedTupleFactory(
        -int(competitor[1]), int(competitor[2]), competitor[0]
    )


if __name__ == '__main__':
    number_of_competitors = int(input())
    NewCompetitor = namedtuple('Competitor', ['score', 'penalty', 'name'])
    competitors = [
        prepare_competitor_data(
                input().split(), NewCompetitor
        ) for competitor in range(number_of_competitors)
    ]
    quicksort_effective(competitors, 0, number_of_competitors - 1)

    for competitor in competitors:
        print(competitor.name)

    # print(*(list(zip(*competitors)))[2], sep='\n')
