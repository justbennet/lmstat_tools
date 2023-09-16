import re

def get_matlab(matlab):

    # -: one or more whitespace '\s+'
    # 1: username '(.+)'
    # -: space
    # 2: hostname where process is running '(.+)'
    # -: space
    # 3: device '(.+)'
    # -: space
    # 4: version '\(v(.+)\)'
    # -: space
    # 5 and 6: license server hostname and port number '\((.+)/(.+)\)'
    # -: space
    # 7: day of week 'start (.+)'
    # -: space
    # 8 and 9: month and year '(\d+)/(\d+)'
    # -: space
    # 10 and 11: hour and minute '(\d*):(\d*)'

    # example named match string: ?P<first_name>
    # re.match(r'\s+(.+) (.+) (.+) \(v(.+)\) \((.+)/(.+) (.+)\), start (.+) (\d+)/(\d+) (\d*):(\d*)', matlab)

    # NOTE:  Not commas separating the r'()' parts; would be seen as
    # multiple arguments which is an error
    the_match = re.match(r'\s+(?P<username>.+) (?P<host>.+) (?P<device>.+)'
             r' \(v(?P<lmver>.+)\) \((?P<lmserver>.+)/(?P<lmport>.+)'
             r'(.+)\), start (?P<start_dayname>.+) '
             r'(?P<start_mo>\d+)/(?P<start_day>\d+) '
             r'(?P<start_hr>\d*):(?P<start_min>\d*)', matlab)
    return the_match

def get_abaqus(abaqus):
    # re.match(r'\s+(.+) (.+) (.+) \(v(.+)\) \((.+)/(.+) (.+)\), start (.+) (\d+)/(\d+) (\d*):(\d*), (\d+) licenses', abaqus)
    the_match = re.match(r'\s+(?P<user>.+) (?P<host>.+) (?P<device>.+)'
             r' \(v(?P<lmver>.+)\) \((?P<lmserver>.+)/(?P<lmport>.+)'
             r'(.+)\), start (?P<start_dayname>.+) '
             r'(?P<start_mo>\d+)/(?P<start_day>\d+) '
             r'(?P<start_hr>\d*):(?P<start_min>\d*), '
             r'(?P<tokens>\d+) licenses', abaqus)
    return the_match

if __name__ == '__main__':
    print('Running example')

    #### Examples of reading lmstat output using re
    ####   matlab output format is stable
    ####   sample abaqus output to see if the format changes

    # Matlab lmstat output
    matlab = '    grundoon node3447.your.computer.ex /dev/tty (v46) (flux-license1.miserver.it.umich.edu/1709 317905), start Sat 9/16 3:15'

    print('\nChecking sample matlab output')
    m = get_matlab(matlab)
    print(m.groupdict())


    # Abaqus lmstat output
    abaqus = '    grundoon node3152.your.computer.ex /dev/tty (v62.5) (flux-license1.miserver.it.umich.edu/27000 3680), start Tue 9/12 4:52, 36 licenses'

    print('\nChecking sample abaqus output')
    m = get_abaqus(abaqus)
    print(m.groupdict())
