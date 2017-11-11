
import matplotlib.pyplot as plt
import numpy as np

def read_rtl_power_logfile_pwr(csv_file):
    import csv

    pwr = np.empty([0, 2])
    with open(csv_file, 'rb') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            pwr = np.vstack([pwr, [float(row[2]), float(row[6])]])

    return pwr

if __name__ == '__main__':
    gain = [0.0, 8.7, 19.7, 29.7, 40.2, 49.6]
    whip = [ None ] * 6
    discone = [ None ] * 6
    whip[0] = read_rtl_power_logfile_pwr(r'whip_25_1700_1M_g00.csv')
    whip[1] = read_rtl_power_logfile_pwr(r'whip_25_1700_1M_g10.csv')
    whip[2] = read_rtl_power_logfile_pwr(r'whip_25_1700_1M_g20.csv')
    whip[3] = read_rtl_power_logfile_pwr(r'whip_25_1700_1M_g30.csv')
    whip[4] = read_rtl_power_logfile_pwr(r'whip_25_1700_1M_g40.csv')
    whip[5] = read_rtl_power_logfile_pwr(r'whip_25_1700_1M_g50.csv')
    discone[0] = read_rtl_power_logfile_pwr(r'discone_25_1700_1M_g00.csv')
    discone[1] = read_rtl_power_logfile_pwr(r'discone_25_1700_1M_g10.csv')
    discone[2] = read_rtl_power_logfile_pwr(r'discone_25_1700_1M_g20.csv')
    discone[3] = read_rtl_power_logfile_pwr(r'discone_25_1700_1M_g30.csv')
    discone[4] = read_rtl_power_logfile_pwr(r'discone_25_1700_1M_g40.csv')
    discone[5] = read_rtl_power_logfile_pwr(r'discone_25_1700_1M_g50.csv')

    i = 2
    plt.figure(1)
    plt.title("RTL-SDR discone vs whip (gain: " + str(gain[i]) + "dB)")
    plt.plot(whip[i][:, 0], discone[i][:, 1], label="discone")
    plt.plot(discone[i][:, 0], whip[i][:, 1], label="whip")

    plt.ylabel('RX power (dB)')
    plt.xlabel('Frequency (MHz)')
    plt.legend(loc='upper right')
    plt.show()