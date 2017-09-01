#!/usr/bin/env python
import os
import aplpy
import numpy
import matplotlib as mpl
mpl.use('Agg')
 
#mpl.use()
#mpl.use('Agg')
import matplotlib.pyplot as pyplot
#import montage_wrapper as montage
#tables and votables
from astropy.io.votable import parse_single_table
 
######### Set variables etc ##################
 
#datadir="/home/tash/Downloads/"
# Chenoa's computer:
datadir="./"
 
#############Change the Header file###############
import astropy
from astropy.io import fits
data, header = fits.getdata(datadir+"SgrA_I_Cont.fits", header=True)
delRA = -0.008 # degrees
delDec = -0.008 # degrees
header['BPA']=0.0
header['CRVAL1']+=delRA     #Correction for the RA based on astrometry calibration
header['CRVAL2']+=delDec     #Correction for the Dec based on astrometry calibration
fits.writeto(datadir+"SgrA_I_Cont_shift.fits", data, header, clobber=True)
 
 
######################################################
#field-of-view (length along x and y axes in degrees)
# Chenoa please update with your preferred levels
#fov_full=30
fov_zoom=10
# zoom center Chenoa please set
RA=269.8042
Dec=-29.8811
 
# greyscale levels Chenoa please set
vmin=-0.16
vmax=4.23
 
# Not used at the moment
#mwa_bmaj=0.0533054098487 # degrees
#mwa_bmin=0.0533054098487 # degrees
#mwa_bpa=0.0
 
bigfig=pyplot.figure(figsize=(11,5))
 
# Subplot is (left, bottom, width height)
fig=aplpy.FITSFigure(datadir+'SgrA_I_Cont_shift.fits',figure=bigfig,subplot=[0.1,0.1,0.33,0.72])
fig.show_colorscale(cmap="cubehelix_r",vmin=vmin,vmax=vmax)
 
 
fig.tick_labels.set_xformat("hh")
fig.tick_labels.set_yformat("dd")
 
#fig.tick_labels.set_font(size='35')
#fig.axis_labels.set_font(size='35')
fig.show_rectangles(RA,Dec,width=fov_zoom,height=fov_zoom,zorder=96,edgecolor='black')
#fig.show_markers(posloc[0], posloc[1], edgecolor='red', linewidth=2, marker='+', s=700)
#fig.set_tick_color('black')
 
# Subplot is (left, bottom, width height)
fig2=aplpy.FITSFigure(datadir+'SgrA_I_Cont_shift.fits',figure=bigfig,subplot=[0.5,0.1,0.33,0.72])
fig2.show_colorscale(cmap="cubehelix_r",vmin=vmin,vmax=vmax)
fig2.recenter(RA,Dec,width=fov_zoom,height=fov_zoom)
fig2.tick_labels.set_xformat("hh")
fig2.tick_labels.set_yformat("dd")
#fig2.show_markers(posloc[0], posloc[1], edgecolor='red', linewidth=2, marker='+', s=3000)
#fig.tick_labels.set_font(size='35')
#fig.axis_labels.set_font(size='35')
#fig2.set_tick_color('white')
 
fig2.add_beam()
fig2.beam.show(zorder=100)
fig2.beam.set_corner('bottom right')  # Chenoa, my preference is for bottom left, but I kept this consistent
fig2.beam.set_frame(True)
fig2.beam.set_hatch('/')
fig2.beam.set_color('black')
fig2.beam.set_edgecolor('black')
fig2.beam.set_facecolor('black')
# Add_axes is (left, bottom, width, height)
axisfig = bigfig.add_axes([0.85,0.1,0.03,0.72])
normf = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
cbfig = mpl.colorbar.ColorbarBase(axisfig, cmap="cubehelix",orientation="vertical",norm=normf)
cbfig.set_label('Flux density (Jy/beam)')
 
bigfig.savefig('Continuum.png',pad_inches=0.25,bbox_inches='tight')
