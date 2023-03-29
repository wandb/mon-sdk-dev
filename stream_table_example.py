import stream_table
import time

table = stream_table.AppendTable('test-table24', ['a', 'b'])

for i in range(50):
    print('ADDING I', i)
    table.add_data(i, i * 2)
    time.sleep(1)
table.join()