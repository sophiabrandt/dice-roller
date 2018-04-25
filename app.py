from random import randint


def main():
    print_header()
    run_event_loop()


def print_header():
    print('--------------------------------')
    print('       D&D DICE ROLLER')
    print('--------------------------------')
    print()


def run_event_loop():
    cmd = 'EMPTY'

    while cmd != 'x':
        try:
            cmd = input(
                'Roll a d<20>, d<12>, d<10>, d<8>, d<6>, d<4> or e<x>it. ').lower().strip()

            if cmd != 'x':
                die_size = int(cmd)

                if die_size == 20 or die_size == 12 or die_size == 10 or die_size == 8 or die_size == 6 or die_size == 4:
                    roll = randint(1, die_size)
                    print(f'\nYou rolled a {roll}!\n')

                else:
                    print(
                        f'\nThere is no {die_size}-sized die. Please choose a die.\n')

        except ValueError:
            print("\nI don't understand! Choose a die or e<x>it!\n")

    print('...exiting...Goodbye!')


if __name__ == '__main__':
    main()
