import pandas as pd

def main():
    df = pd.read_excel('List_temp_excel_2007.xlsx', index_col=0)
    # Fill nan to 'nan'
    df = df.fillna('nan')
    data_dict = df.to_dict('records')
    selected_people = select_record(data_dict)
    fill_template(selected_people)
    
def select_record(data_dict):
    selection = []
    for record in data_dict:
        if record['person_first_name'] != 'nan' and \
           record['person_last_name'] != 'nan' and \
           record['person_email_address'] != 'nan' and \
           record['company_name'] != 'nan':
            selection.append(record)
    return selection
    
def fill_template(data):
    for record in data:
        message = f"Hi {record['person_first_name'].strip()} {record['person_last_name'].strip()}. " \
        f"You email is {record['person_email_address'].strip()}. " \
        f"You work for {record['company_name'].strip()}."
        
        print(message + "\n\n")
            
if __name__ == '__main__':
    main()
