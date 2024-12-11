def load_dataset(file_path):
    """
    Loads the CSV dataset file.
    """
    import pandas as pd
    return pd.read_csv(file_path)
