from locust import HttpUser, TaskSet, task, between





class UserBehaviour(TaskSet):

    @task
    def like_post(self):
        # For now we have only 1 post_id else use random it u have multiple ids
        post_id = 1
        
        # fill with endpoint
        self.client.get(
            f'/post_like/{post_id}/', # endpoint
            data = {}, # data
            headers = {"Content-Type" : "application/json"},
        )  # get(), post(), put(), delete(), patch()


class WebsiteUser(HttpUser):
    tasks = [UserBehaviour]
    wait_time = between(1, 2)


# locust (run in terminal)