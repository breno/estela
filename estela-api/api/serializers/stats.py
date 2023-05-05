from rest_framework import serializers


class LogsStatsSerializer(serializers.Serializer):
    total_logs = serializers.IntegerField(default=0)
    debug_logs = serializers.IntegerField(default=0)
    info_logs = serializers.IntegerField(default=0)
    warning_logs = serializers.IntegerField(default=0)
    error_logs = serializers.IntegerField(default=0)
    critical_logs = serializers.IntegerField(default=0)


class JobsStatsSerializer(serializers.Serializer):
    total_jobs = serializers.IntegerField(default=0)
    running_jobs = serializers.IntegerField(default=0)
    error_jobs = serializers.IntegerField(default=0)
    unknown_jobs = serializers.IntegerField(default=0)
    finished_jobs = serializers.IntegerField(default=0)


class PagesStatsSerializer(serializers.Serializer):
    total_pages = serializers.IntegerField(default=0)
    scraped_pages = serializers.IntegerField(default=0)
    missed_pages = serializers.IntegerField(default=0)


class StatusCodesStatsSerializer(serializers.Serializer):
    status_200 = serializers.IntegerField(default=0)
    status_301 = serializers.IntegerField(default=0)
    status_302 = serializers.IntegerField(default=0)
    status_401 = serializers.IntegerField(default=0)
    status_403 = serializers.IntegerField(default=0)
    status_404 = serializers.IntegerField(default=0)
    status_429 = serializers.IntegerField(default=0)
    status_500 = serializers.IntegerField(default=0)


class StatsSerializer(serializers.Serializer):
    jobs = JobsStatsSerializer()
    pages = PagesStatsSerializer()
    items_count = serializers.IntegerField(default=0)
    runtime = serializers.FloatField(default=0.0)
    status_codes = StatusCodesStatsSerializer()
    success_rate = serializers.FloatField(default=0.0)
    logs = LogsStatsSerializer()


class GlobalStatsSerializer(serializers.Serializer):
    date = serializers.DateField(format="%Y-%m-%d")
    stats = StatsSerializer()


class SpidersJobsStatsSerializer(GlobalStatsSerializer):
    pass