from . import bp
from flask.views import MethodView
from app.schemas import JobQueryArgsSchema, JobSchema


@bp.route('/teste')
class Jobs(MethodView):
    @bp.arguments(JobQueryArgsSchema, location='query')
    @bp.response(JobSchema(many=True))
    def get(self, args):
        return "Hello apiii"


@bp.route('/teste22')
class Jobs2(MethodView):
    @bp.arguments(JobQueryArgsSchema, location='query')
    @bp.response(JobSchema(many=True))
    def get(self, args):
        return "Hello apiii"
