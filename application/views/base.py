from flask import render_template, Blueprint

base_blueprint = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)


@base_blueprint.route('/')
def index():
    return render_template('home.html')


@base_blueprint.route('/skills')
def skills():
    return render_template('skills.html')


@base_blueprint.route('/timeline')
def timeline():
    return render_template('timeline.html', resume_pdf_link="")








