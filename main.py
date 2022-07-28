import numpy as np
import pandas as pd
from tqdm import tqdm

if __name__ == '__main__':

    class UserInfo():
        def __init__(self, id, field, fieldcount):
            self.id = id
            self.field = field
            self.fieldcount = fieldcount

    excel1 = pd.read_excel('C:\\Users\\kevin\\Downloads\\excel_entreg\\libro2.1.xlsx', sheet_name='Hoja2')

    newdt = pd.DataFrame(columns=['id', 'phone'])

    for i in tqdm(excel1.iterrows(), total=excel1.shape[0]):
        #write a nue column in the new excel for each row
        newdt.loc[len(newdt)] = [i[1][1], i[1][3]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][4]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][5]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][6]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][7]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][8]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][9]]
        newdt.loc[len(newdt)] = [i[1][1], i[1][10]]

        # save the new dataframe to a csv file
    try:
        print("Saving the new csv file...")
        chunks = np.array_split(newdt.index, 100)  # chunks of 100 rows

        for chunck, subset in enumerate(tqdm(chunks)):
            if chunck == 0:  # first row
                newdt.loc[subset].to_csv('data.csv', mode='w', index=False, encoding="latin1")
            else:
                newdt.loc[subset].to_csv('data.csv', header=None, mode='a', index=False, encoding="latin1")

        print('Done!')
    except PermissionError:
        print('Error: The file is open, please close it and try again')


