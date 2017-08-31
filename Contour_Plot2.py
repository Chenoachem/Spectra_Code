Last login: Thu Aug 17 19:18:44 on ttys006
-bash: /usr/local/karma/.karmarc: No such file or directory
Chenoas-MacBook-Air:~ Chenoachem$ cd Documents/MWA\ Project\ Data/Orion_Testing/Orion_99/
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
Contour_Spectra_Plot.py
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Orion_05:37:19.83_111.0_.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
Slice_Test.py
Spectra_Plot.ipynb
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 26, in <module>
    mycube=sys.argv[1]
NameError: name 'sys' is not defined
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 67, in <module>
    bigfig=pyplot.figure(figsize=(11,5))
NameError: name 'pyplot' is not defined
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 70, in <module>
    fig.recenter(RA,Dec,width=fov_mwa,height=fov_mwa)
NameError: name 'Dec' is not defined
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 83, in <module>
    fig.set_title(str(round(RA,3))+" "+str(round(DEC,3)), fontsize='14')
NameError: name 'DEC' is not defined
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_05:37:19.83_111.0_.png
1132168688_self_solutions_phase.png	Orion_06:24:42.07_111.0_.png
Histogram10.png				Orion_RMS.png
Histogram12.png				RMS.png
Histogram_12.png			SH.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open SH.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_05:37:19.83_111.0_.png
1132168688_self_solutions_phase.png	Orion_06:24:42.07_111.0_.png
Histogram10.png				Orion_RMS.png
Histogram12.png				RMS.png
Histogram_12.png			SH.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open SH.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open SH.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Test_Plot.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Test_Plot.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Test_Plot.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
  File "Contour_Spectra_Plot.py", line 149
    bigfig.savefig(str(RA)+str(Dec)+str(int(xvals[0])).png',pad_inches=0.5,bbox_inches='tight')
                                                                                       ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
  File "Contour_Spectra_Plot.py", line 149
    bigfig.savefig(str(RA)+str(Dec)+str(int(xvals[0]))'.png',pad_inches=0.5,bbox_inches='tight')
                                                           ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
  File "Contour_Spectra_Plot.py", line 149
    bigfig.savefig(str(RA)+str(Dec)+str(int(xvals[0]))".png",pad_inches=0.5,bbox_inches='tight')
                                                           ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
  File "Contour_Spectra_Plot.py", line 149
    bigfig.savefig(str(RA)+str(Dec)+str(int(xvals[0]/10**6))".png",pad_inches=0.5,bbox_inches='tight')
                                                                 ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
  File "Contour_Spectra_Plot.py", line 149
    bigfig.savefig(str(RA)+str(Dec)+str(xvals[0]/10**6)".png",pad_inches=0.5,bbox_inches='tight')
                                                            ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
  File "Contour_Spectra_Plot.py", line 149
    bigfig.savefig(str(RA)+str(Dec)+str(frequency[0]/10**6)".png",pad_inches=0.5,bbox_inches='tight')
                                                                ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
71.84575-13.677477777899.3.png
Contour_Spectra_Plot.py
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Orion_05:37:19.83_111.0_.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
SH.png
Slice_Test.py
Spectra_Plot.ipynb
Test_Plot.png
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_05:37:19.83_111.0_.png
1132168688_self_solutions_phase.png	Orion_06:24:42.07_111.0_.png
71.84575-13.677477777899.3.png		Orion_RMS.png
Histogram10.png				RMS.png
Histogram12.png				SH.png
Histogram_12.png			Test_Plot.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_06:24:42.07_111.0_.png
1132168688_self_solutions_phase.png	Orion_71.84575_-13.6774777778_99.3.png
71.84575-13.677477777899.3.png		Orion_RMS.png
Histogram10.png				RMS.png
Histogram12.png				SH.png
Histogram_12.png			Test_Plot.png
Orion_05:37:19.83_111.0_.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:47:22.98 -13:40:38.92 36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
71.84575-13.677477777899.3.png
Contour_Spectra_Plot.py
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_71.84575_-13.6774777778_99.3.png
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
SH.png
Slice_Test.py
Spectra_Plot.ipynb
Test_Plot.png
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_05:37:19.83_111.0_.png
1132168688_self_solutions_phase.png	Orion_06:24:42.07_111.0_.png
71.84575-13.677477777899.3.png		Orion_71.84575_-13.6774777778_99.3.png
Histogram10.png				Orion_RMS.png
Histogram12.png				RMS.png
Histogram_12.png			SH.png
Orion_04:47:22.98_-13:40:38.92_99.3.png	Test_Plot.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04:47:22.98_-13:40:38.92_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:38.19 -10:36:15.79 42
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_05:37:19.83_111.0_.png
1132168688_self_solutions_phase.png	Orion_06:24:42.07_111.0_.png
71.84575-13.677477777899.3.png		Orion_71.84575_-13.6774777778_99.3.png
Histogram10.png				Orion_RMS.png
Histogram12.png				RMS.png
Histogram_12.png			SH.png
Orion_04:47:22.98_-13:40:38.92_99.3.png	Test_Plot.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04:52:38.19_-10:36:15.79_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:38.19 -10:36:15.79 43
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04:52:38.19_-10:36:15.79_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:38.19 -10:36:15.79 44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04:52:38.19_-10:36:15.79_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04:52:38.19_-10:36:15.79_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:38.19 -10:36:15.79 45
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04:52:38.19_-10:36:15.79_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:27:19.38 -11:43:16.01 26
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
71.84575-13.677477777899.3.png
Contour_Spectra_Plot.py
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_05:27:19.38_-11:43:16.01_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_71.84575_-13.6774777778_99.3.png
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
SH.png
Slice_Test.py
Spectra_Plot.ipynb
Test_Plot.png
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls *.png
1132168688_self_solutions_amp.png	Orion_05:27:19.38_-11:43:16.01_99.3.png
1132168688_self_solutions_phase.png	Orion_05:37:19.83_111.0_.png
71.84575-13.677477777899.3.png		Orion_06:24:42.07_111.0_.png
Histogram10.png				Orion_71.84575_-13.6774777778_99.3.png
Histogram12.png				Orion_RMS.png
Histogram_12.png			RMS.png
Orion_04:47:22.98_-13:40:38.92_99.3.png	SH.png
Orion_04:52:38.19_-10:36:15.79_99.3.png	Test_Plot.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open )rion_05:27:19.38_-11:43:16.01_99.3.png
-bash: syntax error near unexpected token `)'
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05:27:19.38_-11:43:16.01_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ vi Contour_Spectra_Plot.py 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:27:19.38 -11:43:16.01 26
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05:27:19.38_-11:43:16.01_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:50.04 -12:07:49.85
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 100, in <module>
    slic=int(i)
TypeError: int() argument must be a string or a number, not 'tuple'
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:50.04 -12:07:49.85 45
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:50.04 -12:07:49.85 45
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_0
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_04:52:50.04_-12:07:49.85_99.3.png
Orion_05:27:19.38_-11:43:16.01_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_06:24:42.07_111.0_.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_0
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_04:52:50.04_-12:07:49.85_99.3.png
Orion_05:27:19.38_-11:43:16.01_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_06:24:42.07_111.0_.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:52\:50.04_-12\:07\:49.85_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:50.04 -12:07:49.85 44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:52\:50.04_-12\:07\:49.85_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:50.04 -12:07:49.85 46
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:52\:50.04_-12\:07\:49.85_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:52:50.04 -12:07:49.85 45
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:52\:50.04_-12\:07\:49.85_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:54:57.15 +02:36:45.54 33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_04:52:50.04_-12:07:49.85_99.3.png
Orion_04:54:57.15_+02:36:45.54_99.3.png
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:54\:57.15_+02\:36\:45.54_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:54:57.15 +02:36:45.54 33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:54\:57.15_+02\:36\:45.54_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:56:06.03-02:29:17.93 54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 30, in <module>
    slice=sys.argv[4]
IndexError: list index out of range
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 04:56:06.03 -02:29:17.93 54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_04\:56\:06.03_-02\:29\:17.93_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:01:07.48 -10:37:26.97 28
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:01:07.48 -10:37:26.97 28
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
open Orion_05/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:01\:07.48_-10\:37\:26.97_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:02:25.60 -07:49:54.28 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:02\:25.60_-07\:49\:54.28_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:02:25.60 -07:49:54.28 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:02\:25.60_-07\:49\:54.28_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:10:38.21 -00:24:15.16 43
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:10:38.21 -00:24:15.16 43
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:10\:38.21_-00\:24\:15.16_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:11:18.00 -06:26:14.96 33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:11:18.00 -06:26:14.96 33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:11\:18.00_-06\:26\:14.96_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:11:30.49 +04:22:38.24 33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
<type 'int'>
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:11:30.49 +04:22:38.24 33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 106, in <module>
    fig.show_contour(levels=(0.9,1.2,1.5,1.8), colors='black', linewidths=1)
  File "<string>", line 2, in show_contour
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 946, in show_contour
    c = self._ax1.contour(image_contour, levels, extent=extent_contour, cmap=cmap, colors=colors, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py", line 1812, in inner
    return func(ax, *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 5644, in contour
    return mcontour.QuadContourSet(self, *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/contour.py", line 1424, in __init__
    ContourSet.__init__(self, ax, *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/contour.py", line 960, in __init__
    zorder=zorder)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/collections.py", line 1149, in __init__
    self.set_segments(segments)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/collections.py", line 1164, in set_segments
    self._paths = [mpath.Path(_seg) for _seg in _segments]
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/path.py", line 162, in __init__
    self._update_values()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/path.py", line 215, in _update_values
    (len(self._vertices) >= 128 and
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:11:30.49 +04:22:38.24 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:11\:30.49_+04\:22\:38.24_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:12:24.36 +05:10:15.01 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([34]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 105, in <module>
    fig.recenter(RA,Dec,width=fov_mwa,height=fov_mwa)
  File "<string>", line 2, in recenter
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 530, in recenter
    self._ax1.set_ylim(ypix - dy_pix, ypix + dy_pix)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axes/_base.py", line 3048, in set_ylim
    bottom, top = self.yaxis.limit_range_for_scale(bottom, top)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 700, in limit_range_for_scale
    return self._scale.limit_range_for_scale(vmin, vmax, self.get_minpos())
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 2267, in get_minpos
    return self.axes.dataLim.minposy
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py", line 230, in axes
    return self._axes
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:12:24.36 +05:10:15.01 34
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([34]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:13:39.80 -09:12:48.90 34
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([42]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:13\:39.80_-09\:12\:48.90_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:13:39.80 -09:12:48.90 42
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([42]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:13\:39.80_-09\:12\:48.90_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:13:39.80 -09:12:48.90 42
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([42]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:14:01.09 -15:46:42.94 42
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([54]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 285, in __init__
    self._ax2 = self._ax1.twin()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/mpl_toolkits/axes_grid1/parasite_axes.py", line 395, in twin
    viewlim_mode="equal",
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/mpl_toolkits/axes_grid1/parasite_axes.py", line 91, in __init__
    self._parasite_axes_class.__init__(self, parent_axes, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/mpl_toolkits/axes_grid1/parasite_axes.py", line 39, in __init__
    parent_axes._position, **kargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/mpl_toolkits/axisartist/axislines.py", line 624, in __init__
    super(Axes, self).__init__(*kl, **kw)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axes/_base.py", line 508, in __init__
    self._init_axis()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/mpl_toolkits/axisartist/axislines.py", line 647, in _init_axis
    super(Axes, self)._init_axis()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axes/_base.py", line 566, in _init_axis
    self.xaxis = maxis.XAxis(self)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 658, in __init__
    self.cla()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 742, in cla
    self.reset_ticks()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 756, in reset_ticks
    self.majorTicks.extend([self._get_tick(major=True)])
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 1675, in _get_tick
    return XTick(self.axes, 0, '', major=major, **tick_kw)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 151, in __init__
    self.tick2line = self._get_tick2line()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axis.py", line 414, in _get_tick2line
    zorder=self._zorder)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/lines.py", line 339, in __init__
    self.set_marker(marker)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/lines.py", line 1071, in set_marker
    self._marker.set_marker(marker)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/markers.py", line 255, in set_marker
    self._recache()
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/markers.py", line 193, in _recache
    self._marker_function()
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:14:01.09 -15:46:42.94 54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([54]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:14\:01.09_-15\:46\:42.94_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:14:07.95 -14:09:24.16 34
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([90]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:14:07.95 -14:09:24.16 90
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([90]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:14\:07.95_-14\:09\:24.16_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:16:37.26 -13:23:10.29 34
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([14]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 106, in <module>
    fig.show_contour(levels=(0.6,0.9,1.2,1.5,1.8), colors='black', linewidths=1)
  File "<string>", line 2, in show_contour
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 946, in show_contour
    c = self._ax1.contour(image_contour, levels, extent=extent_contour, cmap=cmap, colors=colors, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py", line 1812, in inner
    return func(ax, *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/axes/_axes.py", line 5644, in contour
    return mcontour.QuadContourSet(self, *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/contour.py", line 1424, in __init__
    ContourSet.__init__(self, ax, *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/contour.py", line 960, in __init__
    zorder=zorder)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/collections.py", line 1149, in __init__
    self.set_segments(segments)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/collections.py", line 1158, in set_segments
    seg = np.asarray(seg, np.float_)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/core/numeric.py", line 474, in asarray
    return array(a, dtype, copy=False, order=order)
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:16:37.26 -13:23:10.29 14
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([14]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:16\:37.26_-13\:23\:10.29_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:19:47.86 -06:11:33.24 14
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([25]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 320, in __init__
    self._auto_v = image_util.percentile_function(self._data)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/image_util.py", line 75, in percentile_function
    array = np.sort(array)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/core/fromnumeric.py", line 819, in sort
    a.sort(axis, kind, order)
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:19:47.86 -06:11:33.24 25
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([25]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:20:21.97 -08:54:38.01 24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([89]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:20:21.97 -08:54:38.01 89
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([89]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:23:42.12 +00:28:25.62 14
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([63]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 320, in __init__
    self._auto_v = image_util.percentile_function(self._data)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/image_util.py", line 75, in percentile_function
    array = np.sort(array)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/core/fromnumeric.py", line 819, in sort
    a.sort(axis, kind, order)
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:23:42.12 +00:28:25.62 63
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([63]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:23:46.12 -00:03:29.92 14
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([85]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:23:46.12 -00:03:29.92 85
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([85]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:23:46.12 -00:03:29.92 85
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([85]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:23\:46.12_-00\:03\:29.92_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:24:24.50 -01:49:36.42 42
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:24:24.50 -01:49:36.42 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:25:46.87 -03:28:44.34 34
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([85]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:25:46.87 -03:28:44.34 85
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([85]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:27:39.57 -11:56:37.57 24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:27:39.57 -11:56:37.57 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:27:39.57 -11:56:37.57 47
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([47]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:27\:39.57_-11\:56\:37.57_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:48:11.71 -09:39:54.74 24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([12]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 320, in __init__
    self._auto_v = image_util.percentile_function(self._data)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/image_util.py", line 56, in percentile_function
    if np.all(np.isnan(array) | np.isinf(array)):
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:48:11.71 -09:39:54.74 12
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([12]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:58:48.05 -11:34:40.26 12
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([26]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:58:48.05 -11:34:40.26 26
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([26]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:58\:48.05_-11\:34\:40.26_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:59:15.86 -06:51:12.96 14
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([90]),)
^CTraceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 104, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[slic,0],subplot=(1,2,1))
  File "<string>", line 2, in __init__
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/decorators.py", line 25, in _auto_refresh
    return f(*args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 254, in __init__
    convention=convention, dimensions=dimensions, slices=slices)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/core.py", line 426, in _get_hdu
    wcs = wcs_util.WCS(header, dimensions=dimensions, slices=slices, relax=True)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/wcs_util.py", line 59, in __init__
    result = AstropyWCS.wcs_pix2world(self, coords, 1)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1329, in wcs_pix2world
    'output', *args, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1231, in _array_converter
    return _return_single_array(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1215, in _return_single_array
    result = func(xy, origin)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/wcs/wcs.py", line 1328, in <lambda>
    lambda xy, o: self.wcs.p2s(xy, o)['world'],
KeyboardInterrupt
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:59:15.86 -06:51:12.96 90
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([90]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:59:15.86 -06:51:12.96 90
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
(array([90]),)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:59\:15.86_-06\:51\:12.96_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:59:15.86 -06:51:12.96 90
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 138, in <module>
    ax1.text(frequency[60]/10**6, max_value, 'Local RMS='+str(RMS2), fontsize=12)
NameError: name 'max_value' is not defined
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:59:15.86 -06:51:12.96
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 138, in <module>
    ax1.text(frequency[60]/10**6, max_value, 'Local RMS='+str(RMS2), fontsize=12)
NameError: name 'max_value' is not defined
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits 05:59:15.86 -06:51:12.96
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Orion_99 Chenoachem$ open Orion_05\:59\:15.86_-06\:51\:12.96_99.3.png 
Chenoas-MacBook-Air:Orion_99 Chenoachem$ cd Cube_143/
Chenoas-MacBook-Air:Cube_143 Chenoachem$ cp ../Contour_Spectra_Plot.py .
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:23:53.78 -12:10:46.22
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:23:53.78 -12:10:46.22
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
open OChenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:23\:53.78_-12\:10\:400.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:39:01.90 -04:32:56.11
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:39:01.90 -04:32:56.11
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:39\:01.90_-04\:32\:56.11_100.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:42:44.48 -01:47:47.94
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:42:44.48 -01:47:47.94
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:42\:44.48_-01\:47\:47.94_100.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted_Inverted.fits 05:42:44.48 -01:47:47.94
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 61, in <module>
    datacube = fits.open(mycube)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/hdu/hdulist.py", line 138, in fitsopen
    return HDUList.fromfile(name, mode, memmap, save_backup, cache, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/hdu/hdulist.py", line 280, in fromfile
    save_backup=save_backup, cache=cache, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/hdu/hdulist.py", line 801, in _readfrom
    ffo = _File(fileobj, mode=mode, memmap=memmap, cache=cache)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/file.py", line 141, in __init__
    self._open_filename(fileobj, mode, clobber)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/file.py", line 493, in _open_filename
    self._file = fileobj_open(self.name, PYFITS_MODES[mode])
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/util.py", line 415, in fileobj_open
    return open(filename, mode)
IOError: [Errno 2] No such file or directory: 'Orion_I_143_Subtracted_Inverted.fits'
Chenoas-MacBook-Air:Cube_143 Chenoachem$ ls
Contour_Spectra_Plot.py
Orion_05:23:53.78_-12:10:46.22_100.62.png
Orion_05:39:01.90_-04:32:56.11_100.62.png
Orion_05:42:44.48_-01:47:47.94_100.62.png
Orion_I_143_Subtracted.fits
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:42:44.48 -01:47:47.94
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:42\:44.48_-01\:47\:47.94_100.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:48:31.08 -13:38:14.07
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:48\:31.08_-13\:38\:14.07_100.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:53:04.59 -15:35:59.01
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:53\:04.59_-15\:35\:59.01_100.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_143_Subtracted.fits 05:56:09.53 -01:38:54.44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:5
Orion_05:53:04.59_-15:35:59.01_100.62.png
Orion_05:56:09.53_-01:38:54.44_100.62.png
Chenoas-MacBook-Air:Cube_143 Chenoachem$ open Orion_05\:56\:09.53_-01\:38\:54.44_100.62.png 
Chenoas-MacBook-Air:Cube_143 Chenoachem$ cd ..
Chenoas-MacBook-Air:Orion_99 Chenoachem$ mkdir Cube_523
Chenoas-MacBook-Air:Orion_99 Chenoachem$ cd Cube_523/
Chenoas-MacBook-Air:Cube_523 Chenoachem$ scp ctremblay@galaxy.pawsey.org.au:/astro/mwasci/ctremblay/G0018_99/Cube_523_Grouped/*Subtracted.fits .
Orion_I_523_Subtracted.fits          100% 1526MB  18.0MB/s   01:25    
Chenoas-MacBook-Air:Cube_523 Chenoachem$ cp ../Contour_Spectra_Plot.py .
Chenoas-MacBook-Air:Cube_523 Chenoachem$ echo "# Spectra_Code" >> README.md
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git init
Initialized empty Git repository in /Users/Chenoachem/Documents/MWA Project Data/Orion_Testing/Orion_99/Cube_523/.git/
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git add Contour_Spectra_Plot.py 
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git commit -m "first commit"
[master (root-commit) f4a8a6f] first commit
 Committer: Chenoa Tremblay <Chenoachem@Chenoas-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 154 insertions(+)
 create mode 100644 Contour_Spectra_Plot.py
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git remote add origin https://github.com/Chenoachem/Spectra_Code.git
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git push -u origin master
Username for 'https://github.com': Chenoachem
Password for 'https://Chenoachem@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Chenoachem/Spectra_Code.git/'
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git push -u origin master
Username for 'https://github.com': Chenoachem
Password for 'https://Chenoachem@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Chenoachem/Spectra_Code.git/'
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git push -u origin master
Username for 'https://github.com': Chenoachem	
Password for 'https://Chenoachem@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/Chenoachem/Spectra_Code.git/'
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git push -u origin master
Username for 'https://github.com': Chenoachem	
Password for 'https://Chenoachem@github.com': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.95 KiB | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Chenoachem/Spectra_Code.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
Chenoas-MacBook-Air:Cube_523 Chenoachem$ cd ..
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
71.84575-13.677477777899.3.png
Contour_Spectra_Plot.py
Cube_143
Cube_523
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Max_Frequency.py
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_04:52:50.04_-12:07:49.85_99.3.png
Orion_04:54:57.15_+02:36:45.54_99.3.png
Orion_04:56:06.03_-02:29:17.93_99.3.png
Orion_05:01:07.48_-10:37:26.97_99.3.png
Orion_05:02:25.60_-07:49:54.28_99.3.png
Orion_05:10:38.21_-00:24:15.16_99.3.png
Orion_05:11:18.00_-06:26:14.96_99.3.png
Orion_05:11:30.49_+04:22:38.24_99.3.png
Orion_05:12:24.36_+05:10:15.01_99.3.png
Orion_05:13:39.80_-09:12:48.90_99.3.png
Orion_05:14:01.09_-15:46:42.94_99.3.png
Orion_05:14:07.95_-14:09:24.16_99.3.png
Orion_05:16:37.26_-13:23:10.29_99.3.png
Orion_05:19:47.86_-06:11:33.24_99.3.png
Orion_05:20:21.97_-08:54:38.01_99.3.png
Orion_05:23:42.12_+00:28:25.62_99.3.png
Orion_05:23:46.12_-00:03:29.92_99.3.png
Orion_05:24:24.50_-01:49:36.42_99.3.png
Orion_05:25:46.87_-03:28:44.34_99.3.png
Orion_05:27:19.38_-11:43:16.01_99.3.png
Orion_05:27:39.57_-11:56:37.57_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_05:48:11.71_-09:39:54.74_99.3.png
Orion_05:58:48.05_-11:34:40.26_99.3.png
Orion_05:59:15.86_-06:51:12.96_99.3.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_71.84575_-13.6774777778_99.3.png
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
SH.png
Slice_Test.py
Spectra_Plot.ipynb
Test_Plot.png
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:47:23 -13:40:39
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 30, in <module>
    cat_Files=sys.argv[4]
IndexError: list index out of range
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:47:23 -13:40:39
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99660000.0
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:47:23 -13:40:39
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.66
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:52:38 -10:36:16
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.75
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:52:50 -12:07:50
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.72
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:54:57 +2:36:45.54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.63
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:56:06 -2:29:18
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.84
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:01:07 -10:37:27
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.58
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:02:26 -7:49:54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:10:38 -0:24:15
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.73
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:11:18 -6:26:15
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.63
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:11:30 +4:22:38.24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:12:24 +5:10:15.01
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.64
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:13:40 -9:12:49
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.72
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:14:01 -15:46:43
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.84
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:14:08 -14:09:24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.2
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:16:37 -13:23:10
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.44
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:19:48 -6:11:33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.55
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:20:22 -8:54:38
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.19
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:23:42 +00:28:25.62
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.93
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:23:46 -0:03:30
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.15
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:24:25 -1:49:36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:25:47 -3:28:44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.15
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:27:19 -11:43:16
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.56
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:27:40 -11:56:38
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:48:12 -9:39:55
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.42
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:58:48 -11:34:40
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.56
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:59:16 -6:51:13
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.2
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Orion_I_143_Subtracted.fits 5:23:54 -12:10:46
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 37, in <module>
    datacube = fits.open(mycube)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/hdu/hdulist.py", line 138, in fitsopen
    return HDUList.fromfile(name, mode, memmap, save_backup, cache, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/hdu/hdulist.py", line 280, in fromfile
    save_backup=save_backup, cache=cache, **kwargs)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/hdu/hdulist.py", line 801, in _readfrom
    ffo = _File(fileobj, mode=mode, memmap=memmap, cache=cache)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/file.py", line 141, in __init__
    self._open_filename(fileobj, mode, clobber)
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/file.py", line 493, in _open_filename
    self._file = fileobj_open(self.name, PYFITS_MODES[mode])
  File "/Users/Chenoachem/anaconda/lib/python2.7/site-packages/astropy/io/fits/util.py", line 415, in fileobj_open
    return open(filename, mode)
IOError: [Errno 2] No such file or directory: 'Orion_I_143_Subtracted.fits'
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:23:54 -12:10:46
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.28
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:39:02 -4:32:56
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.28
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:42:44 -1:47:48
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.08
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:48:32 -8:39:29
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.3
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:53:05 -15:35:59
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.02
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:56:10 -1:38:54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.31
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:56:10 -1:38:54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
Traceback (most recent call last):
  File "Max_Frequency.py", line 76, in <module>
    print "Frequecy at Max is "+frequency[sli]/10**6
TypeError: ufunc 'add' did not contain a loop with signature matching types dtype('S32') dtype('S32') dtype('S32')
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:56:10 -1:38:54
  File "Max_Frequency.py", line 76
    print "Frequecy at Max is " frequency[sli]/10**6
                                        ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:56:10 -1:38:54
  File "Max_Frequency.py", line 76
    print "Frequecy at Max is "frequency[sli]/10**6
                                       ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Max_Frequency.py Cube_143/Orion_I_143_Subtracted.fits 5:56:10 -1:38:54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
101.31
4.18691
Chenoas-MacBook-Air:Orion_99 Chenoachem$ cd Cube_274/
Chenoas-MacBook-Air:Cube_274 Chenoachem$ scp ctremblay@galaxy.pawsey.org.au:/astro/mwasci/ctremblay/G0018_99/Cube_274_Grouped/Orion*I*Subtracted.fits .
Orion_I_274_Subtracted.fits       100% 1526MB  18.4MB/s   01:23    
Chenoas-MacBook-Air:Cube_274 Chenoachem$ ls
Contour_Spectra_Plot.py		Orion_I_274_Subtracted.fits
Max_Frequency.py		ra_dec_cat
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 33, in <module>
    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
NameError: name 'ra' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 33, in <module>
    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
NameError: name 'ra' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 33, in <module>
    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
NameError: name 'ra' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 33, in <module>
    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
NameError: name 'ra' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 33, in <module>
    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
NameError: name 'ra' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 33, in <module>
    c = SkyCoord(ra, dec, unit=(u.hourangle, u.deg))
NameError: name 'ra' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 78, in <module>
    file=open(cat_files)
NameError: name 'cat_files' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 124, in <module>
    fig=aplpy.FITSFigure(datadir+mycube,figure=bigfig,slices=[sli,0],subplot=(1,2,1))
NameError: name 'datadir' is not defined
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_274_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 80, in <module>
    ra,dec = line.strip().split(",")
ValueError: need more than 1 value to unpack
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 05:31:54.93 -07:50:48.07
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.05
4.66034
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 05:20:54.64,-08:01:34.46
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 28, in <module>
    dec=sys.argv[3]
IndexError: list index out of range
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 05:20:54.64 -08:01:34.46
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
3.48508
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:00:29 -4:52:48
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.82344
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:00:50 -7:33:53
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
3.96713
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:08:16 -12:17:10
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.03
4.31465
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:11:18+00:29:15.95
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 28, in <module>
    dec=sys.argv[3]
IndexError: list index out of range
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:11:18 +00:29:15.95
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.25085
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:15:37 -1:34:04
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.71066
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:17:39 -13:42:13
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.42161
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:20:55 -8:01:34
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
3.48508
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:22:22 -14:53:40
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.2
4.01587
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:24:10-15:17:44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 28, in <module>
    dec=sys.argv[3]
IndexError: list index out of range
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:24:10 -15:17:44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.03212
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:31:11 +01:35:22.62
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.34
4.5352
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:31:55-7:50:48
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 28, in <module>
    dec=sys.argv[3]
IndexError: list index out of range
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:31:55 -7:50:48
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.05
4.66034
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:36:37 +04:45:13.40
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.0708
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:39:03 -5:19:56
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.31297
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:40:37 +05:39:01.23
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.1
4.68479
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 5:46:54 -8:40:24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.03
4.4084
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 6:03:10 -2:47:33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.11
3.54433
Chenoas-MacBook-Air:Cube_274 Chenoachem$ python Max_Frequency.py Orion_I_274_Subtracted.fits 6:16:28 +00:18:36.15
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
102.5
4.65187
Chenoas-MacBook-Air:Cube_274 Chenoachem$ cd ..
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
71.84575-13.677477777899.3.png
Contour_Spectra_Plot.py
Cube_143
Cube_274
Cube_523
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Max_Frequency.py
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_04:52:50.04_-12:07:49.85_99.3.png
Orion_04:54:57.15_+02:36:45.54_99.3.png
Orion_04:56:06.03_-02:29:17.93_99.3.png
Orion_05:01:07.48_-10:37:26.97_99.3.png
Orion_05:02:25.60_-07:49:54.28_99.3.png
Orion_05:10:38.21_-00:24:15.16_99.3.png
Orion_05:11:18.00_-06:26:14.96_99.3.png
Orion_05:11:30.49_+04:22:38.24_99.3.png
Orion_05:12:24.36_+05:10:15.01_99.3.png
Orion_05:13:39.80_-09:12:48.90_99.3.png
Orion_05:14:01.09_-15:46:42.94_99.3.png
Orion_05:14:07.95_-14:09:24.16_99.3.png
Orion_05:16:37.26_-13:23:10.29_99.3.png
Orion_05:19:47.86_-06:11:33.24_99.3.png
Orion_05:20:21.97_-08:54:38.01_99.3.png
Orion_05:23:42.12_+00:28:25.62_99.3.png
Orion_05:23:46.12_-00:03:29.92_99.3.png
Orion_05:24:24.50_-01:49:36.42_99.3.png
Orion_05:25:46.87_-03:28:44.34_99.3.png
Orion_05:27:19.38_-11:43:16.01_99.3.png
Orion_05:27:39.57_-11:56:37.57_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_05:48:11.71_-09:39:54.74_99.3.png
Orion_05:58:48.05_-11:34:40.26_99.3.png
Orion_05:59:15.86_-06:51:12.96_99.3.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_71.84575_-13.6774777778_99.3.png
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
SH.png
Slice_Test.py
Spectra_Plot.ipynb
Test_Plot.png
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ra_dec_cat
-bash: ra_dec_cat: command not found
Chenoas-MacBook-Air:Orion_99 Chenoachem$ vi ra_dec_cat
Chenoas-MacBook-Air:Orion_99 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_013_Subtracted.fits ra_dec_cat 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
Traceback (most recent call last):
  File "Contour_Spectra_Plot.py", line 80, in <module>
    ra,dec = line.strip().split(",")
ValueError: too many values to unpack
Chenoas-MacBook-Air:Orion_99 Chenoachem$ ls
1132158368_shallow_test2-image.fits
1132168688_self_solutions_amp.png
1132168688_self_solutions_phase.png
4sigabs_12_isle.fits
71.84575-13.677477777899.3.png
Contour_Spectra_Plot.py
Cube_143
Cube_274
Cube_523
Cube_Quality_Checks.ipynb
Histogram10.png
Histogram12.png
Histogram_12.png
Histogram_Plots.py
Max_Frequency.py
Orion_04:47:22.98_-13:40:38.92_99.3.png
Orion_04:52:38.19_-10:36:15.79_99.3.png
Orion_04:52:50.04_-12:07:49.85_99.3.png
Orion_04:54:57.15_+02:36:45.54_99.3.png
Orion_04:56:06.03_-02:29:17.93_99.3.png
Orion_05:01:07.48_-10:37:26.97_99.3.png
Orion_05:02:25.60_-07:49:54.28_99.3.png
Orion_05:10:38.21_-00:24:15.16_99.3.png
Orion_05:11:18.00_-06:26:14.96_99.3.png
Orion_05:11:30.49_+04:22:38.24_99.3.png
Orion_05:12:24.36_+05:10:15.01_99.3.png
Orion_05:13:39.80_-09:12:48.90_99.3.png
Orion_05:14:01.09_-15:46:42.94_99.3.png
Orion_05:14:07.95_-14:09:24.16_99.3.png
Orion_05:16:37.26_-13:23:10.29_99.3.png
Orion_05:19:47.86_-06:11:33.24_99.3.png
Orion_05:20:21.97_-08:54:38.01_99.3.png
Orion_05:23:42.12_+00:28:25.62_99.3.png
Orion_05:23:46.12_-00:03:29.92_99.3.png
Orion_05:24:24.50_-01:49:36.42_99.3.png
Orion_05:25:46.87_-03:28:44.34_99.3.png
Orion_05:27:19.38_-11:43:16.01_99.3.png
Orion_05:27:39.57_-11:56:37.57_99.3.png
Orion_05:37:19.83_111.0_.png
Orion_05:48:11.71_-09:39:54.74_99.3.png
Orion_05:58:48.05_-11:34:40.26_99.3.png
Orion_05:59:15.86_-06:51:12.96_99.3.png
Orion_06:24:42.07_111.0_.png
Orion_400_Continuum.fits
Orion_400_Subtracted.fits
Orion_400_Subtracted_Moment.fits
Orion_4:47:23_-13:40:39_99.3.png
Orion_4:52:38_-10:36:16_99.3.png
Orion_4:52:50_-12:07:50_99.3.png
Orion_4:54:57_+2:36:45.54_99.3.png
Orion_4:56:06_-2:29:18_99.3.png
Orion_5:01:07_-10:37:27_99.3.png
Orion_5:02:26_-7:49:54_99.3.png
Orion_5:10:38_-0:24:15_99.3.png
Orion_5:11:18_-6:26:15_99.3.png
Orion_5:11:30_+4:22:38.24_99.3.png
Orion_5:12:24_+5:10:15.01_99.3.png
Orion_5:13:40_-9:12:49_99.3.png
Orion_5:14:01_-15:46:43_99.3.png
Orion_5:14:08_-14:09:24_99.3.png
Orion_71.84575_-13.6774777778_99.3.png
Orion_I_013_Subtracted.fits
Orion_I_1160_Continuum.fits
Orion_I_1160_Subtracted.fits
Orion_I_1160_Subtracted.fits 2
Orion_RMS.png
Orion_rms.fits
Orion_rms.fits 2
Orion_rms_fix.fits
Orion_snr.fits
RMS.png
RMS_Image.py
Recombination_Line_Spectra.py
SH.png
Slice_Test.py
Spectra_Plot.ipynb
Test_Plot.png
Untitled.ipynb
cube_slice.py
new_1132158368_1132158488_coarse-MFS-image.fits
new_1132158368_1132158488_cube_786-MFS-image.fits
new_1132160528_1132160648_cube_786-0061-image.fits
ra_dec_cat
Chenoas-MacBook-Air:Orion_99 Chenoachem$ cd Cube_13/
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:47:23 -13:40:39
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.66
0.335934
3.8479
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:52:38 -10:36:16
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.75
0.330199
4.10504
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:52:50 -12:07:50
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.72
0.315998
3.78235
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:54:57 +2:36:45.54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.63
0.345246
3.96289
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 4:56:06 -2:29:18
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.84
0.299652
4.37783
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:01:07 -10:37:27
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.58
0.298188
4.0465
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:02:26 -7:49:54
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
0.234876
4.26893
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:10:38 -0:24:15
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.73
0.276328
3.95812
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:11:18 -6:26:15
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.63
0.21466
3.95961
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:11:30 +4:22:38.24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
0.378798
4.30562
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:12:24 +5:10:15.01
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.64
0.351135
4.26033
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:13:40 -9:12:49
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.72
0.213954
3.85982
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:14:01 -15:46:43
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.84
0.243343
4.07992
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:14:08 -14:09:24
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.2
0.231644
4.10794
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:16:37 -13:23:10
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.44
0.226786
4.42543
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:19:48 -6:11:33
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.55
0.219
4.32303
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:20:22 -8:54:38
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.19
0.207515
4.64565
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:23:42+00:28:25.62
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 28, in <module>
    dec=sys.argv[3]
IndexError: list index out of range
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:23:42 +00:28:25.62
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.93
0.271279
3.99076
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:23:46 -0:03:30
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.15
0.251073
4.29356
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:24:25 -1:49:36
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
0.200708
3.94821
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:25:47 -3:28:44
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.15
0.183066
4.31688
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:27:19 -11:43:16
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.56
0.209335
4.9007
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:27:40 -11:56:38
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.77
0.211163
4.51487
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:48:12 -9:39:55
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.42
0.212297
3.80389
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:58:48 -11:34:40
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
99.56
0.189227
4.58555
Chenoas-MacBook-Air:Cube_13 Chenoachem$ python Max_Frequency.py Orion_I_013_Subtracted.fits 5:59:16 -6:51:13
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
100.2
0.231829
4.53968
Chenoas-MacBook-Air:Cube_13 Chenoachem$ cd ..
Chenoas-MacBook-Air:Orion_99 Chenoachem$ cd Cube_523/
Chenoas-MacBook-Air:Cube_523 Chenoachem$ vi ra_dec_cat2 
Chenoas-MacBook-Air:Cube_523 Chenoachem$ ls
Contour_Spectra_Plot.py		README.md
Orion_I_523_Subtracted.fits	ra_dec_cat2
Chenoas-MacBook-Air:Cube_523 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_523_Subtracted.fits ra_dec_cat2 
  File "Contour_Spectra_Plot.py", line 47
    Invert the cube for absorption
             ^
SyntaxError: invalid syntax
Chenoas-MacBook-Air:Cube_523 Chenoachem$ vi Contour_Spectra_Plot.py 
Chenoas-MacBook-Air:Cube_523 Chenoachem$ cp ../Cube_274/Contour_Spectra_Plot.py 
usage: cp [-R [-H | -L | -P]] [-fi | -n] [-apvX] source_file target_file
       cp [-R [-H | -L | -P]] [-fi | -n] [-apvX] source_file ... target_directory
Chenoas-MacBook-Air:Cube_523 Chenoachem$ cp ../Cube_274/Contour_Spectra_Plot.py .
Chenoas-MacBook-Air:Cube_523 Chenoachem$ python Contour_Spectra_Plot.py Orion_I_523_Subtracted.fits ra_dec_cat2 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/artist.py:221: MatplotlibDeprecationWarning: This has been deprecated in mpl 1.5, please use the
axes property.  A removal date has not been set.
  warnings.warn(_get_axes_msg, mplDeprecation, stacklevel=1)
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/tight_layout.py:222: UserWarning: tight_layout : falling back to Agg renderer
  warnings.warn("tight_layout : falling back to Agg renderer")
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/aplpy/labels.py:432: UnicodeWarning: Unicode equal comparison failed to convert both arguments to Unicode - interpreting them as being unequal
  if self.coord == x or self.axis.apl_tick_positions_world[ipos] > 0:
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/pyplot.py:516: RuntimeWarning: More than 20 figures have been opened. Figures created through the pyplot interface (`matplotlib.pyplot.figure`) are retained until explicitly closed and may consume too much memory. (To control this warning, see the rcParam `figure.max_open_warning`).
  max_open_warning, RuntimeWarning)
Chenoas-MacBook-Air:Cube_523 Chenoachem$ ls
Contour_Spectra_Plot.py
Orion_04:42:21.56_-08:27:11.39_104.42.png
Orion_04:43:19.42_-06:45:26.80_104.42.png
Orion_04:43:41.54_-07:05:38.30_104.42.png
Orion_04:44:05.95_-09:54:42.74_104.42.png
Orion_04:45:33.08_-15:23:04.94_104.42.png
Orion_04:46:39.25_-13:42:10.80_104.42.png
Orion_04:47:21.66_-09:45:36.09_104.42.png
Orion_04:47:30.11_-08:34:40.50_104.42.png
Orion_04:47:50.84_-02:10:37.96_104.42.png
Orion_04:48:07.66_+00:34:59.23_104.42.png
Orion_04:48:20.50_-04:14:33.16_104.42.png
Orion_04:48:24.45_-01:04:56.21_104.42.png
Orion_04:50:40.88_-14:58:25.08_104.42.png
Orion_04:51:12.29_-07:00:44.04_104.42.png
Orion_04:51:18.25_-14:37:34.05_104.42.png
Orion_04:51:36.60_-10:20:47.25_104.42.png
Orion_04:52:11.72_-01:16:26.91_104.42.png
Orion_04:54:35.51_+02:30:56.47_104.42.png
Orion_04:54:58.96_-01:56:36.08_104.42.png
Orion_04:55:39.09_-06:21:13.60_104.42.png
Orion_04:59:34.96_-04:13:10.58_104.42.png
Orion_05:00:14.10_-08:45:04.89_104.42.png
Orion_05:01:10.53_-09:51:31.49_104.42.png
Orion_05:01:15.13_+00:50:39.14_104.42.png
Orion_05:02:03.25_+02:33:20.12_104.42.png
Orion_05:04:32.64_-04:57:49.13_104.42.png
Orion_05:06:53.71_-17:48:11.28_104.42.png
Orion_05:07:52.03_-17:57:55.22_104.42.png
Orion_05:08:24.12_-11:16:46.79_104.42.png
Orion_05:09:16.49_-15:07:34.51_104.42.png
Orion_05:09:29.71_-11:40:05.18_104.42.png
Orion_05:12:12.22_-17:40:57.92_104.42.png
Orion_05:13:20.11_-06:50:50.62_104.42.png
Orion_05:14:01.08_-11:16:56.91_104.42.png
Orion_05:16:23.28_-00:37:52.58_104.42.png
Orion_05:26:41.81_-05:25:02.56_104.42.png
Orion_05:26:41.96_-03:45:06.93_104.42.png
Orion_05:28:28.39_-04:53:03.13_104.42.png
Orion_05:31:46.78_+01:27:54.68_104.42.png
Orion_05:33:39.48_-13:16:20.40_104.42.png
Orion_05:34:14.50_-01:10:37.52_104.42.png
Orion_05:35:00.20_-05:48:45.75_104.42.png
Orion_05:42:13.20_-14:47:13.63_104.42.png
Orion_05:45:59.06_-00:34:19.42_104.42.png
Orion_05:48:35.75_-18:13:43.45_104.42.png
Orion_05:49:26.11_+03:19:54.18_104.42.png
Orion_05:50:22.52_-00:13:12.41_104.42.png
Orion_05:51:00.23_-14:52:33.73_104.42.png
Orion_05:51:22.58_-03:07:57.38_104.42.png
Orion_05:53:10.18_-00:17:15.67_104.42.png
Orion_05:53:10.23_+04:51:29.91_104.42.png
Orion_05:53:34.85_-13:01:18.11_104.42.png
Orion_05:56:39.30_-07:03:30.66_104.42.png
Orion_05:56:39.78_-10:23:37.96_104.42.png
Orion_05:57:28.31_-02:13:19.09_104.42.png
Orion_05:58:48.83_+00:05:30.58_104.42.png
Orion_06:00:09.56_-04:29:58.48_104.42.png
Orion_06:04:56.94_-00:54:24.88_104.42.png
Orion_06:06:12.30_-05:45:56.74_104.42.png
Orion_06:07:32.40_-03:56:51.24_104.42.png
Orion_06:08:25.70_-11:17:27.93_104.42.png
Orion_06:09:23.69_+00:50:16.67_104.42.png
Orion_06:12:23.98_-12:16:13.38_104.42.png
Orion_06:17:50.80_-02:19:34.89_104.42.png
Orion_06:19:44.78_-14:30:43.38_104.42.png
Orion_06:19:45.16_-03:06:15.79_104.42.png
Orion_06:21:10.41_-07:31:25.34_104.42.png
Orion_06:22:45.87_-03:16:02.36_104.42.png
Orion_I_523_Subtracted.fits
README.md
ra_dec_cat2
Chenoas-MacBook-Air:Cube_523 Chenoachem$ python Max_Frequency.py Orion_I_523_Subtracted.fits ra_dec_cat2 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 28, in <module>
    dec=sys.argv[3]
IndexError: list index out of range
Chenoas-MacBook-Air:Cube_523 Chenoachem$ python Max_Frequency.py Orion_I_523_Subtracted.fits ra_dec_cat2 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
Traceback (most recent call last):
  File "Max_Frequency.py", line 32, in <module>
    file=open(cat_files)
NameError: name 'cat_files' is not defined
Chenoas-MacBook-Air:Cube_523 Chenoachem$ vi Max_Frequency.py 
Chenoas-MacBook-Air:Cube_523 Chenoachem$ python Max_Frequency.py Orion_I_523_Subtracted.fits ra_dec_cat2 
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/matplotlib/__init__.py:1350: UserWarning:  This call to matplotlib.use() has no effect
because the backend has already been chosen;
matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
or matplotlib.backends is imported for the first time.

  warnings.warn(_use_error_msg)
WARNING: VerifyWarning: Invalid 'BLANK' keyword in header.  The 'BLANK' keyword is only applicable to integer data, and will be ignored in this HDU. [astropy.io.fits.hdu.image]
/Users/Chenoachem/anaconda/lib/python2.7/site-packages/numpy/lib/nanfunctions.py:675: RuntimeWarning: Mean of empty slice
  warnings.warn("Mean of empty slice", RuntimeWarning)
104.79
0.371175
3.47397
105.1
0.390282
3.49633
104.88
0.352895
3.69407
105.09
0.397826
4.15462
105.09
0.439242
4.26537
105.09
0.367017
4.08967
105.09
0.297853
4.12701
105.09
0.299234
5.05865
105.09
0.363925
4.46432
105.09
0.358324
4.24198
105.09
0.313113
5.09168
105.09
0.352576
5.40786
105.09
0.332879
4.49785
105.09
0.242992
4.79932
104.88
0.327586
4.92057
105.09
0.27855
4.58366
104.79
0.289645
4.15972
105.09
0.366736
5.61665
105.09
0.247123
4.79563
105.09
0.242763
5.44204
105.09
0.215085
4.33016
105.09
0.204909
5.35751
105.21
0.210568
4.6711
105.09
0.26579
4.84685
105.09
0.30147
5.41279
104.84
0.198183
4.16393
104.88
0.385956
4.66283
104.88
0.338702
4.36549
105.09
0.170613
4.69621
104.88
0.238393
5.5116
104.88
0.202049
4.766
105.21
0.315028
4.29624
105.09
0.184713
5.39807
104.88
0.183561
4.5842
105.09
0.224115
3.57118
105.09
0.179528
3.78568
105.09
0.193486
4.61322
104.53
0.160156
4.19349
104.79
0.240837
4.35775
105.09
0.190988
4.65884
104.53
0.200444
4.4168
105.21
0.183695
5.15959
104.88
0.17276
4.53396
104.52
0.207828
4.53825
104.88
0.32334
4.27965
105.01
0.275872
4.77945
104.64
0.208689
4.21254
105.09
0.201609
4.81291
105.09
0.168553
4.82501
105.09
0.197925
4.55368
105.09
0.320303
3.88327
104.79
0.186483
3.93067
105.09
0.196255
5.194
105.09
0.202645
3.29737
105.09
0.227289
3.90624
104.79
0.247899
4.38655
105.09
0.223129
4.80214
104.97
0.264999
4.22306
105.19
0.199721
4.08281
105.09
0.200582
3.23097
105.21
0.219068
4.40282
104.79
0.28748
4.21349
104.88
0.251043
4.3239
105.09
0.313927
4.48387
104.99
0.323982
4.48664
105.09
0.345345
4.99407
104.89
0.310272
4.68165
104.62
0.371516
4.84485
Chenoas-MacBook-Air:Cube_523 Chenoachem$ echo "# Spectra_Code" >> README.md
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git add Max_Frequency.py 
Chenoas-MacBook-Air:Cube_523 Chenoachem$ git push -u origin master
To https://github.com/Chenoachem/Spectra_Code.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Chenoachem/Spectra_Code.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Chenoas-MacBook-Air:Cube_523 Chenoachem$ vi Max_Frequency.py 
Chenoas-MacBook-Air:Cube_523 Chenoachem$ ls
Contour_Spectra_Plot.py
Max_Frequency.py
Orion_04:42:21.56_-08:27:11.39_104.42.png
Orion_04:43:19.42_-06:45:26.80_104.42.png
Orion_04:43:41.54_-07:05:38.30_104.42.png
Orion_04:44:05.95_-09:54:42.74_104.42.png
Orion_04:45:33.08_-15:23:04.94_104.42.png
Orion_04:46:39.25_-13:42:10.80_104.42.png
Orion_04:47:21.66_-09:45:36.09_104.42.png
Orion_04:47:30.11_-08:34:40.50_104.42.png
Orion_04:47:50.84_-02:10:37.96_104.42.png
Orion_04:48:07.66_+00:34:59.23_104.42.png
Orion_04:48:20.50_-04:14:33.16_104.42.png
Orion_04:48:24.45_-01:04:56.21_104.42.png
Orion_04:50:40.88_-14:58:25.08_104.42.png
Orion_04:51:12.29_-07:00:44.04_104.42.png
Orion_04:51:18.25_-14:37:34.05_104.42.png
Orion_04:51:36.60_-10:20:47.25_104.42.png
Orion_04:52:11.72_-01:16:26.91_104.42.png
Orion_04:54:35.51_+02:30:56.47_104.42.png
Orion_04:54:58.96_-01:56:36.08_104.42.png
Orion_04:55:39.09_-06:21:13.60_104.42.png
Orion_04:59:34.96_-04:13:10.58_104.42.png
Orion_05:00:14.10_-08:45:04.89_104.42.png
Orion_05:01:10.53_-09:51:31.49_104.42.png
Orion_05:01:15.13_+00:50:39.14_104.42.png
Orion_05:02:03.25_+02:33:20.12_104.42.png
Orion_05:04:32.64_-04:57:49.13_104.42.png
Orion_05:06:53.71_-17:48:11.28_104.42.png
Orion_05:07:52.03_-17:57:55.22_104.42.png
Orion_05:08:24.12_-11:16:46.79_104.42.png
Orion_05:09:16.49_-15:07:34.51_104.42.png
Orion_05:09:29.71_-11:40:05.18_104.42.png
Orion_05:12:12.22_-17:40:57.92_104.42.png
Orion_05:13:20.11_-06:50:50.62_104.42.png
Orion_05:14:01.08_-11:16:56.91_104.42.png
Orion_05:16:23.28_-00:37:52.58_104.42.png
Orion_05:26:41.81_-05:25:02.56_104.42.png
Orion_05:26:41.96_-03:45:06.93_104.42.png
Orion_05:28:28.39_-04:53:03.13_104.42.png
Orion_05:31:46.78_+01:27:54.68_104.42.png
Orion_05:33:39.48_-13:16:20.40_104.42.png
Orion_05:34:14.50_-01:10:37.52_104.42.png
Orion_05:35:00.20_-05:48:45.75_104.42.png
Orion_05:42:13.20_-14:47:13.63_104.42.png
Orion_05:45:59.06_-00:34:19.42_104.42.png
Orion_05:48:35.75_-18:13:43.45_104.42.png
Orion_05:49:26.11_+03:19:54.18_104.42.png
Orion_05:50:22.52_-00:13:12.41_104.42.png
Orion_05:51:00.23_-14:52:33.73_104.42.png
Orion_05:51:22.58_-03:07:57.38_104.42.png
Orion_05:53:10.18_-00:17:15.67_104.42.png
Orion_05:53:10.23_+04:51:29.91_104.42.png
Orion_05:53:34.85_-13:01:18.11_104.42.png
Orion_05:56:39.30_-07:03:30.66_104.42.png
Orion_05:56:39.78_-10:23:37.96_104.42.png
Orion_05:57:28.31_-02:13:19.09_104.42.png
Orion_05:58:48.83_+00:05:30.58_104.42.png
Orion_06:00:09.56_-04:29:58.48_104.42.png
Orion_06:04:56.94_-00:54:24.88_104.42.png
Orion_06:06:12.30_-05:45:56.74_104.42.png
Orion_06:07:32.40_-03:56:51.24_104.42.png
Orion_06:08:25.70_-11:17:27.93_104.42.png
Orion_06:09:23.69_+00:50:16.67_104.42.png
Orion_06:12:23.98_-12:16:13.38_104.42.png
Orion_06:17:50.80_-02:19:34.89_104.42.png
Orion_06:19:44.78_-14:30:43.38_104.42.png
Orion_06:19:45.16_-03:06:15.79_104.42.png
Orion_06:21:10.41_-07:31:25.34_104.42.png
Orion_06:22:45.87_-03:16:02.36_104.42.png
Orion_I_523_Subtracted.fits
README.md
ra_dec_cat2
Chenoas-MacBook-Air:Cube_523 Chenoachem$ vi Contour_Spectra_Plot.py 

    ax1.step(frequency/10**6,signal,color='white',linewidth=2)
    ax1.set_xlabel("Frequency (MHz)", fontsize=12)
    ax1.set_ylabel("Flux (Jy)", fontsize=12 )
    ax1.text(frequency[60]/10**6, max_value, 'Local RMS='+str(RMS2), fontsize=12)
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
