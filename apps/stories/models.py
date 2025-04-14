from django.db import models
from apps.users.models import User
from django.utils import timezone


class Story(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories')
    image = models.ImageField(upload_to='stories/')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    story_views = models.ManyToManyField(User, through='StoryView', related_name='story_views', blank=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timezone.timedelta(hours=24)  # 24 soat keyin tugaydi
        super().save(*args, **kwargs)

    def get_story_viewers(self):
        return self.story_views.all()

    def get_story_view_count(self):
        return self.story_views.count()

    def __str__(self):
        return f"Story {self.id} by {self.user.username} created at {self.created_at}"


class StoryLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_likes')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'story')
        verbose_name = "Story Like"
        verbose_name_plural = "Story Likes"

    def __str__(self):
        return f"Like by {self.user.username} for Story {self.story.id}"


class StoryView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_views_history')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='story_views_history')
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'story')
        verbose_name = "Story View"
        verbose_name_plural = "Story Views"

    def __str__(self):
        return f"{self.user.username} viewed Story {self.story.id} at {self.viewed_at}"

