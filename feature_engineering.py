import pandas as pd


def extract_features(df):
    df = df.drop(['timestamp', 'Unnamed: 458', 'Unnamed: 458'], axis=1)
    feature_df = pd.DataFrame()
    for column in df:
        data = df[column]
        i = 0
        mean = []
        var = []
        min_ = []
        max_ = []
        movement_range = []
        mean_str = '_'.join([column, 'mean'])
        var_str = '_'.join([column, 'var'])
        min_str = '_'.join([column, 'min'])
        max_str = '_'.join([column, 'max'])
        movement_range_str = '_'.join([column, 'movement_range'])

        while i < len(data):
            d = data[i:i+60]
            mean.append(d.mean())
            var.append(d.var())
            min_.append(d.min())
            max_.append(d.max())
            movement_range.append(d.max() - d.min())
            i += 60

        if not all(v == 0 for v in mean):
            current_df = pd.DataFrame({mean_str: mean, var_str: var, min_str: min_, max_str: max_, movement_range_str: movement_range})
            feature_df = pd.concat([feature_df, current_df], axis=1)
    return feature_df

if __name__ == '__main__':
    win = pd.read_csv('win_all.csv')
    lose = pd.read_csv('lose_all.csv')

    w = extract_features(win)
    w.to_csv('win_feature.csv')
    l = extract_features(lose)
    l.to_csv('lose_feature.csv')

    w['win/lose'] = 1
    l['win/lose'] = 0
    all_df = pd.DataFrame(pd.concat([w, l], ignore_index=True))

    all_df.to_csv('df_all.csv')
