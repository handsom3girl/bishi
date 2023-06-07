import csv

def split_csv_file(filename, batch_size):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(str(row[0]))

    batches = [data[i:i+batch_size] for i in range(0, len(data), batch_size)]
    print(len(batches))
    for batch in batches:
        print(batch)
        print(len(batch))
        print('\n')

# 指定您的 CSV 文件路径和批次大小
filename = 'fyx_chinamoney.csv'
batch_size = 80

# 调用函数进行拆分和打印输出
split_csv_file(filename, batch_size)