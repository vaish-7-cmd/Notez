from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # voice_note = models.FileField(upload_to='voice_notes/', blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='note_images/', blank=True, null=True)  # 👈 Add this!
    # created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField(default=False)  # New field for pinning notes

    class Meta:
       ordering = ['-created_at']
    class Meta:
        unique_together = ('title', 'content')

    def __str__(self):
        return self.title
