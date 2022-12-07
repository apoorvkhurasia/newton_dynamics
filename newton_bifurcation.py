from pylab import *
from numpy import NaN
from matplotlib.colors import LogNorm
import time
from sys import getsizeof

dr, dx = .001/4, .001/4

# Perform max_it iterations at a time, repeated over it_cyc cycles.
# (This is done so that the memory requirement for the out array
# does not get too big. Lower max_it if you do not have enough free RAM.)
max_it = 10000
it_cyc = 10

R = arange(0.3, 0.5, dr)
X = arange(-5, 2, dx)
Z = zeros((len(X), len(R)))

z = zeros((len(R)))
out = zeros((max_it, len(R)))

for cy in range(it_cyc):
    z[:] = (cy + .5) / it_cyc  # use different starting values, not just 0.25
    for i in range(1000):
        z[:] = (R[:]/(R[:] + 1)) * (z[:] + 1/z[:] - (R[:] - 1)/R[:])

    for i in range(max_it):
        z[:] = (R[:]/(R[:] + 1)) * (z[:] + 1/z[:] - (R[:] - 1)/R[:])
        out[i, :] = z[:]

    for ir, r in enumerate(R):
        h = histogram(out[:, ir], bins=list(X))[0]
        Z[1:, ir] += h[::-1]

for ir, r in enumerate(R):
    Z[:, ir] *= count_nonzero(Z[:, ir])

Z = where(Z > 0, Z, NaN)
save("logmap", Z)  # save array to file

# pick color bar range:
zmi = .001 * nanmax(Z)
zma = .1 * nanmax(Z)

imshow(Z, cmap=plt.cm.inferno_r,
       interpolation='none', norm=LogNorm(zmi, zma), aspect="auto",
       extent=(R.min(), R.max(), X.min(), X.max()))
xlabel("r")
ylabel("x")
axis((0.3, 0.5, -5, 2))

ax = plt.gca()
ax.set_facecolor((1, 1, 1))

savefig("bifurcation.png", format="png", dpi=300)
print("===", max_it * it_cyc, "total iterations")
print("===", int(time.time() - start), "s total time")
show()
