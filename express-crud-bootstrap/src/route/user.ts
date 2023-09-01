import {Router} from 'express';
import UserController from "../controller/user/user-controller";

const userRouter = Router();

//userRouter.get('/:id', findOne);
userRouter.post('/', UserController.create);
//userRouter.put('/:id', update);
//userRouter.delete('/:id', destroy);

export default userRouter;
