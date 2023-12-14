def process_input_line(input_line:str)->tuple:
    game_dict = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    input_line = input_line.rstrip("\n")
    input_array = input_line.split(":")
    
    game_index = int(input_array[0].split(" ")[1])

    game_results = input_array[1].strip().split(";")

    # extract the maximum value for each color from each game
    for game in game_results:
        game_array = game.strip().split(", ")
        for result in game_array:
            color_result = result.split(" ")
            game_dict[color_result[1]] = max(int(color_result[0]), game_dict[color_result[1]])

    return(game_index, game_dict)

def possible_game(game_index: int, game_dict)->int:
    red = 12
    green = 13
    blue = 14

    if game_dict["red"]<= red and game_dict["blue"]<= blue and game_dict["green"]<= green:
        return game_index
    return 0

def sum_possible_games(games:list)->int:
    final = 0
    for game in games:
        index, game_dict = process_input_line(game)
        power = game_dict["red"]*game_dict["blue"]*game_dict["green"]
        final += power
    return final


if __name__ == "__main__":
    file_path = '/home/sami/dev/osu_portfolio/algorithmStudy/adventOfCode/day2/day2.txt'
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
    print(sum_possible_games(lines))