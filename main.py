import pandas as pd
import numpy as np

match1_body1 = pd.read_csv('./wii/5/test1_body2.csv')
match1_body2 = pd.read_csv('./wii/5/test1_body1.csv')

match_timepoint = pd.read_csv('./wii/match5.txt',delim_whitespace=True)
match_timepoint['timepoint_in_sec'] = match_timepoint['timepoint'].apply(lambda x: int(x.split('.')[0]) + 0.01*float(x.split('.')[1]) if len(x) < 6\
                                                                           else int(x[0])*60 + int(x[2:4]) + 0.01*float(x[5:7]))

print match_timepoint
# print match_timepoint.r1winner[1]
# print match_body1['timestamp'].head(500)

win = pd.DataFrame([])
lose = pd.DataFrame([])
for i, t in match_timepoint.timepoint_in_sec.iteritems():
    close_t = min(match1_body1['timestamp'],key=lambda x:abs(x-t))
    start_index = int(np.rint(close_t/0.03333 + 2))
    if int(match_timepoint.r5winner[i]) == 1:
        # print match1_body1.iloc[start_index:start_index+60]
        win = win.append(match1_body1.iloc[start_index:start_index+60], ignore_index=True)
        lose = lose.append(match1_body2.iloc[start_index:start_index+60], ignore_index=True)
    else:
        # print match1_body1.iloc[start_index:start_index+60]
        win = win.append(match1_body2.iloc[start_index:start_index+60], ignore_index=True)
        lose = lose.append(match1_body1.iloc[start_index:start_index+60], ignore_index=True)


win.to_csv('win.csv')
lose.to_csv('lose.csv')