import io

from flask import render_template, request, Blueprint
from flask_menu import register_menu

from application.utils.files import get_static_json, get_static_file


project_blueprint = Blueprint(
    'Project',
    __name__,
    url_prefix='/projects',
    template_folder='templates',
    static_folder='static'
)


@project_blueprint.route('/')
def projects():
    data = get_static_json("static/projects/projects.json")['projects']
    data.sort(key=order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower() for project_tag in project['tags']]]

    return render_template('projects.html', projects=data, tag=tag)


def order_projects_by_weight(projects: dict) -> int:
    try:
        return int(projects['weight'])
    except KeyError:
        return 0


@project_blueprint.route('/<title>')
def project(title):

    projects = get_static_json("static/projects/projects.json")['projects']
    in_project = next((p for p in projects if p['link'] == title), None)

    # if project's title doesn't exists
    if in_project is None:
        return render_template('404.html'), 404

    selected = in_project
    # load html if the json file doesn't contain a description
    if 'description' not in selected:
        path = "projects"
        selected['description'] = io.open(get_static_file(
            'static/%s/%s/%s.html' % (path, selected['link'], selected['link'])), "r", encoding="utf-8").read()
    return render_template('project.html', project=selected)
