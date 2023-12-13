from locust import HttpUser, task, between, TaskSet

class MyUser(HttpUser):
    wait_time = between(2,5)
    
    @task(1)
    def view_homepage(self):
        self.client.get("/")