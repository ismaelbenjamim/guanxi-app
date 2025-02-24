import logging
import os
from celery import Celery
from celery.exceptions import CeleryError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guanxi_app.settings')

app = Celery('guanxi_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# ===========================================
# 1. Defina sua exceção personalizada
# ===========================================
class NoTracebackError(CeleryError):
    """Exceção para falhas sem traceback extenso no log."""
    pass


# ===========================================
# 2. Defina seu filter
# ===========================================
class NoTracebackFilter(logging.Filter):
    """
    Remove 'exc_info' se for NoTracebackError,
    assim o Celery não imprime traceback.
    """
    def filter(self, record: logging.LogRecord) -> bool:
        if record.exc_info and isinstance(record.exc_info[1], NoTracebackError):
            record.exc_info = None  # Remove o traceback
        return True


def setup_celery_logging():
    # Pega o logger do worker Celery (pode variar conforme a versão)
    logger_celery_worker = logging.getLogger('celery.worker')
    # Em algumas versões, o logger é 'celery.app.trace' ou similar
    logger_celery_app = logging.getLogger('celery.app.trace')

    logger_celery_worker.addFilter(NoTracebackFilter())
    logger_celery_app.addFilter(NoTracebackFilter())


# ===========================================
# 3. Chamar a função logo após configurar o app
# ===========================================
setup_celery_logging()
