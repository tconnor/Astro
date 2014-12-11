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

def get_through(filterdict,wavelength,red_steps=5,blue_steps=5,output='median'):
    '''Return the throughput at a given wavelength, with a spread in Angstroms allowed
    Inputs: red_steps,blue_steps -- how many Angstroms red/blue of wavelength to include (default:5)
            output: how to return throughput: Choices are 'median' (default),'sum', and 'average'. '''
    through_list = []
    for ll in range(wavelength-blue_steps,wavelength+red_steps+1):
        try:
            through_list.append(filterdict[ll])
        except KeyError:
            through_list.append(0)
    output = output.lower() #Handle User Error
    if output == 'median':
        return np.median(through_list)
    elif output == 'sum':
        return sum(through_list)
    elif output == 'average':
        return np.mean(through_list)
    else:
        return np.median(through_list)
    
