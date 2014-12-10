'''Useful tools for finding a filter apropos to a given wavelength'''

def make_dict_ACS(filter):
    outdict = {}
    usename = filter.replace('f','F').replace('w','W').replace('lp','LP')
    ff = open('wfc_'+usename+'.dat','r')
    while True:
        try:
            line = ff.readline()
            lammda = int(round(float(line.split()[0])))
            throughput = float(line.split()[1])
            outdict[lammda] = throughput
        except IndexError:
            break
    return outdict


def make_dict_WFC(filter):
    outdict = {}
    ff = open(filter+'.IR.tab','r')
    for ii in range(5):
        foo = ff.readline()
    while True:
        try:
            line = ff.readline()
            lammda = int(round(float(line.split()[1])))
            throughput = float(line.split()[2])
            outdict[lammda] = throughput
        except IndexError:
            break
    return outdict

