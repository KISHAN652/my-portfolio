from djongo import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # ✅ Add this line

    def __str__(self):
        return f"{self.name} - {self.email}"
