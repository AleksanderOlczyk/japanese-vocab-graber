import pandas as pd


def read_cells_from_excel(file, sheet, start_row, column_list):
    df = None
    try:
        df = pd.read_excel(file, sheet_name=sheet, skiprows=start_row - 1)
        selected_columns = df[column_list]
        selected_columns = selected_columns.dropna()
        for column in column_list:
            selected_columns[column] = selected_columns[column].str.strip()
        return selected_columns
    except Exception as e:
        print("An error occurred while reading data from the Excel file:", e)
        if df is not None:
            print("Available columns in the sheet:", df.columns)
        return None


excel_file = 'Słówka　Genki.xlsx'
sheet_name = '8課'
start_row = 3
page = 8

column_list = ['pojutrze', 'あさって', 'Unnamed: 1']
cells = read_cells_from_excel(excel_file, sheet_name, start_row, column_list)

if cells is not None:
    print("Loaded cells from selected columns:")
    print(cells.to_string(index=False, justify='left'))
    output_file_name = f'Genki_{page}.txt'

    count = 0
    with open(output_file_name, 'w', encoding='utf-8') as f:
        f.write('#separator:tab\n')
        f.write('#html:true\n')
        f.write('#tags column:3\n')
        f.write(column_list[0] + '\t' + '<br>'.join(column_list[1:]) + '\n')
        for _, row in cells.iterrows():
            f.write(row.iloc[0] + '\t' + '<br>'.join(row.iloc[1:]) + '\n')
            count += 1

    print("Data has been saved to the file:", output_file_name)
    print("Total number of words:", count)
