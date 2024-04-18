import time

from run import get_top_actors, write_top_actors_to_file


def perform_action():
    print('Now the program is going to parse the movies and actors data')
    time.sleep(1)
    print('Estimated wait time: 5 min')
    time.sleep(1)
    print('Once the action is done, the program will inform you!')
    get_top_actors()
    print('Action is done, thanks for patience!')
    user_input = input('Do you want to continue? (y/n): ')
    if user_input == 'y':
        filename = input('Please enter the name of the file to write the top 250 actors to: ')
        write_top_actors_to_file(filename)
    else:
        return
    user_input = input('Do you want to continue? (y/n): ')
    if user_input == 'y':
        with open(filename, 'r') as file:
            print(file.read())
    else:
        return
    return


def main():
    print('Welcome to the IMDB top 250 actors list!')
    time.sleep(1)
    print('The program itself has the following options:')
    time.sleep(1)
    print('"get top actors" is for getting the top 250 actors.')
    time.sleep(1)
    print('"write top actors to file" is for writing the top 250 actors to a file.')
    time.sleep(1)
    perform_action()
    print('Thank you!')
    time.sleep(1)
    print('Have a nice day! :3')


if __name__ == '__main__':
    main()
