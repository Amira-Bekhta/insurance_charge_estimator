import pandas as pd

def load(dataset: str, path: str, isRoot: bool) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        dataset (str): The name of the dataset (CSV file) to load.
        path (str): The subdirectory path where the dataset is stored.
        isRoot (bool): A boolean indicating if the root directory is used for the path.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the loaded data.
    
    The function reads the dataset from the 'data' directory if isRoot is True, 
    otherwise it reads from a relative path assuming the file is one level up.
    """
    if isRoot:
        return pd.read_csv(f"data/{path}/{dataset}.csv")
    return pd.read_csv(f"../data/{path}/{dataset}.csv")


def save(dataset: pd.DataFrame, name: str, isRoot: bool) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        dataset (pd.DataFrame): The pandas DataFrame to save.
        name (str): The name of the output CSV file.
        isRoot (bool): A boolean indicating if the root directory is used for the path.

    The function saves the dataset to the 'data/processed' directory if isRoot is True,
    otherwise it saves the file to the relative path assuming one level up.
    """
    if isRoot:
        dataset.to_csv(f"data/processed/{name}.csv", index=False)
    else:
        dataset.to_csv(f"../data/processed/{name}.csv", index=False)
