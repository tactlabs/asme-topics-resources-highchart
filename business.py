import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    #print(df['states'].tolist())

    Topics             = df['Topics'].tolist()

    Categories         = df['Categories'].tolist()

    list_of_tuples = [tuple(row) for row in df.values]
  
    print(list_of_tuples)

    result_dict = {
        'Topics '                : Topics ,
        'Categories'             : Categories,
        'data_list'             : list_of_tuples
    }

    #print(result_dict)

    return result_dict


def add_row(Topics, Categories):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Topics'            : Topics, 
        'Categories'        : Categories
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
     get_data()
