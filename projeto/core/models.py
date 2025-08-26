from django.db import models

# Significa que ele só vai atualizar a data quando criar alguma coisa
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'Criado em',
        auto_now_add=True,
        auto_now =False
    )
    # Significa que ele vai atualizar a data toda vez que modificar algum registro
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True    
    )

    #significa que vou usar ele como herença de classes em outros models mais a frente
    class Meta:
        abstract =  True