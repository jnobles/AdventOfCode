def decode(seq: str) -> int:
    display_map = {}
    correct_mappings = {'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5,
                        'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9, 'abcefg':0}
    seq = seq.split(' ')
    digits = [x for x in seq]
    print(digits)
    for place, display in enumerate(seq):
        if len(display) == 2:
            display_map[''.join(sorted(display))] = 'cf'
            digits[place] = 1
        elif len(display) == 4:
            display_map[''.join(sorted(display))] = 'bcdf'
            digits[place] = 4
        elif len(display) == 3:
            display_map[''.join(sorted(display))] = 'acf'
            digits[place] = 7
        elif len(display) == 7:
            display_map[''.join(sorted(display))] = 'abcdefg'
            digits[place] = 8
        print(digits)

#    while not all([type(x) ==  int for x in digits]):
#        if 4 in digits:
#            for place, display in enumerate(seq):
#                if len(display) == 6:
#                    if sum([wire in seq[digits.index(4)] for wire in display]) == 4:
#                        digits[place] = 9
#                print(digits)
#
#        if 4 in digits:
#            for place, display in enumerate(seq):
#                if len(display) == 5:
#                    if sum([wire in seq[digits.index(4)] for wire in display]) == 3:
#                        digits[place] = 3
#                print(digits)
#
#        if 1 in digits and 8 in digits:
#            for place, display in enumerate(seq):
#                if len(display) == 6:
#                    if sum([wire in seq[digits.index(1)] for wire in display]) == 2:
#                        digits[place] = 0
#                    else:
#                        digits[place] = 6
#                print(digits)

decode('fdgacbe cefdb cefbgd gcbe')
decode('fcgedb cgb dgebacf gc')
decode('cg cg fdcagb cbg')
decode('efabcd cedba gadfec cb')
decode('gecf egdcabf bgf bfgea')
