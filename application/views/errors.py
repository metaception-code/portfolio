from flask import render_template

from application.views.base import base_blueprint


@base_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('error-page.html', error='Page not found, try find better'), 404


@base_blueprint.errorhandler(500)
def service_unavailable(e):
    return render_template('error-page.html', error="Service error, me sorry."), 500


