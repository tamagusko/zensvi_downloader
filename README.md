
# Mapillary Image Downloader

This script downloads street-level images from Mapillary using a CSV coordinates file and saves them into an output folder.

It is built on top of the excellent [ZenSVI](https://github.com/koito19960406/ZenSVI) library.

## Requirements

- Python 3.10+
- [Mapillary API Key](https://www.mapillary.com/dashboard/developers)

## Installation

```bash
pip install zensvi python-dotenv
```

## Setup

1. Create a `.env` file in the project root with your Mapillary API key:

```
MLY_API_KEY=your_mapillary_api_key_here
```

2. Prepare your coordinates file in `data/coordinates.csv` with the following format:

```csv
lat,lon
53.349805,-6.260310
53.346400,-6.263200
53.352100,-6.256800
```

## Usage

Run the script:

```bash
python download_images_mapillary.py
```

- Output images will be saved in the `output/` folder.

## Credits

This project uses [ZenSVI](https://github.com/koito19960406/ZenSVI) to download mapillary images. Created by [Tamagusko](https://github.com/tamagusko).

## License

MIT License.
