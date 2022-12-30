def Josephus(n, k):

    finalResult = []
    beginIndexes = []
    mainList = []

    for i in range(1, n + 1):

        mainList.append(i)

    begin = k - 1

    i = 0

    while len(mainList) > 1:

        if i == 0:

            first = []

            for i in range(1, n + 1):

                first.append(i)

            finalResult.append(first)

        secondList = []

        beginIndexes.append(begin)

        begin = generatorBegin(begin, k, mainList)

        del mainList[beginIndexes[-1]:: k]

        for i in mainList:

            secondList.append(i)

        finalResult.append(secondList)

        i += 1

    print(finalResult)

    return mainList[0]


def generatorBegin(start, k, mainList):

    secondList = []

    for i in mainList:

        secondList.append(i)

    mainLength = len(mainList)

    del secondList[start::k]

    numberOfDelete = mainLength - len(secondList) - 1

    step = k - (mainLength - 1 - (start + k * numberOfDelete)) - 1

    return step