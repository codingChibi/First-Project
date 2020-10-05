import pandas as pd
import csv
from prettytable import PrettyTable

#open csv
open_csv = open(r'C:\Users\maric\OneDrive\Desktop\work template.csv')

#as object
reader = csv.reader(open_csv)

#as list
i = next(reader)

#main header list
main_header_list = i[:2]

#categorizing columns
eq_a_list = i[:7]
eq_b_list = main_header_list + i[8:11]
eq_c_list = main_header_list + i[12:14]
eq_d_list = main_header_list + i[15:17]
act_a_list = main_header_list + i[18:21]

#categorize item
eq_a = i[3]
eq_b = i[8]
eq_c = i[12]
eq_d = i[15]
act_a = i[18]


#user input
#one branch or all branch
task = int(input("Please select:\n1-Show 1 branch Status\n2-Show All branch with the same status\n->  "))

#1 branch
if task == 1:
    #user input
    #branch code
    branch_code = int(input("Please enter branch code:\n->  "))

    #user input
    #one equipment or all equipment
    show_option = int(input(
        "Plese select item to show:\n1-Equipment A\n2-Equipment B\n3-Equipment C\n4-Equipment D\n5-Act A\n6-Show All\n->  "))


    if show_option == 1:
        use_cols = eq_a_list
    elif show_option == 2:
        use_cols = eq_b_list
    elif show_option == 3:
        use_cols = eq_c_list
    elif show_option == 4:
        use_cols = eq_d_list
    elif show_option == 5:
        use_cols = act_a_list
    elif show_option == 6:
        use_cols = i


    # finding branch code index
    def bc_index():

        for index, row in enumerate(reader):
            if row[0] == str(branch_code):
                return index


    branch_code_index = bc_index()

    #output display
    df = pd.read_csv(r'C:\Users\maric\OneDrive\Desktop\work template.csv', low_memory=False,
                     usecols=use_cols)
    print(df.iloc[branch_code_index])


#show all branch with the same status
if task == 2:
    #user input
    #select item
    selected_item = int(input("Plese select item to show:\n1-Equipment A\n2-Equipment B\n3-Equipment C\n4-Equipment D\n5-Act A\n->  "))

    #Equipment A
    if selected_item == 1:
        #user input
        #select item status

        show_item_status = int(input("Select Item A Status:\n1-refilled\n2-not refilled\n->  "))

        use_cols = eq_a_list
        item_column_name = eq_a

        if show_item_status == 1:
            item_status = "refilled"
        else:
            item_status = "not refilled"

    #Equipment B
    elif selected_item == 2:
        # user input
        # select item status

        show_item_status = int(input("Select Item B Status:\n1-Checked\n2-Not Checked\n->  "))

        use_cols = eq_b_list
        item_column_name = eq_b

        if show_item_status == 1:
            item_status = "Checked"
        else:
            item_status = "Not Checked"

    #Equipment C
    elif selected_item == 3:
        # user input
        # select item status

        show_item_status = int(input("Select Item C Status:\n1-Installed\n2-Not Installed\n->  "))

        use_cols = eq_c_list
        item_column_name = eq_c

        if show_item_status == 1:
            item_status = "Installed"
        else:
            item_status = "Not Installed"

    #Equipment D
    elif selected_item == 4:
        # user input
        # select item status

        show_item_status = int(input("Select Item D Status:\n1-Posted\n2-Not Posted\n->  "))

        use_cols = eq_d_list
        item_column_name = eq_d

        if show_item_status == 1:
            item_status = "Posted"
        else:
            item_status = "Not Posted"

    #Activity A
    elif selected_item == 5:
        # user input
        # select item status

        show_item_status = int(input("Select Item Status:\n1-Done\n2-Not Done\n->  "))

        use_cols = act_a_list
        item_column_name = act_a

        if show_item_status == 1:
            item_status = "Done"
        else:
            item_status = "Not Done"



    #data frame
    df = pd.read_csv(r'C:\Users\maric\OneDrive\Desktop\work template.csv', low_memory=False, usecols=use_cols)
    dataframe_display = df.loc[df[item_column_name] == item_status]

    #Prettytable
    #collect columns from dataframe as list
    columns_in_list = list(dataframe_display.columns)

    #collect rows from dataframe as list
    rows_in_list = [list(row) for (itx, row) in dataframe_display.iterrows()]

    table = PrettyTable()

    #table columns
    table.field_names = columns_in_list

    #table rows
    for row in rows_in_list:
        table.add_row(row)

    print(table)








