import numpy as np
from scipy import interpolate
from astropy.io import fits
from matplotlib import pyplot as plt


def datapreview(filename, file_path, png_path):
    label_font = {
                'family': 'serif',
                'color': '#000000',
                'weight': 'normal',
                'size': 19,
                }

    wave_begin = 5000
    wave_end = 8910
    wavelengthT = np.linspace(wave_begin, wave_end, wave_end-wave_begin)

    fits_data = fits.open(file_path + '/' + filename)
    data = fits_data[0].data
    lamost_data1 = data[0, :]   # 流量
    lamost_wave1 = data[2, :]   # 波长
    fluxnorm = (lamost_data1-min(lamost_data1))/(max(lamost_data1) - min(lamost_data1))     # 流量归一化
    flux_inter = interpolate.interp1d(lamost_wave1, fluxnorm, kind='cubic')     # 插值
    flux = flux_inter(wavelengthT)

    # 绘图
    fig = plt.figure(facecolor='w', figsize=(11, 9))
    ax = plt.subplot(111)
    x = wavelengthT
    y = flux
    ax.plot(x, y)
    ax.set_xlabel('Wavelength', fontdict=label_font)
    ax.set_ylabel('Flux', fontdict=label_font)
    ax.set_title(str(filename), fontdict=label_font)
    axis_label = ax.get_xticklabels() + ax.get_yticklabels()
    [label.set_fontsize(15) for label in axis_label]
    fig.savefig(png_path + "/" + str(filename) + ".png")
    plt.close()

    n_sum = 0
    count = 0
    for i in flux:
        count += 1
        n_sum += float(i)
    max_value = max(flux)
    min_value = min(flux)
    mean_value = n_sum/count
    sbsq = sum([(float(i) - float(mean_value)) ** 2 for i in flux])
    stdev = (sbsq/(len(flux)-1)) ** .5

    max_value = round(max_value, 3)
    min_value = round(min_value, 3)
    mean_value = round(mean_value, 3)
    stdev = round(stdev, 3)

    return max_value, min_value, mean_value, stdev
