FROM node:14

WORKDIR /usr/src/app/whykingz

COPY ./whykingz/package.json ./
COPY ./whykingz/package-lock.json ./

RUN npm install

EXPOSE 3000

CMD ["npm", "run", "serve", "--", "--port", "3000"]
