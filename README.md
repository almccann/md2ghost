Adapted from the [ever2simple](https://github.com/claytron/ever2simple) project.  Thank you @claytron.

Convert nested folders of markdown to [Ghost](https://github.com/TryGhost/Ghost) blog posts in json format according to import rules.

The conversion will ignore `.DS_Store` file and `.git` directory.

Assumes:
\- the title of the post is the first line in h1 followed by a space. E.g:
`# This is my title`
\- the author id is `1`

Usage:
`python -m /path/to/notes > /path/to/ghost.json`