import os
from dotenv import load_dotenv
from zensvi.download import MLYDownloader


def download_images(input_csv, out_dir, api_key):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    downloader = MLYDownloader(mly_api_key=api_key)
    downloader.download_svi(
        dir_output=out_dir,
        input_csv_file=input_csv,
        buffer=10  # Avoid ValueError for point geometries
    )


def main():
    load_dotenv()
    api_key = os.getenv("MLY_API_KEY")
    if not api_key:
        raise ValueError("Mapillary API key not found in .env.")

    input_csv = os.path.join("data", "coordinates.csv")
    out_dir = "output"

    download_images(input_csv, out_dir, api_key)


if __name__ == "__main__":
    main()
