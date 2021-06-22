import uuid
from ***REMOVED***.conf import settings
from ***REMOVED***.contrib.auth.models import User
from ***REMOVED***.db import models
from urllib.parse import urlparse


class Project(models.Model):
    pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1000)
    users = models.ManyToManyField(User)

    @property
    def container_image(self):
        parsed_container_host = urlparse(settings.REGISTRY_HOST)
        container_image = "{}/{}:bm_{}".format(
            parsed_container_host.netloc,
            settings.REPOSITORY_NAME,
            self.pid,
        )
        return container_image


class Spider(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="spiders"
    )


class SpiderJob(models.Model):
    WAITING_STATUS = "WAITING"
    RUNNING_STATUS = "RUNNING"
    COMPLETED_STATUS = "COMPLETED"
    STATUS_OPTIONS = [
        (WAITING_STATUS, "Waiting"),
        (RUNNING_STATUS, "Running"),
        (COMPLETED_STATUS, "Completed"),
    ]

    jid = models.AutoField(primary_key=True)
    spider = models.ForeignKey(Spider, on_delete=models.CASCADE, related_name="jobs")
    status = models.CharField(
        max_length=16, choices=STATUS_OPTIONS, default=WAITING_STATUS
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ["created"]

    @property
    def name(self):
        return "{}-{}".format(self.spider.project.pid, self.jid)


class SpiderJobArg(models.Model):
    aid = models.AutoField(primary_key=True)
    job = models.ForeignKey(SpiderJob, on_delete=models.CASCADE, related_name="args")
    name = models.CharField(max_length=1000)
    value = models.CharField(max_length=1000)
