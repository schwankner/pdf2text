# MMDA VILA pdf to text
Container image for converting PDFs to plain text.
The ml-models and packages are from https://github.com/allenai/vila.

## Container image
Mount one directory for the pdfs to convert to text and another one for the resulting textfiles.
You can also specify what types of text are included in the output via environment variable. The `TYPES` env accepts a comma separated string with no spaces! Valid values are `paragraph` (default), `title`, `abstract`, `caption`, `section`, `caption`, `figure`, `footer`, `list`, `table`, `reference` and `author`.
### Usage
You can mount a reports folder with pdfs and an output folder for the generated text files with the following command:

    docker run \
        --mount type=bind,source="$(pwd)"/reports,target=/usr/src/app/reports \
        --mount type=bind,source="$(pwd)"/output,target=/usr/src/app/output \
        --env TYPES=paragraph,title,abstract,list,table,section
        ghcr.io/schwankner/mmda-vila-pdf2text:latest

### Build
The container image is build automagic with GitHub actions and available as `docker/podman pull ghcr.io/schwankner/mmda-vila-pdf2text:latest`.
But you can also build your own image with:

    podman build . -t mmda-vila:latest