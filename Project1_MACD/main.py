import pandas as pd
import matplotlib.pyplot as plt


def readCsvFile():
    data = pd.read_csv("dis.csv")
    samples = data.Zamkniecie
    return samples


def calcEMA(samples, n, current):
    alpha = 2 / (n + 1)
    ema = 0
    denominator = 0
    for i in range(n + 1):
        if current - i >= 0:
            ema += ((1 - alpha) ** i) * samples[current - i]
            denominator += (1 - alpha) ** i
        else:
            break
    return ema / denominator


def formulaMACD():
    samples = readCsvFile()
    macd = []
    signal = []
    for current in range(1000):
        ema12 = calcEMA(samples, 12, current)
        ema26 = calcEMA(samples, 26, current)
        macd.append((ema12 - ema26))
        ema9 = calcEMA(macd, 9, current)
        signal.append(ema9)
    drawPlots(samples, macd, signal)


def showPlot():
    plt.title("Walt Disney Co")
    plt.xlabel("Samples 29.03.2019 - 17.03.2023")
    plt.ylabel("Close of the day on stocks")
    plt.show()


# all plot creating
def drawPlots(samples, macd, signal):
    # main data plot
    plt.figure().set_figwidth(15)
    plt.plot(samples, color='g', linewidth='0.8')
    showPlot()
    # macd and signal plot
    plt.figure().set_figwidth(15)
    plt.plot(macd, color='b', linewidth='0.8')
    plt.plot(signal, color='r', linewidth='0.8')
    showPlot()
    # all in one plot
    plt.figure().set_figwidth(15)
    plt.plot(samples, color='g', linewidth='0.8')
    plt.plot(macd, color='b', linewidth='0.8')
    plt.plot(signal, color='r', linewidth='0.8')
    showPlot()


# start
formulaMACD()