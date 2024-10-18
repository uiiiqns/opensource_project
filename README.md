# <프로젝트 주제 :  과외 및 멘토링 튜터를 위한 학습 관리 어플>


## 목차
1. 프로젝트 개요
2. 주요 기능
3. 기술 스택

****

### 1. 프로젝트 개요

> 이 프로젝트는 클라우드 스토리지, Firebase, 화상 플랫폼 통합 기능을 통해 튜터가 학생의 학습 자료를 관리하고, 출석 및 집중도를 실시간으로 모니터링할 수 있게 한다. 또한 피드백 기능으로 학부모에게 학습에 대한 피드백을 제공하는 기능도 지원한다.
- 프론트 엔드 : 튜터가 사용하는 인터페이스로, 자료 업로드, 시간표 관리, 집중도 모니터링, 피드백 전송이 가능하다.
- 자료 처리 및 저장을 담당하며, 클라우드 스토리지와 Firebase로 시간표를 관리한다.

****

### 2. 주요 기능
- 수업 자료 관리 : 클라우드 스토리지를 사용하여 대용량의 학습 자료를 저장하고 공유한다.
- 학생 출석 및 집중도 모니터링 : OpenCV 및 TensorFlow Lite를 사용해 학생의 집중도를 분석하고 실시간으로 모니터링한다.
- 학부모 피드백 자동 전송 : Firebase Cloud Messaging을 통해 학부모에게 학생의 학습 상황에 대한 피드백을 자동으로 전송한다.
- 학생별 시간표 관리 : Google Calendar API를 통해 다수의 학생 일정을 색상별로 관리할 수 있다.

****

### 3. 기술 스택
- 프론트엔드 : Flutter
- 백엔드 : Node.js, Express
- 데이터베이스 : Firebase
- 클라우드 스토리지 : Google Cloud Storage
- 화상 플랫폼 통합 : Zoom SDK, Jitsi Meet API

****

*관련 링크*
1. [Firebase Documentation](https://firebase.google.com/docs/reference/fcm/rest?hl=ko)
2. [Google Cloud Storage Documentation](https://cloud.google.com/storage/docs?hl=ko)

  
