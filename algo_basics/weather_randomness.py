def weather_randomness(n, weather_array):
    
    if n == 1:
        return 1 

    randomness = 0
    if weather_array[0] > weather_array[1]:
        randomness += 1
    if weather_array[n-2] < weather_array[n-1]:
        randomness += 1

    for i in range(1, n - 1):
        randomness_condition = (
            weather_array[i-1] < weather_array[i] and
            weather_array[i+1] < weather_array[i]
        )
        if randomness_condition:
            randomness += 1

    return str(randomness)


def main():
    n = int(input())
    weather_array = [int(elem) for elem in input().split()]

    print(weather_randomness(n, weather_array))


if __name__ == '__main__':
    main()



