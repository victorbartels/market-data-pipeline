import os
from pathlib import Path

from azure.storage.filedatalake import DataLakeServiceClient
from dotenv import load_dotenv


load_dotenv()


def upload_file_to_adls(local_file_path: str):

    account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
    account_key = os.getenv("AZURE_STORAGE_KEY")

    service_client = DataLakeServiceClient(
        account_url=f"https://{account_name}.dfs.core.windows.net",
        credential=account_key
    )

    file_system_client = service_client.get_file_system_client(
        file_system="landing"
    )

    local_path = Path(local_file_path)

    directory = (
        f"alpha_vantage/stock_daily/AAPL"
    )

    file_client = file_system_client.get_file_client(
        f"{directory}/{local_path.name}"
    )

    with open(local_path, "rb") as file:
        file_client.upload_data(file, overwrite=True)

    print(f"Upload realizado para ADLS: {local_path.name}")