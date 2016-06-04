Adapted from the [ever2simple](https://github.com/claytron/ever2simple) project.

Convert nested folders of of markdown to [Ghost](https://github.com/TryGhost/Ghost) posts in json format according to inport rules.  The conversion will ignore `.DS_Store` file and `.git` directory.

Usage:
`python -m /path/to/notes > /path/to/ghost.json`

Assumes:
\- the title of the post is the first line in h1 followed by a space. E.g:
`# This is my title`
\- the author id is `1`