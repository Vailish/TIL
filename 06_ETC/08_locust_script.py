from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    # host = "127.0.0.1:8080"
    host = 'http://localhost:8080/'
   
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    @task
    def index(self):
        self.client.get("/")  # 메인 화면 요청

        