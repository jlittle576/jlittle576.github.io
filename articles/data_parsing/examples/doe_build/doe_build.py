import copy, sys
f_matrix = open('design_matrix.csv', 'r')

matrix = {}
datastart = False
design_variables = []
runs = []

for line in f_matrix:

    row = line.rstrip().replace(' ', '').split(',')

    # checkpoint:
    # print the row to verify it was split correctly

    # print row
    # sys.exit()

    if (not datastart) and 'run,' in line:
        design_variables = row[1:]
        for design_variable in design_variables:
            matrix[design_variable] = {}

        # checkpoint:
        # verify design_variables array contains the column titles in design_matrix.csv

        # print row
        # sys.exit()

        datastart = True

    elif datastart:

        run = int(row[0])
        runs.append(run)
        values = row[1:]
        for value, design_variable in zip(values, design_variables):
            matrix[design_variable][run] = value


# checkpoint:
# verify matrix dict structure and contents

# for design_variable in matrix:
#     print '%-15s' % design_variable,
#     for run in matrix[design_variable]:
#         print ' %3s: %-12s' % (run, matrix[design_variable][run]),
#     print ''
# sys.exit()



for run in runs:

    run = int(run)

    new_file_name = 'pendulum_run_%02d.adm' % run

    part = False
    f_baseline = open('pendulum.adm', 'r')
    f_iteration = open(new_file_name, 'w')

    # checkpoint
    # verify a series of numbered blank files are created in the directory

    # continue

    for line in f_baseline:

        line = line.rstrip()
        if 'PART/' in line:
            part = int(line.rstrip().split('/')[1])

            # checkpoint:
            # this should print out the each part for each run
            # tip: for debugging, change the 'for run in runs' line so the loop only runs once or twice

            # print 'run', run, 'part', part
            # continue

        if part and ('MASS =' in line):
            mass = line.split('=')[1]

            # checkpoint:
            # verify mass is the numerical portion iof the MASS = ... strings

            # print run, part, mass
            # continue

            check_str = 'part_%02d_mass' % part
            if check_str in design_variables:
                old_line = copy.copy(line)           # for debug print
                line = ', MASS = ' + matrix[check_str][run]

                # checkpoint:
                # verify the design_variable match and line reconstruction

                # print old_line, '         >>             ', line
                # continue


        # permuting the INERTIA attributes is similar, but a bit more involved,
        # since there are contains 3 values, some, none, or all which may need to be permuted

        if part and ('INERTIA =' in line):
            inertias = line.split('=')[1].split(',')
            new_inertias = copy.copy(inertias)

            for index, component in enumerate(['x', 'y', 'z']):

                # build a check string to see if its the design variable list
                check_str = 'part_%02d_i%s' % (part, component)
                if check_str in design_variables:

                    # get the appropriate index form the map and assign the value to new_inertias
                    new_inertias[index] = matrix[check_str][run]

                    # checkpoint:
                    # verify new inertia values are being transferred properly from design matrix

                    # print inertias, '>>', new_inertias
                    # f_iteration.close()
                    # f_baseline.close()
                    # continue

            line = ', INERTIA = ' + ','.join(new_inertias)

        f_iteration.write(line + '\n')

        if line[0] == '!':
            part = False

    f_iteration.close()
    f_baseline.close()

