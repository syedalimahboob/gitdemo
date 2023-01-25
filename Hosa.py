import json
import logging

import pandas as pd
from pathlib import Path

source_path = "D:/DATA/csv/complex/2021-Hosa-Dealer-Price-List.csv"
destination_path = "D:/CLEANED DATA/Cleaned_CSV/SHosatest.csv"

df = pd.read_csv(source_path, delimiter=',', names=list(range(12)))
df.dropna(thresh=4, inplace=True)
df.dropna(axis=1, how='all', inplace=True)

# creating Dataframe
df1 = pd.DataFrame(df, index=range(70, 82))
df1.dropna(thresh=2, inplace=True)
df1.dropna(axis=1, how='all', inplace=True)
headers = ['Description', 'Model', 'Option', 'Dealer', 'SMP', 'SRP']
df1.columns = headers
df1 = df1[df1["SMP"].str.match('[^a-zA-Z]')]

df2 = pd.DataFrame(df, index=range(83, 118))
df2.dropna(thresh=4, inplace=True)
df2.dropna(axis=1, how='all', inplace=True)
headers1 = ['Model', 'Option', 'Dealer', 'SMP', 'SRP']
df2.columns = headers1

df3 = pd.DataFrame(df, index=range(118, 121))
df3.dropna(thresh=2, inplace=True)
df3.dropna(axis=1, how='all', inplace=True)
df3.columns = headers
df3 = df3[df3["SRP"].str.match('[^a-zA-Z]')]

df4 = pd.DataFrame(df, index=range(121, 137))
df4.dropna(thresh=2, inplace=True)
df4.dropna(axis=1, how='all', inplace=True)
df4.columns = headers1

df5 = pd.DataFrame(df, index=range(137, 144))
df5.dropna(thresh=2, inplace=True)
df5.dropna(axis=1, how='all', inplace=True)
df5.columns = headers

df6 = pd.DataFrame(df, index=range(144, 177))
df6.dropna(thresh=2, inplace=True)
df6.dropna(axis=1, how='all', inplace=True)
df6.columns = headers1

df7 = pd.DataFrame(df, index=range(177, 186))
df7.dropna(thresh=2, inplace=True)
df7.dropna(axis=1, how='all', inplace=True)
df7.columns = headers
df7 = df7[df7["SMP"].str.match('[^a-zA-Z]')]

df8 = pd.DataFrame(df, index=range(189, 324))
df8.dropna(thresh=2, inplace=True)
df8.dropna(axis=1, how='all', inplace=True)
df8.columns = headers
df8 = df8[df8["Dealer"].str.match('[^a-zA-Z]')]

df9 = pd.DataFrame(df, index=range(324, 355))
df9.dropna(thresh=2, inplace=True)
df9.dropna(axis=1, how='all', inplace=True)
df9.columns = headers1

df10 = pd.DataFrame(df, index=range(355, 458))
df10.dropna(thresh=2, inplace=True)
df10.dropna(axis=1, how='all', inplace=True)
df10.columns = headers
df10 = df10[df10["Dealer"].str.match('[^a-zA-Z]')]

df11 = pd.DataFrame(df, index=range(186, 189))
df11.dropna(thresh=2, inplace=True)
df11.dropna(axis=1, how='all', inplace=True)
df11.columns = headers1

df12 = pd.DataFrame(df, index=range(458, 461))
df12.dropna(thresh=2, inplace=True)
df12.dropna(axis=1, how='all', inplace=True)
df12.columns = headers1

df13 = pd.DataFrame(df, index=range(461, 551))
df13.dropna(thresh=2, inplace=True)
df13.dropna(axis=1, how='all', inplace=True)
df13.columns = headers
df13 = df13[df13["Dealer"].str.match('[^a-zA-Z]')]

df14 = pd.DataFrame(df, index=range(551, 563))
df14.dropna(thresh=2, inplace=True)
df14.dropna(axis=1, how='all', inplace=True)
df14.columns = headers1

df15 = pd.DataFrame(df, index=range(563, 568))
df15.dropna(thresh=2, inplace=True)
df15.dropna(axis=1, how='all', inplace=True)
df15.columns = headers
df15 = df15[df15["Dealer"].str.match('[^a-zA-Z]')]

df16 = pd.DataFrame(df, index=range(568, 580))
df16.dropna(thresh=2, inplace=True)
df16.dropna(axis=1, how='all', inplace=True)
df16.columns = headers1

df17 = pd.DataFrame(df, index=[584, 583])
df17.dropna(thresh=2, inplace=True)
df17.dropna(axis=1, how='all', inplace=True)
df17.columns = headers1

df18 = pd.DataFrame(df, index=range(580, 616))
df18.dropna(thresh=2, inplace=True)
df18.dropna(axis=1, how='all', inplace=True)
df18 = df18.drop([584, 583])
df18.columns = headers
df18 = df18[df18["Dealer"].str.match('[^a-zA-Z]')]

df19 = pd.DataFrame(df, index=range(616, 627))
df19.dropna(thresh=2, inplace=True)
df19.dropna(axis=1, how='all', inplace=True)
df19.columns = headers
df19 = df19[df19["SMP"].str.match('[^a-zA-Z]')]

df20 = pd.DataFrame(df, index=range(627, 666))
df20.dropna(thresh=2, inplace=True)
df20.dropna(axis=1, how='all', inplace=True)
df20 = df20.drop([641, 642, 643])
df20.columns = headers1

df21 = pd.DataFrame(df, index=[641, 642, 643])
df21.dropna(thresh=2, inplace=True)
df21.dropna(axis=1, how='all', inplace=True)
df21[[3, 4]] = df21[3].str.split(' ', n=1, expand=True)
df21.columns = headers1

df22 = pd.DataFrame(df, index=range(667, 689))
df22.dropna(thresh=2, inplace=True)
df22.dropna(axis=1, how='all', inplace=True)
df22.columns = headers
df22 = df22[df22["Dealer"].str.match('[^a-zA-Z]')]

df23 = pd.DataFrame(df, index=range(690, 695))
df23.dropna(thresh=2, inplace=True)
df23.dropna(axis=1, how='all', inplace=True)
df23.columns = headers1

df24 = pd.DataFrame(df, index=range(695, 708))
df24.dropna(thresh=2, inplace=True)
df24.dropna(axis=1, how='all', inplace=True)
df24.columns = headers
df24 = df24[df24["Dealer"].str.match('[^a-zA-Z]')]

df25 = pd.DataFrame(df, index=range(711, 713))
df25.dropna(axis=1, how='all', inplace=True)
df25.dropna(thresh=2, inplace=True)
df25.columns = headers1

df26 = pd.DataFrame(df, index=range(714, 719))
df26.dropna(axis=1, how='all', inplace=True)
df26.dropna(thresh=2, inplace=True)
df26.columns = headers
df26 = df26[df26["SMP"].str.match('[^a-zA-Z]')]

df27 = pd.DataFrame(df, index=range(719, 725))
df27.dropna(axis=1, how='all', inplace=True)
df27.dropna(thresh=2, inplace=True)
df27.columns = headers1
df27 = df27[df27["SMP"].str.match('[^a-zA-Z]')]

df28 = pd.DataFrame(df, index=range(726, 731))
df28.dropna(axis=1, how='all', inplace=True)
df28.columns = headers
df28 = df28[df28["SMP"].str.match('[^a-zA-Z]')]

df29 = pd.DataFrame(df, index=range(731, 744))
df29.dropna(axis=1, how='all', inplace=True)
df29.dropna(thresh=2, inplace=True)
df29.columns = headers1

df30 = pd.DataFrame(df, index=range(745, 751))
df30.dropna(axis=1, how='all', inplace=True)
df30.columns = headers
df30 = df30[df30["SMP"].str.match('[^a-zA-Z]')]

df31 = pd.DataFrame(df, index=range(751, 753))
df31.dropna(axis=1, how='all', inplace=True)
df31.columns = headers1

df32 = pd.DataFrame(df, index=range(753, 783))
df32.dropna(axis=1, how='all', inplace=True)
df32.dropna(thresh=2, inplace=True)
df32.columns = headers
df32 = df32.drop([753, 770])

df33 = pd.DataFrame(df, index=range(783, 788))
df33.dropna(axis=1, how='all', inplace=True)
df33.dropna(thresh=2, inplace=True)
df33.columns = headers1

df34 = pd.DataFrame(df, index=range(789, 857))
df34.dropna(axis=1, how='all', inplace=True)
df34.dropna(thresh=2, inplace=True)
df34.columns = headers
df34["SRP"] = df34["SRP"].fillna('-')
df34 = df34[df34["SRP"].str.match('[^a-zA-Z]')]
df34["SRP"] = df34["SRP"].replace("-", "", regex=True)

df35 = pd.DataFrame(df, index=range(858, 871))
df35.dropna(axis=1, how='all', inplace=True)
df35.dropna(thresh=2, inplace=True)
df35[[0, 2]] = df35[2].str.split(' ', n=1, expand=True)
df35 = df35[[1, 0, 2, 3, 4]]
df35.columns = headers1

df36 = pd.DataFrame(df, index=range(872, 887))
df36.dropna(axis=1, how='all', inplace=True)
df36.dropna(thresh=2, inplace=True)
df36.columns = headers
df36["SRP"] = df36["SRP"].fillna('-')
df36 = df36[df36["SRP"].str.match('[^a-zA-Z]')]
df36["SRP"] = df36["SRP"].replace("-", "", regex=True)

df37 = pd.DataFrame(df, index=range(887, 900))
df37.dropna(axis=1, how='all', inplace=True)
df37.dropna(thresh=2, inplace=True)
df37.columns = headers1

df38 = pd.DataFrame(df, index=range(900, 906))
df38.dropna(axis=1, how='all', inplace=True)
df38.dropna(thresh=2, inplace=True)
df38.columns = headers
df38["SRP"] = df38["SRP"].fillna('-')
df38 = df38[df38["SRP"].str.match('[^a-zA-Z]')]
df38["SRP"] = df38["SRP"].replace("-", "", regex=True)

df39 = pd.DataFrame(df, index=range(906, 922))
df39.dropna(axis=1, how='all', inplace=True)
df39.dropna(thresh=2, inplace=True)
df39.columns = headers1

df40 = pd.DataFrame(df, index=range(922, 952))
df40.dropna(axis=1, how='all', inplace=True)
df40.dropna(thresh=2, inplace=True)
headers2 = ['Description', 'Model', 'Option', 'Dealer per Foot', 'Spool', 'SRP per Foot']
df40.columns = headers2
df40["SRP per Foot"] = df40["SRP per Foot"].fillna('-')
df40 = df40[df40["SRP per Foot"].str.match('[^a-zA-Z]')]
df40["SRP per Foot"] = df40["SRP per Foot"].replace("-", "", regex=True)

df41 = pd.DataFrame(df, index=range(953, 955))
df41[[10, 2]] = df41[2].str.split(' ', n=1, expand=True)
df41 = df41[[0, 1, 10, 2, 3, 4]]
df41.columns = headers

df42 = pd.DataFrame(df, index=[955, 956, 959, 960, 961, 962])
df42.dropna(axis=1, how='all', inplace=True)
df42.dropna(thresh=2, inplace=True)
df42.columns = headers

df43 = pd.DataFrame(df, index=[958])
df43.dropna(axis=1, how='all', inplace=True)
df43.dropna(thresh=2, inplace=True)
df43[[2, 3, 6]] = df43[3].str.split(' ', n=2, expand=True)
df43[2] = df43[2] + df43[3]
df43 = df43.drop([3], axis=1)
df43 = df43[[0, 1, 2, 6, 4, 5]]
df43.columns = headers

df44 = pd.DataFrame(df, index=range(963, 984))
df44.dropna(axis=1, how='all', inplace=True)
df44.dropna(thresh=2, inplace=True)
df44.drop([963, 980], inplace=True)
df44.columns = headers

df45 = pd.DataFrame(df, index=range(984, 996))
df45.dropna(axis=1, how='all', inplace=True)
df45.dropna(thresh=2, inplace=True)
df45.columns = headers1

df46 = pd.DataFrame(df, index=range(997, 998))
df46.dropna(axis=1, how='all', inplace=True)
df46[[2, 3, 6, 7]] = df46[3].str.split(' ', n=3, expand=True)
df46[2] = df46[2] + df46[2] + df46[6]
df46 = df46.drop([3, 6], axis=1)
df46 = df46[[0, 1, 2, 7, 4, 5]]
df46.columns = headers

df47 = pd.DataFrame(df, index=range(998, 1006))
df47.dropna(axis=1, how='all', inplace=True)
df47.columns = headers1

df48 = pd.DataFrame(df, index=range(1007, 1009))
df48.dropna(axis=1, how='all', inplace=True)
df48.columns = headers

df49 = pd.DataFrame(df, index=range(1009, 1019))
df49.dropna(axis=1, how='all', inplace=True)
df49.columns = headers1

df50 = pd.DataFrame(df, index=range(1021, 1027))
df50.dropna(axis=1, how='all', inplace=True)
df50.columns = headers1

df51 = pd.DataFrame(df, index=range(1027, 1037))
df51.dropna(axis=1, how='all', inplace=True)
df51.columns = headers1

df52 = pd.DataFrame(df, index=range(1039, 1040))
df52.dropna(axis=1, how='all', inplace=True)
df52[[0, 2]] = df52[2].str.split(' ', n=1, expand=True)
df52 = df52[[1, 0, 2, 3, 4]]
df52.columns = headers1

df53 = pd.DataFrame(df, index=range(1042, 1048))
df53.dropna(axis=1, how='all', inplace=True)
df53.columns = headers1

df54 = pd.DataFrame(df, index=range(1048, 1054))
df54.dropna(axis=1, how='all', inplace=True)
df54.columns = headers1

df55 = pd.DataFrame(df, index=range(1056, 1063))
df55.dropna(axis=1, how='all', inplace=True)
df55.columns = headers1

df56 = pd.DataFrame(df, index=range(1063, 1070))
df56.dropna(axis=1, how='all', inplace=True)
df56.columns = headers1

df57 = pd.DataFrame(df, index=range(1071, 1076))
df57.dropna(axis=1, how='all', inplace=True)
df57.columns = headers

df58 = pd.DataFrame(df, index=range(1076, 1079))
df58.dropna(axis=1, how='all', inplace=True)
df58.columns = headers1

df59 = pd.DataFrame(df, index=range(1079, 1094))
df59.dropna(axis=1, how='all', inplace=True)
df59.dropna(thresh=2, inplace=True)
df59.columns = headers
df59["SRP"] = df59["SRP"].fillna('-')
df59 = df59[df59["SRP"].str.match('[^a-zA-Z]')]
df59["SRP"] = df59["SRP"].replace("-", "", regex=True)

df60 = pd.DataFrame(df, index=range(1094, 1103))
df60.dropna(axis=1, how='all', inplace=True)
df60.dropna(thresh=2, inplace=True)
df60.columns = headers1

df61 = pd.DataFrame(df, index=range(1104, 1111))
df61.dropna(axis=1, how='all', inplace=True)
df61[[2, 3, 6, 7]] = df61[3].str.split(' ', n=3, expand=True)
df61[2] = df61[2] + df61[3] + df61[6]
d61 = df61.drop([3, 6], axis=1)
df61 = df61[[0, 1, 2, 7, 4, 5]]
df61.columns = headers

df62 = pd.DataFrame(df, index=range(1112, 1119))
df62.dropna(axis=1, how='all', inplace=True)
df62.columns = headers

df63 = pd.DataFrame(df, index=range(1130, 1141))
df63.dropna(axis=1, how='all', inplace=True)
df63.columns = headers1

df64 = pd.DataFrame(df, index=range(1142, 1154))
df64.dropna(axis=1, how='all', inplace=True)
df64.dropna(thresh=2, inplace=True)
df64.columns = headers

df65 = pd.DataFrame(df, index=range(1154, 1162))
df65.dropna(axis=1, how='all', inplace=True)
df65.columns = headers1

df66 = pd.DataFrame(df, index=range(1163, 1169))
df66.dropna(axis=1, how='all', inplace=True)
df66.columns = headers

df67 = pd.DataFrame(df, index=range(1169, 1201))
df67.dropna(axis=1, how='all', inplace=True)
df67.columns = headers1

df68 = pd.DataFrame(df, index=range(1202, 1210))
df68.dropna(axis=1, how='all', inplace=True)
df68.dropna(thresh=2, inplace=True)
df68 = df68.drop(1205)
df68.columns = headers

df69 = pd.DataFrame(df, index=range(1210, 1227))
df69.dropna(axis=1, how='all', inplace=True)
df69.columns = headers1

df70 = pd.DataFrame(df, index=range(1228, 1241))
df70.dropna(axis=1, how='all', inplace=True)
df70 = df70.drop(1232)
df70.columns = headers

df71 = pd.DataFrame(df, index=range(1242, 1245))
df71.dropna(axis=1, how='all', inplace=True)
df71.columns = headers

df72 = pd.DataFrame(df, index=range(1245, 1250))
df72.dropna(axis=1, how='all', inplace=True)
df72.dropna(thresh=2, inplace=True)
headers3 = ['Description', 'Model', 'Case Qty', 'SMP', 'SRP']
df72.columns = headers3
df72 = df72[df72["SMP"].str.match('[^a-zA-Z]')]

df73 = pd.DataFrame(df, index=range(1251, 1253))
df73.dropna(axis=1, how='all', inplace=True)
df73.columns = headers

df74 = pd.DataFrame(df, index=[1253])
df74.dropna(axis=1, how='all', inplace=True)
df74.dropna(thresh=2, inplace=True)
df74.columns = headers1

df75 = pd.DataFrame(df, index=[1254])
df75.dropna(axis=1, how='all', inplace=True)
df75.dropna(thresh=2, inplace=True)
df75[[1, 2, 6, 7]] = df75[2].str.split(' ', n=4, expand=True)
df75[1] = df75[1] + df75[2]
df75 = df75.drop([2, 7], axis=1)
df75 = df75[[0, 1, 6, 3, 4]]
df75.columns = headers1

df76 = pd.DataFrame(df, index=range(1254, 1270))
df76.dropna(axis=1, how='all', inplace=True)
df76.dropna(thresh=2, inplace=True)
df76.columns = headers1
df76 = df76[df76["SRP"].str.match('[^a-zA-Z]')]

df77 = pd.DataFrame(df, index=range(1271, 1285))
df77.dropna(axis=1, how='all', inplace=True)
df77.dropna(thresh=2, inplace=True)
headers4 = ['Model', 'Option', 'Dealer', 'Case Qty', 'SMP', 'SRP']
df77.columns = headers4
df77 = pd.DataFrame(df, index=range(1285, 1289))
df77.dropna(axis=1, how='all', inplace=True)
df77.columns = headers1

df78 = pd.DataFrame(df, index=range(1290, 1295))
df78.dropna(axis=1, how='all', inplace=True)
df78.columns = headers

df79 = pd.DataFrame(df, index=range(1295, 1299))
df79.dropna(axis=1, how='all', inplace=True)
df79.dropna(axis=1, how='all', inplace=True)
df79[[5, 2, 6]] = df79[2].str.split(' ', n=2, expand=True)
df79[1] = df79[1] + df79[2] + +df79[5]
df79.drop([2, 5], inplace=True, axis=1)
df79 = df79[[0, 1, 6, 3, 4]]

df80 = pd.DataFrame(df, index=range(1299, 1301))
df80.dropna(axis=1, how='all', inplace=True)
df80.columns = headers1

df81 = pd.DataFrame(df, index=range(1302, 1308))
df81.dropna(axis=1, how='all', inplace=True)
df81.columns = headers

df82 = pd.DataFrame(df, index=range(1308, 1326))
df82.dropna(axis=1, how='all', inplace=True)
df82.columns = headers1

df83 = pd.DataFrame(df, index=range(1328, 1390))
df83.dropna(thresh=2, inplace=True)
df83.dropna(axis=1, how='all', inplace=True)
headers5 = ['Pos', 'Model', 'Description', 'Qty', 'Dealer Each', 'Dealer Subtotal', 'Promo -10%',
            'Promo Subtotal', 'MSRP Each', 'MSRP Subtotal']
df83.columns = headers5

df84 = pd.DataFrame(df, index=range(1392, 1442))
df84.dropna(thresh=2, inplace=True)
df84.dropna(axis=1, how='all', inplace=True)
df84.columns = headers5

frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df80, df11, df12, df13, df14, df15, df16, df17,
          df18, df19, df20, df21, df22, df23, df24, df25, df26, df27, df28, df29, df30, df31, df32, df33, df34,
          df35, df36, df37, df38, df39, df40, df41, df42, df43, df44, df45, df46, df47, df48, df49, df50, df51,
          df52, df53, df54, df55, df56, df57, df58, df59, df60, df61, df62, df63, df64, df65, df66, df67, df68,
          df69, df70, df71, df73, df74, df75, df76, df77, df78, df79, df80, df81, df82, df83, df84]

df = pd.concat(frames, axis=0)

df.to_csv(destination_path, header=True, sep=',', index=False)

response = {'message': "Cleaned Xls", 'status': "success", 'filePath': destination_path}
# print(df)
print(json.dumps(response))
