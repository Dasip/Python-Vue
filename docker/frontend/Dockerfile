FROM node:14

WORKDIR /usr/src/app/frontend

COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "serve", "--", "--port", "3000"]
