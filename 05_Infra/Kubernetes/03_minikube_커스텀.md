```yaml
kind: Pod
apiVersion: v1
metadata:
name: foo-app
labels:
    app: foo
spec:
containers:
    - name: foo-app
    image: 'kicbase/echo-server:1.0'
---
kind: Service
apiVersion: v1
metadata:
name: foo-service
spec:
selector:
    app: foo
ports:
    - port: 8080
---
kind: Pod
apiVersion: v1
metadata:
name: bar-app
labels:
    app: bar
spec:
containers:
    - name: bar-app
    image: 'kicbase/echo-server:1.0'
---
kind: Service
apiVersion: v1
metadata:
name: bar-service
spec:
selector:
    app: bar
ports:
    - port: 8080


--- 
kind: Pod
apiVersion: v1
metadata:
name: server_1-app
labels:
    app: server_1
spec:
containers:
    - name: server_1-app
    image: 'kicbase/echo-server:1.0'
---
kind: Service
apiVersion: v1
metadata:
name: server_1-service
spec:
selector:
    app: server_1
ports:
    - port: 8081
---
kind: Pod
apiVersion: v1
metadata:
name: server_2-app
labels:
    app: server_2
spec:
containers:
    - name: server_2-app
    image: 'kicbase/echo-server:1.0'
---
kind: Service
apiVersion: v1
metadata:
name: server_2-service
spec:
selector:
    app: server_2
ports:
    - port: 8082
---


apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
name: example-ingress
spec:
rules:
    - http:
        paths:
        - pathType: Prefix
            path: /foo
            backend:
            service:
                name: foo-service
                port:
                number: 8080
        - pathType: Prefix
            path: /bar
            backend:
            service:
                name: bar-service
                port:
                number: 8080
        - pathType: Prefix
            path: /server_1
            backend:
            service:
                name: server_1-service
                port:
                number: 8081
        - pathType: Prefix
            path: /server_2
            backend:
            service:
                name: server_2-service
                port:
                number: 8082
```

- 참고 : https://pokers.tistory.com/30

# Local iamge minikube에서 사용하기
- local docker와 minikube docker-daemon 연결하기
    - local docker image 저장소와 minikube image 저장소를 sync
    - docker image build시 local과 minikube 양쪽에 업로드

## local docker와 minikube docker-daemon의 연결
- 해당 명령어는 해당 터미널에서만 적용됨
```bash
# minikube의 설정 및 command 확인
minikube docker-env

# minikube docker-daemon과 연결
eval $(minikube -p minikube docker-env)

# 연결 취소
eval $(minikube -p minikube docker-env --unset)
```

## docker image 생성
```bash
docker build -t {image_name} .
# docker build -t server_1:1.0 .
```
## image pull policy
- `imagePullPolicy : Never` 로 설정하기
```bash
# 예시
apiVersion: apps/v1
kind: Deployment
metadata:
  name: go-example-docker
spec:
  replicas: 3
  selector:
    matchLabels:
      app: go-example-docker
      tier: web-app
  template:
    metadata:
      labels:
        app: go-example-docker
        tier: web-app
    spec:
      containers:
      # To use local docker images, see link blog :
        - name: go-example-docker
          image: example-docker-img:latest
          imagePullPolicy: Never # 설정
          resources:
            limits:
              memory: "128M"
              cpu: "500m"
          ports:
            - containerPort: 8080
              protocol: TCP
```
- 특정 포드의 yaml파일 열어보기
```bash
$ kubectl get pod bar-app -o yaml

apiVersion: v1
kind: Pod
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"labels":{"app":"bar"},"name":"bar-app","namespace":"default"},"spec":{"containers":[{"image":"kicbase/echo-server:1.0","name":"bar-app"}]}}
  creationTimestamp: "2024-03-08T06:17:28Z"
  labels:
    app: bar
  name: bar-app
  namespace: default
  resourceVersion: "750"
  uid: c654a30e-78a2-4755-973d-56e9eed06d6c
spec:
  containers:
  - image: kicbase/echo-server:1.0
    imagePullPolicy: IfNotPresent
    name: bar-app
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-6dzbm
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: minikube
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-6dzbm
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2024-03-08T06:17:28Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2024-03-08T06:17:36Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2024-03-08T06:17:36Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2024-03-08T06:17:28Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: docker://579fc169e4532bffa4586da482cd8f80077e330c1defd6fac38aab7b065a981c
    image: kicbase/echo-server:1.0
    imageID: docker-pullable://kicbase/echo-server@sha256:127ac38a2bb9537b7f252addff209ea6801edcac8a92c8b1104dacd66a583ed6
    lastState: {}
    name: bar-app
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2024-03-08T06:17:35Z"
  hostIP: 172.24.154.68
  phase: Running
  podIP: 10.244.0.9
  podIPs:
  - ip: 10.244.0.9
  qosClass: BestEffort
  startTime: "2024-03-08T06:17:28Z"

```