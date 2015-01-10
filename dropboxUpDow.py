#! /usr/bin/env python
import os
import sys
import textwrap
import dropbox
from optparse import OptionParser


conf = {'APP_KEY': 'YOUR APP KEY',
        'APP_SECRET': 'YOUR APP SECRET',
        'ACCESS_TYPE': 'dropbox',
        'TOKEN': 'YOUR TOKEN',
        'DIR': '/home/',  # Default directory
        }


def doopts():
    program = os.path.basename(sys.argv[0])
    usg = """\
                usage: %s -h | [-u PATH/DIRECTORY] [-d DROPBOX/PATH/FILE]
          """
    usg = textwrap.dedent(usg) % program
    parser = OptionParser(usage=usg)

    parser.add_option('-p', '--upload', dest='upload',
                      metavar='UPLOAR', default=12345,
                      help='Upload your directory o file')

    parser.add_option('-d', '--download', dest='download',
                      metavar='DOWNLOAD', default=None,
                      help='Download your dropbox file')
    return parser


def map():
    parser = doopts()
    (options, args) = parser.parse_args()
    if options.upload:
        print "--upload argument is not defined"
        exit(0)
    if options.download:
        print "--download argument is not defined"
        exit(0)
    conf['UPLOAD'] = options.upload
    conf['DOWNLOAD'] = options.download


def _upload_local_dir(dire, dp_cli):
    for dirname, dirnames, filenames in os.walk(dire):
        for subdirname in dirnames:
            new_dire = str(os.path.join(dirname, subdirname)+"/")
            print new_dire
            _upload_local_dir(new_dire, dp_cli)

        for filename in filenames:
            print filename
            f = open(dirname+"/"+filename, 'rb')
            response = dp_cli.put_file(dirname+"/"+filename, f)
            print 'uploaded: ', response


def _download_remote_file(filename, dp_cli):
    f, metadata = dp_cli.get_file_and_metadata(filename)
    out = open('ejem_descargado.txt', 'wb')
    out.write(f.read())
    out.close()
    print metadata


def main():
    map()
    dp_sess = dropbox.session.DropboxSession(conf['APP_KEY'],
                                             conf['APP_SECRET'],
                                             conf['ACCESS_TYPE']
                                             )
    dp_cli = dropbox.client.DropboxClient(conf['TOKEN'])
    if 'UPLOAD' in conf.keys():
        _upload_local_dir(conf['UPLOAD'], dp_cli)
    if 'DOWNLOAD' in conf.keys():
        _download_remote_file(conf['DOWNLOAD'], dp_cli)

main()
