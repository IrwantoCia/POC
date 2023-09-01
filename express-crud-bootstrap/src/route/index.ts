import {Router} from "express";
import userRouter from "./user";

const routes = Router();

routes.get('/', (req, res) => {
    res.send('check health');
} );

routes.use('/user', userRouter);

export default routes;
