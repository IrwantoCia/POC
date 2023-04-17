import express, { Express } from 'express';
import dotenv from 'dotenv';
import bodyParser from 'body-parser';
import cors from 'cors';
import routes from './src/route';

dotenv.config();

const app: Express = express();
const port = process.env.PORT;

app.use(cors({
    origin: '*',
    methods: 'OPTIONS,GET,PUT,POST,DELETE',
    allowedHeaders: ['Content-Type', 'Authorization', 'Accept-Language', 'X-Api-Key', 'X-Amz-Date', 'X-Amz-Security-Token'],
    credentials: true,
    optionsSuccessStatus: 200
}));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(routes);

app.listen(port, () => {
    console.log(`⚡️[server]: Server is running at port ${port}`);
});