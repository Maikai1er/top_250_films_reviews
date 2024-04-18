import time

from run import get_top_actors, write_top_actors_to_file
from run import sort_top_actors


def main():
    print('Welcome to the IMDB top 250 actors list!')
    time.sleep(1)
    print('The program itself has the following options:')
    time.sleep(1)
    print('"get top actors" is for getting the top 250 actors.')
    time.sleep(1)
    print('"write top actors to file" is for writing the top 250 actors to a file.')
    time.sleep(1)
    print('Estimated wait time: 5 min')
    time.sleep(1)
    print('Once the action is done, the program will inform you!')

    top_actors = get_top_actors()

    print('Getting data is done, thanks for patience!')
    time.sleep(1)
    print('The next step is to sort the data by films count and actors\' names.')
    time.sleep(1)

    sorted_top_actors = sort_top_actors(top_actors)

    time.sleep(1)
    print('The next step is to write our sorted data to file.')
    time.sleep(1)
    filename = input('Please enter the name of the file to write the top 250 actors to: ')
    time.sleep(1)
    print(f'Writing the top 250 actors to {filename}...')

    write_top_actors_to_file(filename, sorted_top_actors)

    time.sleep(1)
    print('Now you can see the top 250 actors list!')
    time.sleep(1)

    with open(filename, 'r') as file:
        print(file.read())

    time.sleep(1)
    print('Thank you!')
    time.sleep(1)
    print('Have a nice day! :3')


if __name__ == '__main__':
    main()
