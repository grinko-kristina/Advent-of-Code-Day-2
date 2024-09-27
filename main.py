def sum_of_possible_game_ids(games, max_cubes):
    sum_ids = 0
    for game in games:
        try:
            game_id, sequences = game.split(": ")
            if is_game_possible(sequences, max_cubes):
                sum_ids += int(game_id.split()[1])
        except ValueError as e:
            print(f"Error processing game data: {e}")
    return sum_ids


def is_game_possible(game_sequence, max_cubes):
    sequences = game_sequence.split(";")
    for sequence in sequences:
        if not is_sequence_possible(sequence.strip(), max_cubes):
            return False
    return True


def is_sequence_possible(sequence, max_cubes):
    cubes = sequence.split(",")
    for cube in cubes:
        count, color = cube.strip().split()
        if int(count) > max_cubes[color]:
            return False
    return True


def main():
    # Read games from the input file
    with open("input.txt") as f:
        games = f.readlines()

    # Define the maximum number of cubes allowed per color
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    # Calculate and display the sum of possible game IDs
    print(sum_of_possible_game_ids(games, max_cubes))


def test():
    games = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    sum_of_ids = sum_of_possible_game_ids(games, max_cubes)

    assert sum_of_ids == 8, f"Test failed: Expected 8, got {sum_of_ids}"
    print(f"Test passed: Sum of IDs is {sum_of_ids}")


if __name__ == "__main__":
    # Run the test function
    test()

    # Execute the main function
    main()
