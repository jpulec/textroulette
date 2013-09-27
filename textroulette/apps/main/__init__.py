import logging

from textroulette.apps.main.tasks import check_for_messages

logger = logging.getLogger(__name__)


def init_scheduler():

    import django_rq
    import tasks
    from collections import defaultdict
    import datetime

    scheduler = django_rq.get_scheduler('default')

    jobs = scheduler.get_jobs()

    functions = defaultdict(lambda: list())

    map(lambda x: functions[(x.func, x.args)].append(x.meta), jobs)

    now = datetime.datetime.now()

    def schedule_once(func, *args, **kwargs):
        if not (func) in functions or not args in functions[(func)] or not kwargs in functions[(func)] or len(functions[(func)]) > 1:
            map(scheduler.cancel, filter(lambda x: (x.func, x.args)==(func), jobs))
            scheduler.schedule(now, func, *args, **kwargs)

    schedule_once(check_for_messages, interval=30, timeout=-1)

init_scheduler()
