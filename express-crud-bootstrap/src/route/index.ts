import {Router} from "express";
import user from "./user";

const routes = Router();

routes.get('/', (req, res) => {
    res.send('check health');
} );

routes.use('/user', user);

export default routes;