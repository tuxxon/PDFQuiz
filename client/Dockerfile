# 베이스 이미지로 Node.js 사용
FROM node:18

# 작업 디렉터리 설정
WORKDIR /app

# 패키지 설치를 위한 package.json 및 package-lock.json 복사
COPY package.json ./
COPY package-lock.json ./

# 패키지 설치
RUN npm install

# 애플리케이션 파일 복사
COPY . .

# 빌드 명령 실행 (빌드 후에는 production 모드로 Serve)
RUN npm run build

# Serve를 사용하여 빌드된 파일 제공
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
