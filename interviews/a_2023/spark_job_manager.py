"""
Implement an api that accomplishes

1. User create new job
2. User can cancel his job
3. User can view all his jobs
4. User can view his past N completed jobs
5. View logs for a job using jobId
"""


from collections import OrderedDict


class Job:
    VALID_STATUSES = {'Active', 'Cancelled', 'Completed'}

    def __init__(self, job_id, user_id, status, out_path):
        self.job_id = job_id
        self.user_id = user_id
        self.set_status(status)
        self.out_path = out_path

    def set_status(self, status):
        if status in self.VALID_STATUSES:
            self.status = status
        else:
            raise ValueError("Invalid status value")


class JobQueue:
    def __init__(self):
        self.queue = OrderedDict()

    def add_job(self, job_id, job):
        self.queue[job_id] = job

    def remove_job(self, job_id):
        if job_id in self.queue:
            del self.queue[job_id]
            return True
        return False

    def get_job(self, job_id):
        return self.queue.get(job_id, None)

    def get_all_jobs(self):
        return self.queue.items()


class JobManager:
    def __init__(self):
        self.job_queue = JobQueue()
        self.user_job_map = {}
        self.jobs_archive = {}

    def create_job(self, job: Job):
        user_id = job.user_id
        job_id = job.job_id
        self.job_queue.add_job(job)
        if user_id not in self.user_job_map:
            self.user_job_map[user_id] = [{}, {}, []]
        self.user_job_map[user_id][0][job_id].append(job)
        self.jobs_archive[job_id] = job
        job.set_status(Job.VALID_STATUSES[0])

    def cancel_job(self, job: Job):
        user_id = job.user_id
        job_id = job.job_id
        if self.job_queue.remove_job(job_id):
            del self.user_job_map[user_id][0][job_id]
            self.user_job_map[user_id][1][job_id] = job
            job.set_status(Job.VALID_STATUSES[1])

    def view_jobs(self, user_id):
        user_jobs = self.user_job_map[user_id]
        return user_jobs  # create json?

    def get_completed_jobs(self, user_id, N):
        return self.user_job_map[user_id][2][-N:]
