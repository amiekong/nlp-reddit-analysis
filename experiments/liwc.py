class liwc_sum:
    def count_liwc_values(self, df):
        col_liwc = ['affect', 'social', 'cogproc', 'percept', 'bio', 'drives', 'time', 'relativ', 'informal']

    #dictionary stores sum of liwc value counts
        valueCount = {}

        total = 0
        for item in col_liwc:
            try:
                valueCount[item].add(df[item].values.sum())
                for i in valueCount[item]:
                    total += float(i)
            except:
                valueCount[item] = [df[item].values.sum()]
                for i in valueCount[item]:
                    total += float(i)

        for item in valueCount:
            for val in valueCount[item]:
                norm = float(val)/total
                valueCount[item] = norm

        print(valueCount)
