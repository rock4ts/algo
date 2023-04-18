
def merge_gargen_beds(beds: list):
    beds = sorted(beds, key=lambda bed: bed[0])
    current_bed = beds[0]
    for i in range(1, len(beds)):
        next_bed = beds[i]
        beds_are_intersected = next_bed[0] <= current_bed[1]
        next_within_current = next_bed[1] <= current_bed[1]
        if beds_are_intersected and next_within_current:
            next
        elif beds_are_intersected:
            current_bed[1] = next_bed[1]
        else:
            print(*current_bed)
            current_bed = next_bed
    print(*current_bed)


if __name__ == '__main__':
    number_of_beds = int(input())
    garden_beds = []
    for _ in range(number_of_beds):
        garden_beds.append(list(map(int, input().split())))

    merge_gargen_beds(garden_beds)
