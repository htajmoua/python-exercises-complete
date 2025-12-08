from celery import Celery

app = Celery('tasks',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Paris',
    enable_utc=True,
)

# Test de configuration
if __name__ == '__main__':
    print("Configuration Celery:")
    print(f"  Broker: {app.conf.broker_url}")
    print(f"  Backend: {app.conf.result_backend}")
    print("✓ Configuration chargée avec succès")
