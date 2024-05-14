from locust import FastHttpUser, task

data = {"input": 1.0}


class LitUser(FastHttpUser):
    # wait_time = between(1, 5)

    @task
    def predict(self):
        self.client.post("/predict", json=data)
