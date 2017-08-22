'''oRide Python application

This module prompts the user for menu options and
execute the menu features accordingly.
'''
from multiprocessing import Process
from datetime import datetime
from sense_hat import SenseHat
import time

bicycles_data = []
time_format = '%d/%m/%Y'
OPTIONS = {
    'admin': [
        {
            'desc': 'Read bicycle info from file',
            'action': lambda: menu_read_info(bicycles_data)
        },
        {
            'desc': 'Display all bicycle info with servicing indication',
            'action': lambda: menu_display_info(bicycles_data)
        },
        {
            'desc': 'Display selected bicycle info',
            'action': lambda: menu_display_select_info()
        },
        {
            'desc': 'Add a bicycle',
            'action': lambda: menu_add_bicycle(bicycles_data)
        },
        {
            'desc': 'Perform bicycle maintenance',
            'action': lambda: menu_service_bicycle(bicycles_data)
        }
    ],
    'rider': [
        {
            'desc': 'Ride a bicycle',
            'action': lambda: menu_ride_bicycle(bicycles_data)
        }
    ],
    'etc': [
        {
            'desc': 'Exit',
            'action': lambda: quit()
        }
    ]
}

FIRST_COLUMNS = [
    ['Bike No.', 'number'],
    ['Purchase Date', 'purchase_date'],
    ['Batt %', 'battery'],
    ['Last Maintenance', 'last_maintenance'],
    ['KM since Last', 'km_since_last'],
    ['Service?', 'service']
]

SECOND_COLUMNS = [
    FIRST_COLUMNS[0],
    ['Ride duration', 'duration'],
    ['Ride distance', 'distance'],
    FIRST_COLUMNS[2]
]


def request_menu():
    '''
    Requests the menu indefinitely.
    '''
    while True:
        try:
            request_action(OPTIONS)() # Additional parentheses to execute lambda
        except (ValueError, IndexError):
            print('Invalid menu option.')
        except KeyboardInterrupt:
            # For when program is interrupted via keyboard (Ctrl-C)
            quit()
        except:
            raise
        print()


def request_action(options):
    '''
    Sends a menu to the user and awaits input.
    When input is received, returns the action (lambda) for the based on the input.
    '''
    # Generates appropriate starting option numbers for each category
    start_admin = len(OPTIONS['etc'])
    cur_admin = start_admin
    start_rider = start_admin + len(OPTIONS['admin'])
    cur_rider = start_rider
    cur_etc = 0

    print('Admin Menu')
    print('==========')
    for option in options['admin']:
        print('[%s] %s' % (cur_admin, option["desc"]))
        cur_admin += 1
    print()

    print('Rider Menu')
    print('==========')
    for option in options['rider']:
        print('[%s] %s' % (cur_rider, option["desc"]))
        cur_rider += 1
    print()

    for option in options['etc']:
        print('[%s] %s' % (cur_etc, option["desc"]))
        cur_etc += 1
    print()

    option = int(input('Enter your option: '))
    option_type = 'etc' if option < start_admin else 'admin' if option < start_rider else 'rider'
    selection = option - (start_admin if option_type ==
                          'admin' else start_rider if option_type == 'rider' else 0)
    dictionary = options[option_type][selection]

    print()
    print('Option %s: %s' % (option, dictionary["desc"]))
    print()
    return dictionary['action']


def menu_read_info(bicycles):
    '''
    Reads bicycle data from specified .csv file.
    Also, displays the amount of bicycle data loaded.
    '''
    file_name = input('Enter the name of the data file: ')
    file_obj = open(file_name, 'r')
    c_loaded = []

    for i, line in enumerate(file_obj):
        if i != 0:
            splitted = line.rstrip().split(',')
            c_loaded.append({
                FIRST_COLUMNS[0][1]: splitted[0],
                FIRST_COLUMNS[1][1]: splitted[1],
                FIRST_COLUMNS[2][1]: int(splitted[2]),
                FIRST_COLUMNS[3][1]: splitted[3],
                FIRST_COLUMNS[4][1]: float(splitted[4])
            })
    bicycles.extend(c_loaded)
    print('Number of bicycle records read: %s' % (len(c_loaded)))


def menu_display_info(bicycles):
    '''
    Displays all bicycle data in cache with a pretty table.
    '''
    contents = []

    for bicycle in bicycles:
        contents.append({
            FIRST_COLUMNS[0][1]: bicycle[FIRST_COLUMNS[0][1]],
            FIRST_COLUMNS[1][1]: bicycle[FIRST_COLUMNS[1][1]],
            FIRST_COLUMNS[2][1]: bicycle[FIRST_COLUMNS[2][1]],
            FIRST_COLUMNS[3][1]: bicycle[FIRST_COLUMNS[3][1]],
            FIRST_COLUMNS[4][1]: bicycle[FIRST_COLUMNS[4][1]],
            FIRST_COLUMNS[5][1]: ['N', 'Y'][len(get_service_reasons(bicycle)) > 0]})
    print_table(FIRST_COLUMNS, contents)


def menu_display_select_info():
    '''
    Reads and displays specified bicycle ride history.
    '''
    file_name = 'Assignment_Data2.csv'
    file_obj = open(file_name, 'r')
    number = input('Enter a bike no.: ')
    bicycles = []

    for i, line in enumerate(file_obj):
        if i != 0:
            splitted = line.rstrip().split(',')
            if len(splitted) == len(SECOND_COLUMNS):
                bicycles.append({
                    SECOND_COLUMNS[0][1]: splitted[0],
                    SECOND_COLUMNS[1][1]: int(splitted[1]),
                    SECOND_COLUMNS[2][1]: float(splitted[2]),
                    SECOND_COLUMNS[3][1]: float(splitted[3])
                })
    filtered = [bicycle for bicycle in bicycles if bicycle['number'] == number]
    print_table(SECOND_COLUMNS, filtered)


def menu_add_bicycle(bicycles):
    '''
    Adds new bicycle to cache based on input.
    '''
    number = input('Bike No.: ')
    purchase_date = datetime.strptime(input('Purchase Date: '), time_format)
    bicycle = {
        FIRST_COLUMNS[0][1]: number,
        FIRST_COLUMNS[1][1]: datetime.strftime(purchase_date, time_format),
        FIRST_COLUMNS[2][1]: 100,
        FIRST_COLUMNS[3][1]: datetime.strftime(datetime.now(), time_format),
        FIRST_COLUMNS[4][1]: 0.0
    }

    bicycles.append(bicycle)
    print('Bicycle (%s) has been created.' % (bicycle["number"]))


def menu_service_bicycle(bicycles):
    '''
    Services servicable bicycles in cache.
    '''
    due = []
    columns = [FIRST_COLUMNS[0],
               FIRST_COLUMNS[2],
               FIRST_COLUMNS[3],
               FIRST_COLUMNS[4],
               ['Reason/s', 'reasons']]

    for bicycle in bicycles:
        reasons = get_service_reasons(bicycle)
        if reasons:
            due.append({
                columns[0][1]: bicycle[columns[0][1]],
                columns[1][1]: bicycle[columns[1][1]],
                columns[2][1]: bicycle[columns[2][1]],
                columns[3][1]: bicycle[columns[3][1]],
                'reasons': ' & '.join(reasons)
            })
    print_table(columns, due)

    while due:
        number = input('Bike No.: ')
        is_due = number in [b[columns[0][1]] for b in due]
        is_existing = number in [b[columns[0][1]] for b in bicycles]

        if is_existing:
            if is_due:
                bicycle = [
                    b for b in bicycles if b[columns[0][1]] == number][0]
                bicycle[columns[1][1]] = 100
                bicycle[columns[2][1]] = datetime.strftime(
                    datetime.now(), time_format)
                bicycle[columns[3][1]] = 0.0
                print('Bicycle serviced.')

                bicycle = [
                    b for b in due if b[columns[0][1]] == number][0]
                due.remove(bicycle)
                print_table(columns, due)
                break
            else:
                print('Bicycle is not due for servicing.')
        else:
            print('No such bicycle.')


def menu_ride_bicycle(bicycles):
    '''
    Initiate riding on specified available bicycle.
    '''
    sense = SenseHat()
    ridable = [b for b in bicycles if not(get_service_reasons(b))]
    columns = [FIRST_COLUMNS[0],
               FIRST_COLUMNS[2],
               FIRST_COLUMNS[4]]

    print_table(columns, ridable)
    print()

    while ridable:
        number = input('Bike No.: ')
        is_existing = number in [b[columns[0][1]] for b in ridable]

        if is_existing:
            bike = [b for b in ridable if b[columns[0][1]] == number][0]
            # Empty space in column header due to insufficient spacing for data
            ride_columns = [['   Pitch', 'pitch'],
                            ['   Roll', 'roll'],
                            ['   Yaw', 'yaw'],
                            ['Movement', 'movement'],
                            ['   Temp', 'temp'],
                            columns[1],
                            ['KM', 'km']]
            ride_time = 15
            interval = 3
            temp_to_charge = 0.5

            G = [0, 255, 0] # Green Color Code
            R = [255, 0, 0] # Red Color Code
            E = [0, 0, 0] # Black Color Code

            t_secs = 0
            t_km = 0.0
            p_pitch, p_roll, p_yaw = 0, 0, 0

            print_table(ride_columns, [])
            for i in range(0, ride_time):
                time.sleep(1)
                t_secs += 1
                if i % interval == 0:
                    o = sense.get_orientation()
                    c_pitch, c_roll, c_yaw = o["pitch"], o["roll"], o["yaw"]
                    c_temp = sense.get_temperature()
                    c_movement = abs(c_pitch - p_pitch) + \
                        abs(c_roll - p_roll) + \
                        abs(c_yaw - p_yaw) >= 20

                    if c_movement and c_temp > temp_to_charge:
                        bike[columns[1][1]] += 1
                        bike[columns[2][1]] += 0.1
                        t_km += 0.1
                        t_km = round(t_km, 2)
                    else:
                        bike[columns[1][1]] -= 1
                    # Ensures battery is within bounds (0 and 100)
                    # And also rounds KM to 2 decimal places
                    bike[columns[1][1]] = max(0, min(100, bike[columns[1][1]]))
                    bike[columns[2][1]] = round(bike[columns[2][1]], 2)

                    # Display battery
                    sense.clear()
                    for ii in range(0, 50):
                        c_batt = (ii + 1) * 2
                        color = G if c_batt <= bike[columns[1][1]] \
                            else R if c_batt - 1 <= bike[columns[1][1]] \
                            else E
                        x_pos = ii % 8
                        y_pos = int(ii / 8)
                        sense.set_pixel(x_pos, y_pos, color)

                    # Print row for current iteration
                    print_table(ride_columns, [{
                        ride_columns[0][1]: round(c_pitch, 2),
                        ride_columns[1][1]: round(c_roll, 2),
                        ride_columns[2][1]: round(c_yaw, 2),
                        ride_columns[3][1]: c_movement,
                        ride_columns[4][1]: round(c_temp, 2),
                        ride_columns[5][1]: bike[columns[1][1]],
                        ride_columns[6][1]: t_km
                    }], show_header=False)

                    p_pitch, p_roll, p_yaw = c_pitch, c_roll, c_yaw
            print('Trip ended.')
            print()
            print('You travelled %s over %s seconds.' % (t_km, t_secs))
            print('Thank you for riding with oRide!')

            sense.clear()

            file_name = 'Assignment_Data2.csv'
            file_obj = open(file_name, 'a')

            file_obj.write(','.join([str(bike[columns[0][1]]),
                                     str(t_secs),
                                     str(t_km),
                                     str(bike[columns[1][1]])]))
            break
        else:
            print('No such bicycle.')


def get_service_reasons(bicycle):
    '''
    Gets all reasons for servicing for a bicycle.
    Returns a list of reasons.
    '''
    current_date = datetime.now()
    bicycle_date = datetime.strptime(bicycle['last_maintenance'], time_format)
    reasons = []

    if bicycle['battery'] < 10:
        reasons.append('Batt')
    if (current_date - bicycle_date).days > 6 * 30:
        reasons.append('Months')
    if bicycle['km_since_last'] > 50:
        reasons.append('KM')
    return reasons


def print_table(columns, contents, show_header=True):
    '''
    Prints a pretty table with the columns and contents
    '''
    aligns = [len(column[0]) for column in columns]
    headers = [[column[0] for column in columns],
               [align * '-' for align in aligns]]
    if show_header:
        for header in headers:
            print(' '.join(header))
    for content in contents:
        for i, column in enumerate(columns):
            data = str(content[column[1]])
            print((aligns[i] - len(data)) * ' ' + data, end=' ')
        print()


def main():
    '''The main method'''
    Process(target=request_menu()).start()


if __name__ == "__main__":
    main()
