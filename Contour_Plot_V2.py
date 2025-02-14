#!/bin/python

#  Contour_Spectra_Plot.py
#  
#
#  Created by Chenoa Tremblay on 25/08/2017.
#

import os
import argparse
import numpy as np
import astropy
from astropy.io import fits
import matplotlib
from matplotlib import pyplot
from astropy.coordinates import SkyCoord  # High-level coordinates
from astropy.coordinates import ICRS, Galactic, FK4, FK5  # Low-level frames
from astropy.coordinates import Angle, Latitude, Longitude  # Angles
import astropy.units as u
from astropy import wcs
import math
import aplpy
matplotlib.use('Agg')
from astropy.io.votable import parse_single_table
import sys

mycube=sys.argv[1]
#ra=sys.argv[2]
#dec=sys.argv[3]
#slice=sys.argv[4]
cat_files=sys.argv[2]



######### Set variables etc ##################

# Chenoa's computer:
datadir="./"

#import astropy
#from astropy.io import fits
#data, header = fits.getdata(datadir+"SgrA_I_786_Subtracted.fits", header=True)


#Invert the cube for absorption
#Inversion=-1
#data*=Inversion

#fits.writeto(datadir+"Orion_I_143_Subtracted_Inverted.fits", data, header, clobber=True)
#mycube=str(Orion_I_143_Subtracted_Inverted.fits)
######################################################


#field-of-view (length along x and y axes in degrees)
fov_mwa=0.5
fov_wise=0.07
s_plot=7980

datacube = fits.open(mycube)
data = datacube[0].data
header = datacube[0].header

#Choose the header components for frequency
rp = datacube[0].header['CRPIX3']
rf = datacube[0].header['CRVAL3']
df = datacube[0].header['CDELT3']
nf = datacube[0].header['NAXIS3']
frequency=rf + df*(np.arange(nf)-rp)
#Input for all the coordinates to create a plot for
file=open(cat_files)
for line in file:
    ra,dec = line.strip().split(",")
    ra=str(ra)
    dec=str(dec)
#c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))

#Convert the coordinates
    w = wcs.WCS(header, naxis=2)


    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
    RA=c.ra.deg
    Dec=c.dec.deg
    Gal=c.galactic.l.degree
    Galb=c.galactic.b.degree
    #Convert to pixel values.
    xpix,ypix=c.to_pixel(w,origin=0,mode='wcs')
    xpix=int(xpix)
    ypix=int(ypix)

    signal=[]
    for x in range(0, 100):
        value = np.mean(data[:,x,ypix:ypix+1,xpix:xpix+1])
        #print rms_number_x
        signal.append(value)

    signal=np.multiply(signal,1.13)

    max_signal=np.nan_to_num(signal)
    max_value=np.max(max_signal)
    sli=np.argmax(max_signal, axis=0)
#Determine the contour levels by using a nearby pixel coordinates.
    rms_number = np.nanstd(data[:,slice,ypix+5:ypix+15,xpix+5:xpix+15])
    sig1=rms_number*3
    sig2=rms_number*4
    sig3=rms_number*5
    sig4=rms_number*6

#print i
#np.argmax(i)

    # MWA co-ordinates of detection
    posloc=np.array([85.7042,-1.8069])

    sli=int(sli)
    bigfig=pyplot.figure(figsize=(11,5))

    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[sli,0],subplot=(1,2,1))
    fig.recenter(RA,Dec,width=fov_mwa,height=fov_mwa)
#fig.show_contour(levels=(0.6,0.9,1.2,1.5,1.8), colors='black', linewidths=1)
    fig.show_contour(levels=(sig1,sig2,sig3,sig4), colors='black', linewidths=1)
    fig.add_beam()
    fig.beam.show(zorder=100)
    fig.beam.set_corner('bottom right')
    fig.beam.set_frame(True)
    fig.beam.set_hatch('/')
    fig.beam.set_color('black')
    fig.beam.set_edgecolor('black')
    fig.beam.set_facecolor('black')

    fig.tick_labels.set_xformat("hh:mm")
    fig.tick_labels.set_yformat("dd:mm")
    fig.set_title(("Gal: "+str(round(Gal,3))+" " + str(round(Galb,3))), fontsize='14')
    fig.show_markers(posloc[0], posloc[1], edgecolor='red', linewidth=2, marker='*', s=s_plot*(fov_wise/fov_mwa)**2)
    fig.set_tick_color('black')


#Subplot graph



    RMS2=str(round(rms_number,2))

    signal_ar=np.asarray(signal)
    snr=signal_ar/rms_number



    ax1=bigfig.add_subplot(122)
    ax1.step(frequency/10**6,signal,color='white',linewidth=2)
    ax1.set_xlabel("Frequency (MHz)", fontsize=12)
    ax1.set_ylabel("Flux (Jy)", fontsize=12 )
    ax1.text(frequency[60]/10**6, max_value, 'Local RMS='+str(RMS2), fontsize=14)
    ax1.tick_params(labelsize=12)
    #ax1.set_xlim([110.9,111.8])
    #ax1.annotate('SH', xy=(111.56, -1.5), xycoords='data', xytext=(111.65,-1.5), arrowprops=dict(facecolor='black', shrink=0.03))



    ax2 = ax1.twinx()
    ax2.step(frequency/10**6,snr,linewidth=2)
    ax2.set_ylabel("Signal to Noise Ratio", fontsize=12)
    ax2.tick_params(labelsize=12)
    #ax2.set_xlim([110.88,111.89])

    pyplot.tight_layout(pad=4, w_pad=4, h_pad=4)

    bigfig.savefig("Orion_"+str(ra)+"_"+str(dec)+"_"+str(frequency[0]/10**6)+".png",pad_inches=0.5,bbox_inches='tight')
