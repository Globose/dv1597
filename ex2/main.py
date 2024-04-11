import numpy as np
import matplotlib.pyplot as mpl
import scipy.stats as stats

with open('data.txt', 'r') as file:
    A = []
    for f in file:
        nums = f.strip().split(',')
        A.extend(nums)
    B = []

    for a in A:
        if a == '':
            continue
        B.append((float)(a.strip()))
    array = np.array(B)

    fig = mpl.figure()
    ax = fig.add_subplot()
    num_bins = 15
    ax.hist(array, bins=num_bins, label="Datatata", linewidth=3, color='skyblue')

    bin_width = (array.max() - array.min()) / num_bins
    mu = array.mean()
    sigma = array.std()

    print(mu, sigma)

    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    mpl.plot(x, stats.norm.pdf(x, mu, sigma)*100*bin_width, color='red')
    mpl.show()
