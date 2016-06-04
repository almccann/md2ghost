import logging
import json
import os
import sys
import time
import string


class MarkdownConverter(object):

    date_fmt = '%h %d %Y %H:%M:%S'

    def __init__(self, zip_filepath):
        self.zip_filepath = os.path.expanduser(zip_filepath)
        self.stdout = False

    def convert(self):
        if not os.path.exists(self.zip_filepath):
            print("File does not exist: %s" % self.zip_filepath)
            sys.exit(1)
        dict = {}
        db = []
        db_dict = {}
        meta_dict = {}
        meta_dict['exported_on'] = int(round(time.time() * 1000))
        meta_dict['version'] = '003'
        db_dict['meta'] = meta_dict
        data_dict = {}
        posts = []
        exclude_dirs = set(['.git'])
        exclude_files = set(['.DS_Store', 'README.md'])
        for root, dirs, files in os.walk(self.zip_filepath):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            files[:] = [f for f in files if f not in exclude_files]
            index = 1
            for file in files:
                with open(os.path.join(root, file), 'r') as f:
                    title = f.readline()[2:]
                    content = f.read()
                    date_created = os.path.getatime(f.name)
                    date_modified = os.path.getmtime(f.name)
                    prepared_data = self._prepare_note(index, content, title, date_created, date_modified)
                    posts.append(prepared_data)
                    index += 1
        data_dict['posts'] = posts
        db_dict['data'] = data_dict
        db.append(db_dict)
        dict['db'] = db
        self._convert_json(dict)

    def _prepare_note(self, index, content, title, date_created, date_modified):
        slug = title
        filter = "+:&.',"
        for char in filter:
            slug = slug.replace(char,"")
        note_dict = {}
        note_dict['id'] = index
        note_dict['title'] = title.rstrip('\n')
        note_dict['slug'] = "-".join(slug.rstrip('\n').lower().split())
        note_dict['markdown'] = content
        note_dict['image'] = None
        note_dict['featured'] = 0
        note_dict['page'] = 0
        note_dict['status'] = 'published'
        note_dict['language'] = 'en_US'
        note_dict['meta_title'] = title.rstrip('\n')
        note_dict['meta_description'] = title.rstrip('\n')
        note_dict['author_id'] = 1
        note_dict['created_at'] = time.strftime(self.date_fmt, time.localtime(date_created))
        # note_dict['created_at'] = date_created.strftime(self.date_fmt)
        note_dict['created_by'] = 1
        note_dict['updated_at'] = time.strftime(self.date_fmt, time.localtime(date_modified))
        # note_dict['updated_at'] = date_modified.strftime(self.date_fmt)
        note_dict['updated_by'] = 1
        note_dict['published_at'] = time.strftime(self.date_fmt, time.localtime(date_created))
        # note_dict['published_at'] = date_created.strftime(self.date_fmt)
        note_dict['published_by'] = 1
        note_dict['visibility'] = 'public'
        note_dict['mobiledoc'] = None
        return note_dict

    def _convert_json(self, notes):
        sys.stdout.write(json.dumps(notes))
