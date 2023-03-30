# New APIs for monitoring

## StreamTable

An API for streaming tabular data to W&B. Same API as wandb.Table but records are automatically persisted and made available in the UI as they are written.

Example usage:

```
import mon_sdk_dev

table = mon_sdk_dev.StreamTable("test-table24", ["a", "b"])

for i in range(50):
    print("ADDING I", i)
    table.add_data(i, i * 2)
    time.sleep(1)

# For now, you should call this when you are done writing data to the table,
# to ensure all written data is committed and stop the write thread.
table.join()
```
