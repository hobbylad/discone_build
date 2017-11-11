f = 110e6
wl = 3e8 / f
cmax = (wl / 4.0) * 0.96
cmin = cmax / 22.0
D = cmax * 0.7
S = 0.3 * cmin

print 'Discone design parameters for frequency: %.1fMHz (%.3fm)' % ((f / 1e6), round(wl, 3))
print 'L = cmax: %.3fm' % round(cmax, 3)
print 'D: %.3fm' % round(D, 3)
print 'cmin: %.3fm' % round(cmin, 3)
print 'S: %.3fm' % round(S, 3)