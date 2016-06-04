# md2ghost
Convert nested folders of markdown to [Ghost](https://github.com/TryGhost/Ghost) blog posts in json format according to import rules.  Adapted from the [ever2simple](https://github.com/claytron/ever2simple) project.

# Usage
`python -m /path/to/notes > /path/to/ghost.json`

Assumes:  
\- the title of the post is the first line in h1 followed by a space. E.g:
`# This is my title`  
\- the author id is `1`

The conversion will ignore `.DS_Store` files and `.git` directory.
