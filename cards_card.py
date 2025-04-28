class Card(models.Model):
    deck = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        related_name='cards'
    )
    json_data = models.JSONField()
    quality = models.FloatField(default=1)
    ef = models.FloatField(default=1.3)
    repetitions = models.FloatField(default=0.0)
    interval = models.FloatField(default=1)
    due_date = models.DateTimeField(default=timezone.now)