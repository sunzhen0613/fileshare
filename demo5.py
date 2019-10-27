import matplotlib.pyplot as plt
# import numpy as np

items = [
    u"fps", u"qsv", u"vmf", u"pnsr", 'aaa', 'bbbb', 'ccc', 'ddd', u"fps",
    u"qsv", u"vmf", u"pnsr", 'aaa', 'bbbb', 'ccc', 'ddd', u"fps", u"qsv",
    u"vmf", u"pnsr", 'aaa', 'bbbb', 'ccc', 'ddd', u"fps", u"qsv", u"vmf",
    u"pnsr", 'aaa', 'bbbb', 'ccc', 'ddd'
]

data1 = {
    'tar': [
        2357, 156, 2045, 168, 2358, 399, 2358, 362, 2358, 399, 2358, 362, 5746,
        312, 4497, 319, 2358, 399, 2358, 362, 5746, 312, 4497, 319, 5746, 312,
        4497, 319, 2357, 156, 2045, 168
    ],
    'rel': [
        2358, 399, 2358, 362, 5746, 312, 4497, 319, 5746, 312, 4497, 319, 2357,
        156, 2045, 168, 5746, 312, 4497, 319, 2357, 156, 2045, 168, 2357, 156,
        2045, 168, 2358, 399, 2358, 362
    ],
    'oth': [
        5746, 312, 4497, 319, 2357, 156, 2045, 168, 2357, 156, 2045, 168, 2358,
        399, 2358, 362, 2357, 156, 2045, 168, 2358, 399, 2358, 362, 2358, 399,
        2358, 362, 5746, 312, 4497, 319
    ]
}


def showbar2(items, data):
    bar_width = 0.2
    fir = list(range(len(items)))

    plt.figure(figsize=(16, 8))
    ax = plt.subplot(1, 1, 1)
    ax.set_title("Counter")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    one_bar = plt.bar(
        range(len(items)),
        list(data.values())[0],
        width=bar_width,
        label=list(data.keys())[0])
    all_bar = one_bar
    for n in range(len(data) - 1):
        n += 1
        oth = [i + bar_width * n for i in fir]
        oth_bar = plt.bar(
            oth,
            list(data.values())[n],
            width=bar_width,
            label=list(data.keys())[n])
        all_bar = all_bar + oth_bar

    plt.legend()
    x = [i + bar_width * (len(data) // 2) for i in fir]
    plt.xticks(x, items, rotation=60)

    for b in all_bar:
        h = b.get_height()
        plt.text(b.get_x() + b.get_width() / 2, h, '%d' % h)

    plt.show()


def showbar1(items, b_14, b_15):
    bar_width = 0.3
    x_14 = list(range(len(items)))
    x_15 = [i + bar_width for i in x_14]
    # x_16 = [i + bar_width * 2 for i in x_14]

    plt.figure(figsize=(16, 8))
    ax = plt.subplot(1, 1, 1)
    ax.set_title("Counter")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    plt.bar(range(len(items)), b_14, width=bar_width, label=u"9/14")
    plt.bar(x_15, b_15, width=bar_width, label=u"9/15")
    # plt.bar(x_16, b_16, width=bar_width, label=u"9/16")

    plt.legend()
    plt.xticks(x_15, items, rotation=60)

    plt.show()


showbar2(items, data1)
