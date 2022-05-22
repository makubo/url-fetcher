# URL Fetcher script

This is the Take Home Test solution.

Please run all commands from the Build and Usage section inside the project root directory.

## Build

### Prepare development environment

This step is required for editing and/or running the fetcher script from the command line.

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create symlink to executable script

```bash
ln -s src/fetcher.py fetcher
```

### Create docker image

Run the command from project root to create docker image

```bash
docker build -t fetcher .
```

## Usage

### Script behavior explanation

Script save given url downloaded data to the `fetched_data/<host_name>/<path>/<file>` catalog.

- If url ended with `/` like `https://example.org/` script will save fetched html into `fetched_data/example.org/index.html`

- If url ended with file name or without `/` like `https://example.org/example/path/example-file.php` script will create exact the same path for downloaded file `fetched_data/example.org/example/path/example-file.php`

### Command line

To use script from cli, please prepare a development environment.

- Fetch site

```bash
fetcher https://www.google.com/ https://autify.com
```

> Script will create `fetched_data` directory inside the project root

- Show metadata

```bash
src/fetcher.py --metadata https://www.google.com/ https://autify.com
```

### Docker

To simplify access to fetcher executing results I recommend to bind local `fetched_data` directory to the container with option `--volume="$(pwd)/fetched_data:/opt/fetcher/fetched_data"` (docker will create the catalog inside project directory )

1. Run fetcher inside a container with default options.

> By default command looks like `fetcher https://www.google.com/ https://autify.com`

```bash
docker run --volume="$(pwd)/fetched_data:/opt/fetcher/fetched_data" fetcher:latest
```

Output:

```stdout
Fetching https://www.google.com/ ...
Save file /opt/fetcher/fetched_data/www.google.com/index.html ...
Fetching https://autify.com ...
Save file /opt/fetcher/fetched_data/autify.com/index.html ...
```

2. Run fetcher inside a container with custom options.

- Fetch site

```bash
docker run --volume="$(pwd)/fetched_data:/opt/fetcher/fetched_data" fetcher:latest fetcher https://www.google.com/
```

Output example:

```stdout
Fetching https://www.google.com/ ...
Save file /opt/fetcher/fetched_data/www.google.com/index.html ...com/index.html ...
```

- Show metadata

```bash
docker run --volume="$(pwd)/fetched_data:/opt/fetcher/fetched_data" fetcher:latest fetcher --metadata https://www.google.com/
```

Output example:

```stdout
Site: https://www.google.com/
 last_fetch: 2022-05-22 13:16:42.555850
 image_count: 1
 link_count: 17
 script_count: 8
```

## Extra

To achieve the extra I would use html parsing python library for example "Beautiful Soup".
