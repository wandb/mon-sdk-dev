# New APIs for monitoring

## StreamTable

An API for streaming tabular data to W&B. Same API as wandb.Table but records are automatically persisted and made available in the UI as they are written.

See stream_table_example.py for example usage.

Caveat: you must call StreamTable.join() to exit cleanly for now.
