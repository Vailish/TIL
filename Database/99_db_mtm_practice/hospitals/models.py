from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')  # 다대다에서는 복수형으로 써줌
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
    # ManyToManyField에서는 해당 데이터에 말고 알아서 관계 테이블을 만들어서 넣어줌. 어디에 넣어도 상관 없지만
    # 참조 역참조가 바뀌니까 어떻게 읽는게 편한지 생각해서 만들어 주면 됨.
    # 추가할때 patient1.doctors.add(dcotor1) /// doctor1.patient_set.add(patient2) /// add : 관계가 맺어진다
    # 조회할때 patient1.doctors.all() /// doctor1.patient_set.all()
    # 삭제할때 patient2.doctors.remove(doctor1) /// doctor1.patient_set.remove(patient1)
    # related_name 이걸 써서 patient_set을 바꿔서 patients로 바꾸면 깔끔하게 할 수 있음. related_name='patients'
    # 2만의 관계가 아닌 추가 데이터면 through를 사용해서 중개테이블 써야함.
    # patient2.doctors.add(doctor1, through_defaults={'symptom': 'flue'}) <- 추가 데이터가 필요하므로, through_defaults 뒤에 dictionary로 써주면됨.


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
