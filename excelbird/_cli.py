import webbrowser
import click
import os
import shutil
from subprocess import call

shutil

@click.group()
def main():
    pass

@click.command()
@click.argument('action', required=False)
def docs(action=None):
    here = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(here, os.pardir, 'docs')

    if action is None:
        docs_index = os.path.join(path, 'build', 'html', 'index.html')
        webbrowser.open_new_tab('file://' + docs_index)

    elif action == "build":
        shutil.rmtree(os.path.join(path, 'build'))
        base_path = os.path.join(path, os.pardir, os.pardir)
        os.system(f"cd {base_path}; source env/bin/activate; cd excelbird/docs; make html")




# @click.command()
# @click.argument('base')
# @click.argument('action')
# def temp(base, action=None):
#     if base == "docs":
#         here = os.path.abspath(os.path.dirname(__file__))
#         docs_html = os.path.join(here, os.pardir, 'docs', 'build', 'html')
#         index_html = os.path.join(docs_html, 'index.html')
#         webbrowser.open_new_tab('file://' + index_html)


main.add_command(docs)

if __name__ == "__main__":
    main()
