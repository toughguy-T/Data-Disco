import numpy as np
import pandas as pd
from scipy import interpolate
from astropy.io import fits
"""读取fits数据，作插值与归一化处理后输出。"""
"""调整了格式，但代码还是繁琐，可以考虑用字典类型存储数据key为fitname，value为流量列表"""


def action(filenames, file_path, csv_path):
    wave_begin = 5000
    wave_end = 8910
    wavelengthT = np.linspace(wave_begin, wave_end, wave_end-wave_begin)
    flux_array = []

    for filename in filenames:
        fits_data = fits.open(file_path + '/' + filename)
        data = fits_data[0].data
        lamost_data1 = data[0, :]   # 流量
        lamost_wave1 = data[2, :]   # 波长
        fluxnorm = (lamost_data1-min(lamost_data1))/(max(lamost_data1) - min(lamost_data1))     # 流量归一化
        flux_inter = interpolate.interp1d(lamost_wave1, fluxnorm, kind='cubic')     # 插值
        flux = [filename]
        flux[1:] = flux_inter(wavelengthT)

        flux_array.append(flux)    # 匹配

    column_index = ['Name']
    flag = 1
    for i in range(wave_end - wave_begin):
        string = 'C' + str(flag)
        column_index.append(string)
        flag = flag + 1

    csv_dataframe = pd.DataFrame(flux_array, columns=column_index)
    col_name = csv_dataframe.columns.tolist()
    col_name.insert(col_name.index('C1'), 'Label')
    csv_dataframe = csv_dataframe.reindex(columns=col_name)

    csv_dataframe.to_csv(csv_path + '\\result.csv', mode='w', sep=',', index=False)
