import numpy as np
from matplotlib import pyplot as pt

c_light = 2.99792458E10
plank_h = 6.6260755E-27
plank_hbar = 1.05457266E-27

def great_circle(dec1,dec2,ra1,ra2,decradians=True,raradians=True,out='arcsec',haversine=False):
    '''Computes great circle angle between two coordinates in RA and Dec
    Inputs:
    dec1,ra1 -- position of object 1 (float)
    dec2,ra2 -- position of object2 (float)
    decradians -- are declinations in radians (default=True)
    raradians -- are right ascenscions in radians (default=True)
    out -- Outout format. Options: 'arcsec' (default), 'arcmin', 'degree'
    haversine -- Use haversine approximation (computationally more accurate for small angles) (default=False)'''
    if not decradians:
        dec1 = np.radians(dec1)
        dec2 = np.radians(dec2)
    if not raradians:
        ra1 = np.radians(15.*ra1)
        ra2 = np.radians(15.*ra2)
    del_ra = ra1 - ra2
    if haversine:
        del_dec = dec1 - dec2
        term1 = np.sin(del_dec/2.)**2.
        term2 = np.cos(dec1) * np.cos(dec2)
        term3 = np.sin(del_ra/2.)**2.
        sigma_angle =  2.* np.arcsin(np.sqrt(term1 + term2*term3))
    else:
        term1 = np.sin(dec1) * np.sin(dec2)
        term2 = np.cos(dec1) * np.cos(dec2)
        term3 = np.cos(del_ra)
        sigma_angle = np.arccos(term1 + term2*term3)
    sigma_angle = np.degrees(sigma_angle)
    if out=='degree':
        return sigma_angle
    elif out=='arcmin':
        return sigma_angle * 60.
    elif out=='arcsec':
        return sigma_angle * 3600.
    else:
        print 'Invalid Output format for Great Circle Distance; returning arcseconds'
        return sigma_angle * 3600.
    
def rahmstohdd(hour,minute,second):
    '''Converts a Right Ascension coordinate from HH:MM:SS to HH.DDDDDD (float)
    Inputs:
    hour: RA Hour
    minute: RA Minute
    second: RA Second'''
    out = float(hour) + float(minute)/60. + float(second)/3600.
    return out

def decdmstodec(degree,minute,second):
    '''Converts a Declination coordinate from DD:MM:SS to DD.DDDDDD (float)
    Inputs:
    hour: DEC Hour
    minute: DEC Minute
    second: DEC Second'''
    out = float(hour) + float(minute)/60. + float(second)/3600.
    return out

def rahmstodec(hour,minute,second):
    '''Converts a Right Ascension coordinate from HH:MM:SS to DD.DDDDDD (float)
    This is a decimal angle, not an hour angle.
    Inputs:
    hour: RA Hour
    minute: RA Minute
    second: RA Second'''
    out = (float(hour) + float(minute)/60. + float(second)/3600.)*15.
    return out

def decdectodms(declination):
    '''Converts a declination in decimal degrees to Degrees, Minutes, Seconds'''
    deg = int(declination) #This converts +3.XX to 3 and -3.XX to -3
    rmndr = abs(declination - deg)*60.
    mint = int(rmndr)
    sec = (rmndr - mint)*60.
    return deg,mint,sec

def radectohms(righta):
    '''Converts a right ascension in decimal degrees to Hours, Minutes, Seconds'''
    hrrta = righta / 15.
    hour = int(hrrta)
    rmndr = (hrrta - hour)*60.
    minute = int(rmndr)
    sec = (rmndr - minute)*60.
    return hour,minute,sec


def redshift(lamda,redshift):
    '''Redshifts a wavelength'''
    return lamda * (1. + redshift)

def restframe(lamda,redshift):
    '''Converts a redshifted wavelength to restframe'''
    return lamda / (1. + redshift)

